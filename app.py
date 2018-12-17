
# -*- coding: utf-8 -*-
""" API REST for TwitterGraph """

import json, os
from flask import Flask, jsonify, request, make_response
from src.TwitterGraph import TwitterGraph


app = Flask(__name__)




@app.route("/", methods=['GET'])
def index():
    return jsonify(status='OK')

@app.route("/status", methods=['GET'])
def status():
    return jsonify(status='OK')

@app.route("/vertices", methods=['POST'])
def vertices():
    return jsonify(success=TwitterGraph.vertices())

@app.route("/vertices/add/<vertex>", methods=['POST'])
def add_vertex(vertex):
    return jsonify(success=TwitterGraph.add_vertice(str(vertex)))

@app.route("/aristas/add/<edge>", methods=['POST'])
def add_edge(edge):
    return jsonify(success=TwitterGraph.add_vertice(str(edge)))

@app.route("/vertices/remove/<vertex>", methods=['DELETE'])
def remove_vertex(vertex):
    return jsonify(success=TwitterGraph.elimina_vertice(str(vertex)))

@app.route("/aristas/remove/<edge>", methods=['DELETE'])
def remove_edge(edge):
    return jsonify(success=TwitterGraph.elimina_conexion(str(edge)))




if __name__ == "__main__":
    if 'PORT' in os.environ: p = os.environ['PORT']
    else: p =31416

    app.run(host='0.0.0.0', port=p)
