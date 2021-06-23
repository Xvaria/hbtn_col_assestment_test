#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from models.basemodel import Base


class User(Base):
    """"""
    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    username = Column(String(60), nullable=False)
    passwd = Column(String(60), nullable=False)
    name = Column(String(60), nullable=False)
    lastname = Column(String(60), nullable=False)
    email = Column(String(60), nullable=False)
    company = Column(String(60), nullable=False)
    order = relationship("Order", back_populates="user")

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
