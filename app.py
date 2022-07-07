from flask import Flask, request, jsonify


app = Flask(__name__)

@app.route('/')
def hello():
	return "Server is working!"

# get the json data
@app.route('/get_sentiment', methods = ['POST'])
def get_sentiment():
	tx = request.get_json(force = True)
	text = tx['Review']
	return jsonify(result = sent)



if __name__ == '__main__':
	app.run(host='0.0.0.0',port = 8080, debug = True, use_reloader = False)