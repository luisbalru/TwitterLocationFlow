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

    def vertices(self,client):
        """ Devuelve los vértices del grafo """
        query = "g.V().hasLabel('vertex')"
        callback = client.submitAsync(query)
        resultado = ""
        for result in callback.result():
            resultado = resultado + "\t{0}".format(str(result))
        return resultado

    def add_vertice(self,client, vertex):
        """
            Añade un vértice con id 'vertex' nuevo al grafo.
            El vértice debe ser un string
        """
        if (not type(vertex) is str):
            raise TypeError("El vértice debe ser un string")

        query = "g.addV('vertex').property('id','" + vertex + "').property('name','"+vertex+"')"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def add_arista(self,client, arista):
        """ arista es un conjunto, tupla o lista """
        arista = set(arista)
        vertice1 = arista.pop()
        if arista:
            vertice2 = arista.pop()
        else:
            vertice2 = vertice1
        if(not type(vertice1) is str):
            raise TypeError("El vértice debe ser un string")

        query = "g.V('" + str(vertice1) + "').addE('knows').to(g.V('"+ str(vertice2) +"'))"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def elimina_conexion(self,client, vertice1, vertice2):
        """ Elimina la arista entre vertice1 y vertice2 """
        if(not type(vertice1) is str or not type(vertice2) is str):
            raise TypeError("Los vértices deben ser strings")
        query = "g.V('" + str(vertice1) + "').outE('knows').where(inV().has('vertex','"+str(vertice2)+"')).drop()"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def elimina_vertice(self,client, vertice):
        """ Elimina un vértice del grafo (y todas sus conexiones) """
        if(not type(vertice) is str):
            raise TypeError("El vértice debe ser string")
        query = "g.V('"+str(vertice)+"').drop()"
        callback = client.submitAsync(query)
        if callback.result() is None:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))

    def cuenta_vertices(self,client):
        query = "g.V().count()"
        callback = client.submitAsync(query)
        if callback.result() is not None:
            return ("\t{0}".format(callback.result().one()))
        else:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))


    def find_path(self,client, start_vertex, end_vertex):
        if(not type(start_vertex) is str):
            raise TypeError("El vértice debe ser string")
        query = "g.V('"+str(start_vertex)+"').repeat(out()).until(has('id','"+str(end_vertex)+"')).path().by('name')"
        callback = client.submitAsync(query)
        resultado = ""
        if callback.result() is not None:
            for result in callback.result():
                resultado = resultado + "\t{0}".format(str(result))
            return resultado
        else:
            raise ValueError("Algo fue mal con esta query:{0}".format(query))
