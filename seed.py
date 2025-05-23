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
                'username': 'attacker',
                'email': 'attacker@example.com',
                'role': 'user',
                'flag': None
            },
            {
                'id': 2,
                'username': 'victim',
                'email': 'victim@example.com', 
                'role': 'user',
                'flag': None
            },
            {
                'id': 3,
                'username': 'admin',
                'email': 'admin@ctfsecure.com',
                'role': 'admin',
                'flag': 'CTF{graphql_idor_pwned_2024}'
            },
            {
                'id': 4,
                'username': 'support',
                'email': 'support@example.com',
                'role': 'support',
                'flag': None
            },
            {
                'id': 5,
                'username': 'guest',
                'email': 'guest@example.com',
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
