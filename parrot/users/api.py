#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytz
import openpay
from flask import Blueprint, request
from flask_restful import reqparse, Api, Resource
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from datetime import datetime, timedelta
from parrot import app, login_manager
from parrot.users.models import Users
from parrot.common import utils, config


parser = reqparse.RequestParser()
users = Blueprint('users', __name__, url_prefix="/api/v1")

"""
User management module.
"""
class User(Resource):

    def get(self):
        """ List all users. """
        pass


    def post(self):

        """ Register a new user. """

        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        args = parser.parse_args()

        user_email = args['email']
        user_name = args['name']

        filter_by_email = Users.search_by_email(user_email)

        if filter_by_email:
            return { 'message':'The mail is already in use'}, 409

        users = Users()
        users.create_user(user_name, user_email)

        return { 'message':'User successfully registered' }, 201

    def put(self,id):
        """ Update User """
        pass 


api = Api(users)
api.add_resource(User, "/users/")
