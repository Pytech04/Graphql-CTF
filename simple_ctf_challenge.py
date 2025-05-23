#!/usr/bin/env python3
"""
Simple GraphQL IDOR CTF Challenge
No Docker required - just run with Python!
Perfect for university cybersecurity education
"""

from flask import Flask, render_template_string
import graphene
from flask_graphql import GraphQLView
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "ctf_university_secret_2024"

# Simple in-memory user data for the CTF challenge
USERS_DATA = [
    {"id": 1, "username": "attacker", "email": "attacker@example.com", "role": "user", "flag": None},
    {"id": 2, "username": "victim", "email": "victim@example.com", "role": "user", "flag": None},
    {"id": 3, "username": "admin", "email": "admin@ctfsecure.com", "role": "admin", "flag": "CTF{graphql_idor_pwned_2024}"},
    {"id": 4, "username": "support", "email": "support@example.com", "role": "support", "flag": None},
    {"id": 5, "username": "guest", "email": "guest@example.com", "role": "guest", "flag": None}
]

# GraphQL Types
class User(graphene.ObjectType):
    id = graphene.Int()
    username = graphene.String()
    email = graphene.String()
    role = graphene.String()
    flag = graphene.String()

class Query(graphene.ObjectType):
    me = graphene.Field(User, description="Get current user profile")
    user = graphene.Field(User, id=graphene.Int(required=True), description="Get any user by ID - IDOR vulnerability!")
    all_users = graphene.List(User, description="List all users")
    
    def resolve_me(self, info):
        """Current user (always returns user ID 1 for CTF)"""
        user_data = USERS_DATA[0]  # Always return first user (attacker)
        return User(**user_data)
    
    def resolve_user(self, info, id):
        """🚨 IDOR VULNERABILITY: No authorization check!"""
        for user_data in USERS_DATA:
            if user_data["id"] == id:
                return User(**user_data)
        return None
    
    def resolve_all_users(self, info):
        """Returns all users - also problematic"""
        return [User(**user_data) for user_data in USERS_DATA[:3]]  # Limit to first 3

schema = graphene.Schema(query=Query)

# Main page template
MAIN_PAGE = """
<!DOCTYPE html>
<html lang="en" data-bs-theme="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GraphQL IDOR CTF Challenge</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" rel="stylesheet">
</head>
<body>
    <div class="container py-5">
        <div class="row justify-content-center">
            <div class="col-lg-8">
                <div class="text-center mb-5">
                    <div class="d-inline-block p-3 rounded-circle bg-danger bg-opacity-10 mb-3">
                        <i class="fas fa-bug fa-2x text-danger"></i>
                    </div>
                    <h1 class="display-4 fw-bold text-light">GraphQL IDOR Challenge</h1>
                    <p class="lead text-muted">University Cybersecurity Education</p>
                </div>

                <div class="card border-secondary mb-4">
                    <div class="card-header bg-secondary bg-opacity-25">
                        <h3 class="card-title mb-0">
                            <i class="fas fa-crosshairs me-2 text-danger"></i>
                            Challenge Objective
                        </h3>
                    </div>
                    <div class="card-body">
                        <p>Exploit the <strong>IDOR vulnerability</strong> in this GraphQL API to access the admin user's data and capture the flag!</p>
                        <div class="alert alert-info">
                            <i class="fas fa-flag me-2"></i>
                            <strong>Goal:</strong> Find the CTF flag in the admin user's profile (user ID 3)
                        </div>
                    </div>
                </div>

                <div class="card border-info mb-4">
                    <div class="card-header bg-info bg-opacity-25">
                        <h4 class="card-title mb-0">
                            <i class="fas fa-rocket me-2 text-info"></i>
                            How to Solve
                        </h4>
                    </div>
                    <div class="card-body">
                        <ol>
                            <li><strong>Access GraphQL:</strong> Click the button below to open GraphiQL</li>
                            <li><strong>Explore Schema:</strong> Use introspection to discover available queries</li>
                            <li><strong>Test Current User:</strong> Try the <code>me</code> query</li>
                            <li><strong>Exploit IDOR:</strong> Use <code>user(id: 3)</code> to access admin data</li>
                            <li><strong>Capture Flag:</strong> Extract the flag from the admin user's profile</li>
                        </ol>
                    </div>
                </div>

                <div class="text-center">
                    <a href="/graphql" class="btn btn-primary btn-lg">
                        <i class="fas fa-rocket me-2"></i>
                        Launch GraphiQL Interface
                    </a>
                </div>

                <div class="mt-4 text-center">
                    <small class="text-muted">Perfect for cybersecurity education and ethical hacking practice</small>
                </div>
            </div>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(MAIN_PAGE)

# Add GraphQL endpoint
app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

if __name__ == '__main__':
    print("🚀 Starting GraphQL IDOR CTF Challenge...")
    print("📚 Perfect for university cybersecurity education!")
    print("🎯 Challenge running at: http://localhost:5000")
    print("🔍 GraphQL interface: http://localhost:5000/graphql")
    print("🏆 Find the flag by exploiting the IDOR vulnerability!")
    print("")
    app.run(host='0.0.0.0', port=5000, debug=True)