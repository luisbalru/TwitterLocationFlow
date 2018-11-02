
# -*- coding: utf-8 -*-
""" API Rest for TwitterGraph """

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

@app.route("/all", methods=['POST'])
def all():
    "Devuelve el grafo completo"
    return jsonify(success=TwitterGraph.grafo())

@app.route("/vertices", methods=['POST'])
def vertices():
    """Devuelve todos los vértices"""
    return jsonify(success=TwitterGraph.vertices())

@app.route("/aristas", methods=['POST'])
def aristas():
    """Devuelve todas las aristas"""
    return jsonify(success=TwitterGraph.aristas())

@app.route("/grado/<id>", methods=['POST'])
@token_required
def grado_vertice(id):
    return jsonify(success=TwitterGraph.grado_vertice(str(id))

@app.route("/vertices_aislados", methods=['POST'])
def vertices_aislados():
    return jsonify(success=TwitterGraph.vertices_aislados())

@app.route("/vertices/add/<vertex>", methods=['POST'])
@token_required
def add_vertex(vertex):
    return jsonify(success=TwitterGraph.add_vertice(str(vertex)))

@app.route("/aristas/add/<edge>", methods=['POST'])
@token_required
def add_edge(edge):
    return jsonify(success=TwitterGraph.add_vertice(str(edge)))

@app.route("/vertices/remove/<vertex>", methods=['DELETE'])
@token_required
def remove_vertex(vertex):
    return jsonify(success=TwitterGraph.elimina_vertice(str(vertex)))

@app.route("/aristas/remove/<edge>", methods=['DELETE'])
@token_required
def remove_edge(edge):
    return jsonify(success=TwitterGraph.elimina_conexion(str(edge)))




if __name__ == "__main__":
    app.run()
