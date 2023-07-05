from flask import Blueprint, request
import logging, traceback

from ..services.auth import *

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
  message = ''
  try:
    data = request.json
    user_data = {
      'email': data['email'],
      'password': data['password']
    }
    message = login_service(user_data)
  except Exception as e:
    return {
      'success': False,
      'message': traceback.format_exc()
    }
  
  return {
    'success': True,
    'message': message
  }


@auth.route('/signup', methods=['POST'])
def signup():
  message = ''
  try:
    data = request.json
    user_data = {
      'email': data['email'],
      'name': data['name'],
      'password': data['password']
    }
    message = signup_service(user_data)
  except Exception as e:
    return {
      'success': False,
      'message': traceback.format_exc()
    }
  
  return {
    'success': True,
    'message': message
  }
