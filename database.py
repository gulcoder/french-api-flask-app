from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Quote(Base):
    __tablename__ = 'quotes'
    id = Column(Integer, primary_key=True)
    text = Column(Text, nullable=False)
    author = Column(String(100), nullable=True)

# Koppla till PostgreSQL som vi startar via Docker
engine = create_engine('postgresql://minduser:mindpass@localhost:5432/mindfulnessdb')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
