# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 14:09:53 2021

This is a server 

@author: mateo
"""

from flask import Flask, jsonify, request, render_template

app = Flask(__name__)
stores = [
    {
         'name': 'My Store',
         'items': [
             {
                'name': 'My Item',
                'price': 39.99
             }
         ]
     }
]

@app.route('/')
def home():
    return render_template('index.html')

# From server perspective
# POST - used to receive data 
# GET - use to send data

# POST /store {name:}
@app.route('/store', methods =['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name': request_data['name'],
        'items': []
    }
    stores.append(new_store)
    return jsonify(new_store)

# GET /store/<string:name>
@app.route('/store/<string:name>') # 'http://127.0.0.1:5000/store/some_name'
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})
    
# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores})

# POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data =  request.get_json()    
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name': request_data['name'],
                'price': request_data['price']
            }
            store['items'].append(new_item) 
            return jsonify(new_item)
    return jsonify({'message': 'store not found'})

# GET /store/<string:name>/item
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run('127.0.0.1', 5000)
