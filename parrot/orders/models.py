#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime 
from parrot import app, db
from flask import Blueprint, abort, request, jsonify
from sqlalchemy import Column, Integer, DateTime, DECIMAL
from parrot.common import utils, config

class Orders(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(80), nullable=False)
    order_total = db.Column(db.Float(4))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def create_order(user_id, customer_name, order_amount):

        create_order = Orders(user_id=user_id, 
                             customer_name=customer_name, 
                             order_total=order_amount)
        db.session.add(create_order)
        db.session.commit()

        return create_order



class OrderItems(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(80), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    unit_price = db.Column(db.DECIMAL(20))
    product_amount = db.Column(db.DECIMAL(20))
    created_date = Column(DateTime, default=utils.time_now)


    @classmethod
    def products_report(self, start_date, end_date):

        sql_query = "SELECT order_items.product_name,"\
                    "SUM(order_items.product_amount) as products_amount FROM order_items "\
                    "WHERE created_date BETWEEN '%s' and '%s' group by product_name "\
                    "order by products_amount DESC"%(start_date, end_date)

        products = db.engine.execute(sql_query)

        return products

    def add_product(product_name, order_id, unit_price, product_amount):

        add_product = OrderItems(product_name=product_name, order_id=order_id, unit_price=unit_price, product_amount=product_amount)
        db.session.add(add_product)
        db.session.commit()

        return add_product


    def get_order(order_id):

        order_details  = OrderItems.query.filter_by(order_id=order_id).join(Orders,Orders.id == OrderItems.order_id).all()

        return order_details




    





