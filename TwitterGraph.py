# coding=utf-8
import json
import os


class TwitterGraph:
    """ Clase principal del proyecto que gestiona la estructura de datos de mi grafo.
        Basada en la representación de grafo dada en https://www.python-course.eu
        Aniadidas algunas modificaciones
    """

    def __init__(self):
        """ Inicializa el objeto grafo """
        try: # Basado en el HitosIV.py de JJ/tests-python
            if os.path.isfile('nodes.json'):
                path = 'nodes.json'
            elif os.path.isfile('/data/nodes.json'):
                path = '/data/nodes.json'
            elif os.path.isfile('./data/nodes.json'):
                path = './data/nodes.json'
            elif os.path.isfile('../data/nodes.json'):
                path = '../data/nodes.json'
            else:
                raise IOError("No se encuentra 'nodes.json'")

            with open(path,"r") as data_file:
                self.__graph_dict = json.loads(data_file.read())
        except IOError as fallo:
            print("Error {:s} leyendo nodes.json".format(fallo))

    def vertices(self):
        """ Devuelve los vértices del grafo """
        return list(self.__graph_dict.keys())

    def aristas(self):
        """ Devuelve las aristas del grafo """
        return self.__generar_aristas()

    def add_vertice(self, vertex):
        """ Si el vértice 'vertex' no está en self.__graph_dict
            se introduce en el diccionario una nueva clave
            'vertex' con una lista vacía como valor.
            En otro caso, no se hace nada
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_arista(self, arista):
        """ arista es un conjunto, tupla o lista """
        arista = set(arista)
        vertice1 = arista.pop()
        if arista:
            vertice2 = arista.pop()
        else:
            vertice2 = vertice1
        if vertice1 in self.__graph_dict:
            self.__graph_dict[vertice1].append(vertice2)
        else:
            self.__graph_dict[vertice1] = vertice2

    def elimina_conexion(self, vertice1, vertice2):
        """ Elimina la arista entre vertice1 y vertice2 """
        aristas = self.__graph_dict[vertice1]
        if aristas:
            aristas.remove(vertice2)
            self.__graph_dict[vertice1] = aristas
        aristas = self.__graph_dict[vertice2]
        if aristas:
            aristas.remove(vertice1)
            self.__graph_dict[vertice2] = aristas

    def elimina_vertice(self, vertice):
        """ Elimina un vértice del grafo (y todas sus conexiones) """
        if vertice in self.__graph_dict:
            del self.__graph_dict[vertice]
            for vertex in self.__graph_dict:
                if vertice in self.__graph_dict[vertex]:
                    self.__graph_dict[vertex].remove(vertice)

    def __generar_aristas(self):
        """ Método estático que genera las aristas del grafo
            'graph'. Las aristas se representan como conjuntos
            con uno o dos vértices
        """
        aristas = []
        for vertice in self.__graph_dict:
            for neighbour in self.__graph_dict[vertice]:
                if {neighbour,vertice} not in aristas:
                    aristas.append(({neighbour,vertice}))
        return aristas

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generar_aristas():
            res += str(edge) + " "
        return res

    def vertices_aislados(self):
        """ devuelve una lista de vertices aislados. """
        graph = self.__graph_dict
        isolated = []
        for vert in graph:
            if not graph[vert]:
                isolated += [vert]
        return isolated

    def grado_vertice(self, vertice):
        """ El grado de un vértice es el número de
            aristas que conectan con él, es decir,
            el número de vértices adyacentes.
        """
        adj_vertices = self.__graph_dict[vertice]
        grado = len(adj_vertices)
        return grado

    def find_path(self, start_vertex, end_vertex, path=[]):
        """ Función recuersiva que encuentra un camino entre un vértice de
            partida y otro de llegada
        """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None


    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        """ Encuentra todos los caminos entre un vértices
            de partida y un vértice de llegada
        """
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex,path)
                for p in extended_paths:
                    paths.append(p)
        return paths
