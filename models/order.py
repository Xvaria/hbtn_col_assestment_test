#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from models.basemodel import Base


class Order(Base):
    """Table user with many-to-one realtionship"""
    __tablename__ = "orders"
    id = Column(String(60), primary_key=True)
    date = Column(String(60), nullable=False)
    total = Column(String(60), nullable=False)
    subtotal = Column(String(60), nullable=False)
    taxes = Column(String(60), nullable=False)
    paid = Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'))
    user = relationship("User", back_populates="order")

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
