import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from models import User
from app import db

class UserType(SQLAlchemyObjectType):
    """GraphQL User Type - exposes all user fields including sensitive data"""
    class Meta:
        model = User
        fields = ("id", "username", "email", "role", "flag")

class Query(graphene.ObjectType):
    """GraphQL Query root - contains vulnerable resolvers"""
    
    # Current user endpoint (simulates authenticated user)
    me = graphene.Field(UserType, description="Get current user profile")
    
    # VULNERABLE: Direct user access by ID without authorization
    user = graphene.Field(
        UserType, 
        id=graphene.Int(required=True),
        description="Get any user by ID - IDOR vulnerability present!"
    )
    
    # List all users (also problematic but less obvious)
    all_users = graphene.List(UserType, description="List all users")
    
    def resolve_me(self, info):
        """
        Simulates getting the current authenticated user
        In a real app, this would check session/JWT
        For the CTF, we always return user ID 1 (attacker)
        """
        current_user = db.session.get(User, 1)
        if not current_user:
            return None
        return current_user
    
    def resolve_user(self, info, id):
        """
        🚨 IDOR VULNERABILITY: No permission check!
        This resolver allows any user to query any other user's data
        including sensitive information like flags
        
        Proper implementation should check:
        - If current user is authenticated
        - If current user has permission to view target user
        - If target user exists and is accessible
        """
        # VULNERABLE CODE - NO AUTHORIZATION CHECK
        target_user = db.session.get(User, id)
        return target_user
    
    def resolve_all_users(self, info):
        """
        Returns all users - also problematic as it exposes user enumeration
        But participants need to discover the specific user(id) query
        """
        # Limit to first 10 users to not make it too obvious
        return User.query.limit(10).all()

# Create the GraphQL schema
schema = graphene.Schema(query=Query)
