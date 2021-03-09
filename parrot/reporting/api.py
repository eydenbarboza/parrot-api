#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint
from flask_restful import reqparse, abort, Api, Resource
from parrot.orders.models import Orders, OrderItems
from parrot.common import utils, config 
from parrot import app, db 

parser = reqparse.RequestParser()
reporting = Blueprint('reporting', __name__, url_prefix="/api/v1")

class ProductReport(Resource):

    def get(self):

        """ Get product report """

        parser.add_argument('start_date', required=True)
        parser.add_argument('end_date', required=True)
        args = parser.parse_args()

        start_date = args['start_date']
        end_date = args['end_date']

        products_report = OrderItems.products_report(start_date,end_date)

        data = []
        for item in products_report:
            data.append({'product_name':item.product_name, 'count':str(item.products_amount)})

        return {'report':data}, 200

api = Api(reporting)
api.add_resource(ProductReport, "/reporting/products/")


