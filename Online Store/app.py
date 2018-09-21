
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

stores = [
	{
		'name': 'store1',
		'items' : [
			{
				'name': 'My item', 
				'price': 15.99
			}
		]
	}
]

@app.route('/')
def home():
	return render_template("index.html")

# POST - used to recieve data
# GET - used to send data back

# POST /store data:{name: }
@app.route('/store', methods = ['POST'])
def create_store():
	request_data = request.get_json()
	new_store = {
		'name' : request_data['name'], 
		'items': []
	}
	stores.append(new_store)
	return jsonify(new_store)

# GET /store/<string : name>
@app.route('/store/<string:name>', methods = ['GET'])
def get_store(name):
	# iterate over the stores and return store information
	for store in stores:
		if store['name'] == name:
			return jsonify(store)

	return jsonify({'message': 'store does not exist'})


# GET /store
@app.route('/store', methods=['GET'])
def get_stores():
	return jsonify({'stores' : stores})


# POST /store/<string:name>/item {name : , price : }
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
	request_data = request.get_json()

	for store in stores:
		if store['name'] == name:
			new_item = {
				'name' : request_data['name'], 
				'price': request_data['price']
			}
			store['items'].append(new_item)
			return jsonify(new_item)

	return jsonify({'message': 'Store not found'})


# GET /store/<string:name>/item
@app.route('/store/<string:name>/item', methods = ['GET'])
def get_item_in_store(name):
	items = []
	found = False
	for store in stores:
		if store['name'] == name:
			found = True
			return jsonify({'items' : store['items']})

	if not found:
		return jsonify({'message':'store does not exist'})


app.run(port=5000)
