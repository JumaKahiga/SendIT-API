from flask import request
from flask_restful  import Resource


# Order statuses
canceled = 'Canceled'
delivered = 'Delivered'

# Dummy orders
orders = {
    321: ['532', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    453: ['352', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    133: ['254', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    301: ['686', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    353: ['350', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    633: ['345', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    365: ['140', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    495: ['675', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    127: ['109', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    249: ['140', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    132: ['619', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    808: ['805', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    809: ['532', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    810: ['352', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    811: ['254', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    812: ['686', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    813: ['350', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    814: ['345', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    815: ['140', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    816: ['675', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    817: ['109', '5 6535 453', '8 5465 742', 6, 'Canceled'],
    818: ['140', '4 5345 343', '4 5343 343', 5, 'In-transit'],
    819: ['619', '4 5435 324', '6 5356 353', 3, 'Delivered'],
    820: ['805', '5 6535 453', '8 5465 742', 6, 'Canceled']
}


class Parcels(Resource):
    def __init__(self):
        self.order_no = 100

    def get(self):
        return orders
    
    def post(self):
        data = request.get_json()
        data_list = data['order']
        orders[self.order_no] = data_list
        self.order_no = self.order_no + 1
        return {'messsage': 'Order created'}, 201


class Parcel(Resource):
    def get(self, id):
        try:
            int_id = int(id)
        except:
            return {'message': 'Wrong id format'}, 400

        if int_id in orders.keys():
            return {'order': {str(id): orders[int_id]}}
        else: 
            return {'message': 'No Parcel delivery order with that id'}, 400
        
    
    def put(self, id):
        try:
            int_id = int(id)
        except:
            return {'message': 'Wrong id format'}, 400

        if int_id in orders.keys():
            orders[int_id][4] = delivered
            return {'message': 'Status changed'} 
        else:       
            return {'message': 'No Parcel delivery order with that id'}, 400


class UserParcels(Resource):
    def get(self, id):
        order_list = {}
        str_id = str(id)
        for key, value in orders.items():
            if str_id == value[0]:
                order_list[key] = value
        if not  order_list:
            return {'message': 'No orders by that user'}, 400
        return {'orders': order_list}

            


class CancelOrder(Resource):
    def put(self, id):
        try:
            int_id = int(id)
        except:
            return {'message': 'Wrong id format'}, 400

        if int_id in orders.keys():
            orders[int_id][4] = canceled
            return {'message': 'Order canceled'} 
        else:       
            return {'message': 'No Parcel delivery order with that id'}, 400





