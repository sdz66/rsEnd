from flask import Flask, json, request, jsonify
from flask_cors import CORS
import pymysql
import cv2
import numpy as np
import os
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
CORS(app, resource={r'/*': {'origins': '*'}})

@app.route('/adduser', methods=['get', 'post'])
def adduser():
    username = request.form.get("username")
    password = request.form.get("password")
    print(username)
    print(password)
    return "已接收用户信息"

@app.route('/uploadbefore', methods=['get', 'post'])
def uploadbefore():
    username = request.form.get("username")
    img = request.files['file']
    picname=img.filename
    file = img.read()

    file = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)  # 解码为ndarray
    imgfile1_path = "./static/images/"+username+"/B/"
    if not os.path.exists(imgfile1_path):
        os.makedirs(imgfile1_path)
    img1_path = os.path.join(imgfile1_path, picname)
    cv2.imwrite(filename=img1_path, img=file)
    url = "http://127.0.0.1:5000/static/images/"+username+"/B/" + picname
    print(url)

    tempmap = {"url": url}
    return jsonify(tempmap)


@app.route('/uploadafter', methods=['get', 'post'])
def uploadafter():
    username = request.form.get("username")
    img = request.files['file']
    picname=img.filename
    file = img.read()

    file = cv2.imdecode(np.frombuffer(file, np.uint8), cv2.IMREAD_COLOR)  # 解码为ndarray
    imgfile1_path = "./static/images/"+username+"/A/"
    if not os.path.exists(imgfile1_path):
        os.makedirs(imgfile1_path)
    img1_path = os.path.join(imgfile1_path, picname)
    cv2.imwrite(filename=img1_path, img=file)
    url = "http://127.0.0.1:5000/static/images/"+username+"/A/" + picname
    print(url)

    tempmap = {"url": url}
    return jsonify(tempmap)



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)