import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Enum
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

from enum import Enum as PyEnum

class Nature(PyEnum):
    PLANET = 'planet'
    CHARACTER = 'character'

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250), nullable=False)
    firstname = Column(String(250), nullable=False)
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    password = Column(String(100), nullable=False)

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    url = Column(String(250))
    orbital_period = Column(String(250), nullable=False)
    gravity = Column(String(250))
    diameter = Column(Integer)
    climate = Column(String(250))

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    fullname = Column(String(250))
    birth_year = Column(String(20))
    hair_color = Column(String(50))
    height = Column(Integer)
    weight = Column(Integer)

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    nature = Column(Enum(Nature), nullable=False)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    user = relationship(User)
    planet = relationship(Planet)
    character = relationship(Character)


## Draw from SQLAlchemy base
try:
    render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
