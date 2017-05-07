import tensorflow as tf, sys
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin
import base64
import numpy as np

# webapp
app = Flask(__name__)
#image_path = sys.argv[1]


@app.route('/api/predict', methods=['POST'])
@cross_origin()
def predict():
    data = request.values['imageBase64']
    output_string=["bike","car","men"]
    data = np.load('/home/nikitha/Desktop/labels_xy_new.npy')
    net_out=data[np.random.randint(300)]
    print("bounding box co-ordinates",net_out)



    return jsonify(results=10)


@app.route('/')
def main():
    return render_template('index.html')