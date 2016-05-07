from sqlalchemy.schema import Column, Index
from sqlalchemy.types import Integer, String, Text, TIMESTAMP,VARCHAR
from sqlalchemy.dialects.mysql import TINYINT
from app import app, db
from flask_login import UserMixin

class User(db.Model, UserMixin):
  __tablename__ = 'user'
  id = Column(Integer, primary_key=True)
  username = Column(String(255), nullable=False)
  truename = Column(String(255), nullable=False)
  password = Column(String(64), nullable=False)
  email = Column(String(255), nullable=False, unique=True)
  role = Column(TINYINT(2), nullable=False)
  created = Column(TIMESTAMP, nullable=False, server_default='0000-00-00 00:00:00')
  def __init__(self, username, truename, password, email, role, created):
    self.username = username
    self.truename = truename
    self.password = password
    self.email = email
    self.role = role
    self.created = created

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    return self.id

  def __repr__(self):
    return '<User %r>' % (self.email)

