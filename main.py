from src.functions import filter_adaptative_gaussian, filter_global_thresholding, filter_otsu
from flask import Flask, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello, World!'

@app.route('/filters/otsu', methods=['POST'])
def filterOtsu():
    data = json.loads(request.data)
    path = data['path']
    out_name = data['out']
    filter_otsu(path, out_name)
    return "OK - 200"

@app.route('/filters/global', methods=['POST'])
def filterGlobal():
    data = json.loads(request.data)
    path = data['path']
    out_name = data['out']
    value = data['th_value']
    filter_global_thresholding(path, value, out_name)
    return "OK - 200"

@app.route('/filters/adaptative-gaussian', methods=['POST'])
def filterAdaptativeGaussian():
    data = json.loads(request.data)
    path = data['path']
    out_name = data['out']
    filter_adaptative_gaussian(path, out_name)
    return "OK - 200"

app.run(debug=True)