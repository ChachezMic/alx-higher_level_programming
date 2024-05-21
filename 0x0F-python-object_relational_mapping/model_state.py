#!/usr/bin/python3
"""list all states"""

from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine/
('mysql://user:password@localhost:3306/your_database_name')
Base = declarative_base()
metadata = MetaData()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
states = session.query(State).all()
for state in states:
    print(f"State ID: {state.id}, Name: {state.name}")

session.close()
