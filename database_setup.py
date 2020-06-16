
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import create_engine


Base = declarative_base()

class Log_table(Base):


   __tablename__ = 'payments'

   id = Column(Integer, primary_key=True)
   amount = Column(String(20))
   currency = Column(String(3))
   send_time = Column(String(25))
   payment_id = Column(String(25))
   description = Column(String(250))


engine = create_engine('sqlite:///paymentdb.db')
# print('created')

Base.metadata.create_all(engine)