#!/usr/bin/env python
# -*- coding: utf-8 -*-

from parrot import app, db
from passlib.apps import custom_app_context as pwd_context
from flask_login import UserMixin

class Users(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True)
    name = db.Column(db.String(40))
   
    def create_user(self, user_name, user_email):
        create_user = Users(email=user_email, name=user_name)
        db.session.add(create_user)
        db.session.commit()
    
    def search_by_email(user_email):

        filter_by_email = Users.query.filter_by(email=user_email).first()
        return filter_by_email





