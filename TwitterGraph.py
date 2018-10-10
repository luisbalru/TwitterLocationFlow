import json
import os

class TwitterGraph:
    """ Clase principal del proyecto que gestiona la estructura de datos de mi grafo.
        Basada en la representación de grafo dada en https://www.python-course.eu
        Añadidas algunas modificaciones
    """

    def __init__(self):
        """ Inicializa el objeto grafo """
        try: # Basado en el HitosIV.py de JJ/tests-python
            if os.path.exists('nodes.json'):
                path = 'nodes.json'
            elif os.path.exits('/data/nodes.json'):
                path = '/data/nodes.json'
            elif os.path.exists('./data/nodes.json'):
                path = './data/nodes.json'
            elif os.path.exists('../data/nodes.json'):
                path = '../data/nodes.json'
            else:
                raise IOError("No se encuentra 'nodes.json'")

            with open(path,"r") as data_file:
                self.__graph_dict = json.loads(data_file)[0]
        except IOError as fallo:
            print("Error {:s} leyendo nodes.json".format(fallo))

    def vertices(self):
        """ Devuelve los vértices del grafo """
        return list(self.__graph_dict.keys())

    def aristas(self):
        """ Devuelve las aristas del grafo """
        return self.__generate_edges()

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
        if edge:
            vertice2 = arista.pop()
        else:
            vertice2 = vertice1
        if vertice1 in self.__graph_dict:
            self.__graph_dict[vertice1].append(vertice2)
        else:
            self.__graph_dict[vertice1] = vertice2

    def __generar_vertices(self):
        """ Método estático que genera las aristas del grafo
            'graph'. Las aristas se representan como conjuntos
            con uno o dos vértices
        """
        aristas = []
        for vertice in self.__graph_dict:
            for neighbour in self.__graph_dict[vertice]
                if {vertice, neighbour} not in aristas:
                    aristas.append(({vertice,neighbour}))
        return aristas
