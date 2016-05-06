from sqlalchemy.schema import Column, Index
from sqlalchemy.types import Integer, String, Text, TIMESTAMP,VARCHAR
from sqlalchemy.dialects.mysql import TINYINT
from app import app, db

class User(db.Model):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False)
  truename = Column(String(255), nullable=False)
  email = Column(String(255), nullable=False)
  role = Column(TINYINT(2), nullable=False)
  created = Column(TIMESTAMP, nullable=False, server_default='0000-00-00 00:00:00')
  def __init__(self, username, truename, email, role, created):
    self.username = username
    self.truename = truename
    self.email = email
    self.role = role
    self.created = created
