import logging
from app import db
from models import User

def seed_database():
    """Seed the database with CTF challenge data"""
    try:
        # Create users for the challenge
        users_data = [
            {
                'id': 1,
                'username': 'pyt3ch',
                'email': 'pyt3ch@ctfnfsu.com',
                'role': 'user',
                'flag': None
            },
            {
                'id': 2,
                'username': 'victim',
                'email': 'victim@ctfnfsu.com', 
                'role': 'user',
                'flag': None
            },
            {
                'id': 3,
                'username': 'admin',
                'email': 'admin@ctfnfsu.com',
                'role': 'admin',
                'flag': 'CTF{graphql_love_leak_idor_flame}'
            },
            {
                'id': 4,
                'username': 'support',
                'email': 'support@ctfnfsu.com',
                'role': 'support',
                'flag': None
            },
            {
                'id': 5,
                'username': 'guest',
                'email': 'guest@ctfnfsu.com',
                'role': 'guest',
                'flag': None
            }
        ]
        
        for user_data in users_data:
            # Check if user already exists
            existing_user = User.query.get(user_data['id'])
            if not existing_user:
                user = User(
                    id=user_data['id'],
                    username=user_data['username'],
                    email=user_data['email'],
                    role=user_data['role'],
                    flag=user_data['flag']
                )
                db.session.add(user)
        
        db.session.commit()
        logging.info("Database seeded successfully with CTF challenge data")
        
    except Exception as e:
        logging.error(f"Error seeding database: {e}")
        db.session.rollback()
        raise

if __name__ == "__main__":
    from app import app
    with app.app_context():
        seed_database()
