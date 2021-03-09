#!/usr/bin/env python
# -*- coding: utf-8 -*-
from decimal import Decimal
import decimal
from flask import Blueprint, abort, request, jsonify
from flask_restful import reqparse, abort, Api, Resource
from parrot.orders.models import Orders, OrderItems
from parrot.common import utils, config 
from parrot import app, db 


parser = reqparse.RequestParser()
orders = Blueprint('orders', __name__, url_prefix="/api/v1")

class Order(Resource):
    def post(self):

        """ Create order """

        parser.add_argument('user_id', required=True)
        parser.add_argument('customer_name', type=str, required=True)
        parser.add_argument('order_amount', type=str, required=True)  
        args = parser.parse_args()

        order_amount = args['order_amount']
        user_id = args['user_id']
        customer_name = args['customer_name']

        order = Orders.create_order(user_id, customer_name, order_amount)

        return {'message': 'order created'}, 201
    
    def get(self, order_id):

        """ Get order detail """

        order_details = OrderItems.get_order(order_id)
        data = []
        for item in order_details:
            data.append({'product_name':item.product_name, 'price':str(item.unit_price), "amount":str(item.product_amount)})
        
        return {'products': data},200



class OrderItem(Resource):
    def post(self, order_id):

        """ add products to order"""

        parser.add_argument('product_name',type=str, required=True)
        parser.add_argument('unit_price', type=str, required=True)
        parser.add_argument('product_amount', type=int, required=True)  
        args = parser.parse_args()

        product_name = args['product_name']
        unit_price = args['unit_price']
        product_amount = args['product_amount']

        add_product = OrderItems.add_product(product_name, order_id, unit_price, product_amount)
      
        return {'message': 'added product'}, 201


api = Api(orders)
api.add_resource(Order, "/orders/","/orders/<order_id>/")
api.add_resource(OrderItem,"/orders/<order_id>/products/")


