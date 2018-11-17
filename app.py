
# -*- coding: utf-8 -*-
""" API REST for TwitterGraph """

import json
from flask import Flask, jsonify, request, make_response
from src.TwitterGraph import TwitterGraph


app = Flask(__name__)




@app.route("/", methods=['GET'])
def index():
    return jsonify(status='OK')

@app.route("/status", methods=['GET'])
def status():
    return jsonify(status='OK')

@app.route("/all", methods=['GET','POST'])
def all():
    return jsonify(status=TwitterGraph.grafo())

@app.route("/vertices", methods=['POST'])
def vertices():
    return jsonify(success=TwitterGraph.vertices())

@app.route("/aristas", methods=['POST'])
def aristas():
    return jsonify(success=TwitterGraph.aristas())

@app.route("/grado/<id>", methods=['POST'])
def grado_vertice(id):
    return jsonify(success=TwitterGraph.grado_vertice(str(id)))

@app.route("/vertices_aislados", methods=['POST'])
def vertices_aislados():
    return jsonify(success=TwitterGraph.vertices_aislados())

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
    app.run(host='0.0.0.0', port=80)
