from werkzeug.security import generate_password_hash, check_password_hash
from ..models.user import User
from .. import db


def signup_service(user_data):
  user = User.query.filter_by(email=user_data['email']).first()
  
  if user:
    return 'User already registered!'
  
  new_user = User(email=user_data['email'], name=user_data['name'], 
  password=generate_password_hash(password=user_data['password'], method='sha256'))
  
  db.session.add(new_user)
  db.session.commit()
  
  return 'Successfully registered!'


def login_service(user_data):
  user = User.query.filter_by(email=user_data['email']).first()

  if not user or not check_password_hash(user.password, user_data['password']):
    return 'Please check your login details and try again.'

  return 'token'