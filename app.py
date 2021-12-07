from flask import Flask, render_template, jsonify, request
import datetime
import os
from vending import VendingMachine

app = Flask(__name__, static_folder='./static')

items = {'apple': 1.99, 'banana': 1.99, 'lettuce': 3.99, 'cheese': 2.99}
current_inventory = {'apple': 2.99, 'banana': 1.99}
json_inv = {'items': [{'name': n, "price": current_inventory[n]} for n in current_inventory.keys()]}

class Item:

	def __init__(self, name, price):
		self.id    = 0
		self.name  = name
		self.price = price

	def set_id(self, id):
		self.id = id

	def to_json(self):
		return {"id": self.id, "name": self.name, "price": self.price}

	def __str__(self):
		return f"{self.name.capitalize()} <{self.id}>: $ {self.price}"

class Inventory:

	def __init__(self, inventory):
		self.current_inv = {n: [] for n in inventory.keys()}
		self.id_ctr      = 0

	def add_item(self, item):
		item.set_id(self.id_ctr)
		self.current_inv[item.name].append(item)
		self.id_ctr += 1
		return {'msg': f"Adding {item} to Inventory."}

	def remove_item(self, item):
		removed = self.current_inv[item] = []
		return {'msg': f"Removing {item} from Inventory."}

	def remove_all(self): 
		for key in self.current_inv.keys():
			self.current_inv[key] = []

	def change_quantity(self, item_name, quantity):
		if item_name in self.current_inv.keys():
			item = self.current_inv[item_name][0]
			self.current_inv[item_name] = []
			for i in range(quantity):
				new_item = Item(item.name, item.price)
				self.add_item(new_item)

	def save(self, name):
		data = {n: (len(self.current_inv[n]), self.current_inv[n][0].price) for n in self.current_inv.keys() if len(self.current_inv[n]) > 0}
		tmp = f"{name}\n"
		grand_total = 0
		for key in data.keys():
			quantity, price = data[key]
			tmp += f"\t{quantity} {key} @ {price} per item\n"
			grand_total += quantity * price

		tmp += f"\tGRAND TOTAL: {grand_total}\n"
		return tmp

	def get_all_items(self):
		to_print = {n: [i.to_json() for i in self.current_inv[n]] for n in self.current_inv.keys()}
		return jsonify(to_print)

inventory = Inventory(current_inventory)
try: 
	vending   = VendingMachine()
except Exception:
	pass
	# vending.reset()

@app.route('/', methods=["GET"])
def index():
	return render_template('home.html')

@app.route('/add/items', methods=["POST"])
def get_items():
	request_data = request.get_json(force=True)
	name = request_data["name"]
	price = request_data["price"]
	quantity = request_data["quantity"]
	for i in range(quantity):
		item = Item(name, price)
		inventory.add_item(item)
	return jsonify({"Status": 200})

@app.route('/remove/item', methods=["POST"])
def remove_item():
	request_data = request.get_json(force=True)
	name = request_data["name"]
	inventory.remove_item(name)
	return jsonify({"Status": 200})

@app.route('/update/item', methods=["POST"])
def update_item():
	request_data = request.get_json(force=True)
	name = request_data["name"]
	quantity = request_data["quantity"]
	inventory.change_quantity(name, quantity)
	return jsonify({"Status": 200})

@app.route('/remove/all', methods=["POST"])
def remove_all():
	inventory.remove_all()
	return jsonify({"Status": 200})

@app.route('/checkout', methods=["GET"])
def checkout():
	return render_template('checkout.html')

@app.route('/save', methods=["POST"])
def save_and_run():
	request_data = request.get_json(force=True)
	user_name    = request_data['name']
	with open('log', 'a') as f: 
		f.write(inventory.save(user_name))

	data = [(n, len(inventory.current_inv[n])) for n in inventory.current_inv.keys()]

	curr_x = 0
	for name, quantity in data:
		if quantity > 0:
			if name == 'banana':
				vending.get_item(name, 6250, 0)
				curr_x = 6250
			else:
				if curr_x == 6250:
					vending.get_item(name, -6250, 0)
				else: 
					vending.get_item(name, 0, 0)
	return jsonify({'Status': 200})

	# TODO: RUN THE VENDING MACHINE AND LOCATE THE ITEMS AND DELIVER! 

@app.route('/shopping_cart', methods=["GET"])
def shopping_cart():
	return render_template('shopping_cart.html')

@app.route('/get/inventory', methods=["GET"])
def get_inventory():
	return jsonify(json_inv)

@app.route('/get/items', methods=["GET"])
def get_inventory_items():
	return inventory.get_all_items()

@app.route('/vend/all', methods=["GET"])
def vend_items():
	raise NotImplementedError