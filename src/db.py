from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from os import environ

host=environ.get('HOST', '')
database=environ.get('DATABASE', '')
user=environ.get('USER', '')
password=environ.get('PASSWORD', '')
port=environ.get('PORT', 5432)

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)
Base = declarative_base()