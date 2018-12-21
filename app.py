
# -*- coding: utf-8 -*-
""" API REST for TwitterGraph """

import os,sys, traceback,json
from flask import Flask, jsonify, request, make_response
from gremlin_python.driver import client, serializer
from src.TwitterGraph import TwitterGraph

try:
	with open('data.txt') as json_file:
		data = json.load(json_file)
		url = data['C_URL']
		user = data['C_USER']
		passw = data['C_PASS']
		cliente = client.Client(url,'g',
                                        username = user,
                                        password = passw,
                                        message_serializer = serializer.GraphSONSerializersV2d0())
except Exception as e:
	print('There was an exception: {0}'.format(e))
	traceback.print_exc(file=sys.stdout)
	sys.exit(1)

app = Flask(__name__)




@app.route("/", methods=['GET'])
def index():
    return jsonify(status='OK')

@app.route("/status", methods=['GET'])
def status():
    return jsonify(status='OK')

@app.route("/vertices", methods=['POST'])
def vertices():
    return jsonify(success=TwitterGraph.vertices(cliente))

@app.route("/vertices/add/<vertex>", methods=['POST'])
def add_vertex(vertex):
    return jsonify(success=TwitterGraph.add_vertice(cliente,str(vertex)))

@app.route("/aristas/add/<edge>", methods=['POST'])
def add_edge(edge):
    return jsonify(success=TwitterGraph.add_vertice(cliente,str(edge)))

@app.route("/vertices/remove/<vertex>", methods=['DELETE'])
def remove_vertex(vertex):
    return jsonify(success=TwitterGraph.elimina_vertice(cliente,str(vertex)))

@app.route("/aristas/remove/<edge1>/<edge2>", methods=['DELETE'])
def remove_edge(edge):
    return jsonify(success=TwitterGraph.elimina_conexion(cliente,str(edge1),str(edge2)))

@app.route("/vertices/cuenta_vertices", methods=['POST'])
def count_vertex():
    return jsonify(success=TwitterGraph.cuenta_vertices(cliente))




if __name__ == "__main__":
    if 'PORT' in os.environ: p = os.environ['PORT']
    else: p =31416

    app.run(host='0.0.0.0', port=p)
