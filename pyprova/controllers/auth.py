from flask import Blueprint, request
import logging, traceback

from ..services.auth import *


auth = Blueprint('auth', __name__)

""" Handles the login post request 

Returns:
    dict: boolean, str
"""
@auth.route('/login', methods=['POST'])
def login():
  message = ''
  try:
    data = request.json
    user_data = {'email': data['email'], 'password': data['password']}
    message = login_service(user_data)
  except Exception as e:
    return {'success': False,'message': traceback.format_exc()}
  return {'success': True,'message': message}


""" Handles the signup post request

Returns:
    dict: boolean, str
"""
@auth.route('/signup', methods=['POST'])
def signup():
  message = ''
  try:
    data = request.json
    user_data = {'email': data['email'],'name': data['name'],'password': data['password'], 'profile_type': data['profile']}
    message = signup_service(user_data)
  except Exception as e:
    return {'success': False,'message': traceback.format_exc()}
  return {'success': True,'message': message}


@auth.route('/user', methods=['GET'])
def get_user():
  response = {}
  try:
    email = request.args.get("email")
    response = get_user_by_email(email)
  except Exception as e:
    return {'success': False,'message': traceback.format_exc()}
  return {'success': True,'response': response}