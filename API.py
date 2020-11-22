import os
import predict as pr
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/predict_function', methods = ['POST'])
def predict_function(data):
    result = pr.predict(data)
    return result

@app.route('/predict_api', methods = ['POST'])
def predict_api():
    data = request.get_json(force = True)
    result = predict_function(data)
    return jsonify(result)

if __name__ == "__main__":
    port = os.environ.get('PORT', '5000')
    app.run(host = '0.0.0.0', port = port, debug = True)
