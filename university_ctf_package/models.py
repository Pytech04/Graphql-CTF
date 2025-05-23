from app import db
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String

class User(db.Model):
    """User model for the CTF challenge"""
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(80), nullable=False)
    email: Mapped[str] = mapped_column(String(120), nullable=False)
    role: Mapped[str] = mapped_column(String(50), nullable=False, default='user')
    flag: Mapped[str] = mapped_column(String(255), nullable=True)
    
    def __repr__(self):
        return f'<User {self.username}>'
