#!/usr/bin/python3
from sqlalchemy import Column, String, Integer, Sequence
from sqlalchemy.orm import relationship
from models.basemodel import Base


class Shipping(Base):
    """"""
    __tablename__ = "shippings"
    id = Column(String(60), primary_key=True)
    address = Column(String(60), nullable=False)
    city = Column(String(60), nullable=False)
    state = Column(String(60), nullable=False)
    country = Column(String(60), nullable=False)
    cost = Column(String(60), nullable=False)
    order = relationship("Order", back_populates="shipping", uselist=False)

    # def __init__(self, id, username, passwd, name, lastname, email, company):
    #     self.id = id
    #     self.username = username
    #     self.passwd = passwd
    #     self.name = name
    #     self.lastname = lastname
    #     self.email = email
    #     self.company = company
