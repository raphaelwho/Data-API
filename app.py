from unittest import result
from flask import Flask, request, jsonify
from load_dat import load


app = Flask(__name__)

@app.route('/')
def hello():
	return "Server is working!"

# get the json data
@app.route('/get_data', methods = ['POST'])
def get_sentiment():
	file_url = request.form['file_url']
	file_stream = request.get(file_url, stream=True)
	tx = request.get_json(force = True)
	text = tx['Review']
	result = load(text)
	return jsonify(result = sent)



if __name__ == '__main__':
	app.run(host='0.0.0.0',port = 8080, debug = True, use_reloader = False)