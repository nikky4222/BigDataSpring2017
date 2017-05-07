import tensorflow as tf, sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import base64

# webapp
app = Flask(__name__)
#image_path = sys.argv[1]


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    data = request.values['imageBase64']
    output_string=["bike","car","men"]
    print (data)
    return jsonify(results=[output_string[int(data)]])


@app.route('/')
def main():
    return render_template('index1.html')