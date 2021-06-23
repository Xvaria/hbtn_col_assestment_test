#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models.order import Order
from models.user import User
from models.basemodel import Base
import uuid


if __name__ == '__main__':
   class dbstorage:
      engine = create_engine('mysql+mysqldb://admin_01:admin_01_pwd@localhost/hbtn_col')
      Base.metadata.create_all(engine, checkfirst=True)
      Session = sessionmaker(bind=engine)
      session = Session()

      def __init__(self):
         """"""
         id_user = str(uuid.uuid4())
         info_user = User(**{'id': id_user,'username': 'Xvaria', 'passwd': '123',
                           'name': 'Diego','lastname': 'Ahumada',
                           'email': '123@ejemplo.com','company': 'DreamAhu'})
         self.session.add(info_user)
         self.session.commit()
         self.order(id_user)

      def order(self, id_user):
         order_user = str(uuid.uuid4())
         info_order = Order(**{'id': order_user, 'date': '2021-06-23',
                               'total': '1.000.000', 'subtotal': '750.000',
                               'taxes': '250.000', 'paid': '1.000.000',
                               'user_id': id_user})
         self.session.add(info_order)
         self.session.commit()

   dbstorage()
