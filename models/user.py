#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, PrimaryKeyConstraint
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    # Define the primary key constraint
    id = Column(String(60), primary_key=True, nullable=False)
    reviews = relationship("Review", backref="user", cascade="all, delete-orphan")
