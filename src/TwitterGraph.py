# coding=utf-8
import json
import os
from gremlin_python.driver import client, serializer
import sys, traceback


class TwitterGraph:
    """ Clase principal del proyecto que gestiona la estructura de datos de mi grafo.
        Basada en la representación de grafo dada en https://www.python-course.eu
        Añadidas algunas modificaciones.
    """

    def __init__(self):
        """ Inicializa el objeto grafo """


    def vertices(client):
        """ Devuelve los vértices del grafo """
        query = "g.V().hasLabel('vertex')"
        callback = client.submitAsync(query)
        resultado = ""
        for result in callback.result():
            resultado = resultado + "\t{0}".format(str(result))
        return resultado

    def add_vertice(client, vertex):
        """
            Añade un vértice con id 'vertex' nuevo al grafo.
            El vértice debe ser un string
        """
        if (not type(vertex) is str):
            raise TypeError("El vértice debe ser un string")

        query = "g.addV('vertex').property('id','" + str + "').property('name','"+str+"')"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def add_arista(client, arista):
        """ arista es un conjunto, tupla o lista """
        arista = set(arista)
        vertice1 = arista.pop()
        if arista:
            vertice2 = arista.pop()
        else:
            vertice2 = vertice1

        query = "g.V('" + vertice1 + "').addE('knows').to(g.V('"+ vertice2 +"'))"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def elimina_conexion(client, vertice1, vertice2):
        """ Elimina la arista entre vertice1 y vertice2 """
        query = "g.V('" + vertice1 + "').outE('knows').where(inV().has('vertex','"+vertice2+"')).drop()"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def elimina_vertice(client, vertice):
        """ Elimina un vértice del grafo (y todas sus conexiones) """
        query = "g.V('"+vertice+"').drop()"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def cuenta_vertices(client):
        query = "g.V().count()"
        callback = client.submitAsync(query)
        if callback.result() is not None:
            return ("\t{0}".format(callback.result().one()))
        else:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))


    def find_path(client, start_vertex, end_vertex):
        query = "g.V('"+start_vertex+"').repeat(out()).util(has('id','"+end_vertex+"')).path().by('name')"
        callback = client.submitAsync(query)
        resultado = ""
        for result in callback.result():
            resultado = resultado + "\t{0}".format(str(result))
        return resultado
