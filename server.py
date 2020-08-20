#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:01:21 2019

@author: r
"""
import sys
from flask import Flask, jsonify, abort, request
# from gevent import monkey, pywsgi
from flask_cors import CORS
import numpy as np 
import os 
from turbojpeg import TurboJPEG

class CFG(object):
    def __init__(self):
        self.port = int(sys.argv[1])


# monkey.patch_all()
app = Flask(__name__)
CORS(app,support_credentials=True)

cfg = CFG()
jpeg = TurboJPEG()

@app.route('/test/',methods=["POST"])
def test():
    data = request.data
    img = jpeg.decode(data)
    print(sys.getsizeof(data))
    print(sys.getsizeof(img))
    print(img.shape)
    return jsonify(1)


@app.route('/test_api/',methods=["GET"])
def test_api():
    return jsonify(1)



if __name__ == '__main__':
    # server = pywsgi.WSGIServer(('0.0.0.0',cfg.port),app)

    print("server configuration is done!")
    print('API is running!')
    print('LocalIP: {} , Port: {}'.format("localhost",cfg.port))
    # print('HostName: {} , LocalIP: {} , Port: {}'.format(,cfg.port))

    print()
    app.run(host='0.0.0.0', port=cfg.port)
    # server.serve_forever()


