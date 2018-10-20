from sqlalchemy import Column, DateTime, String, BigInteger as Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
 
Base = declarative_base()
 
 
class Transaction(Base):
    __tablename__ = 'transactions'
    id = Column(Integer, primary_key=True)
    blockNumber = Column(Integer)
    cumulativeGasUsed = Column(Integer)
    gasUsed = Column(Integer)
    frm = Column(String)
    to = Column(String)
    transactionHash = Column(String)
    transactionIndex = Column(Integer)
 
class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    transaction_id = Column(Integer, ForeignKey(Transaction.id))
    contract_address = Column(String)
    event_name = Column(String)
    event_name = Column(String)
    frm = Column(String)
    to = Column(String)
    value = Column(Integer)
 
from sqlalchemy import create_engine
engine = create_engine('postgresql:///token')
 
from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
