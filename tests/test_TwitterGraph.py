# coding=utf-8

import unittest
from gremlin_python.driver import client, serializer
from src.TwitterGraph import TwitterGraph

class TestTwitterGraph(unittest.TestCase):
    """ Clase creada para pasar tests a TwitterGraph """

    def setUp(self):
        self.__graph_dict = TwitterGraph()
        try:
            client = client.Client('wss://twitterlocationflow.gremlin.cosmosdb.azure.com:443/','g',username="/dbs/db-iv-ugr/colls/grafo-iv-ugr",password="2r4SoDdlxiXaqxsLgb6yohACz6tVWuv5dgbQ3dqQ5rvvZInn3cUW7pNFHg8DeW5gxSj3xi1KSG3X95qaqBNZjA")
        except TypeError:
            print("Hubo un error!")
            
    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.__graph_dict,TwitterGraph, "Objeto creado correctamente")

    def test_add_vertice_correctamente(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.add_vertice(client,1)

    def test_add_arista_correctamente(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.add_arista(client,[1,2])

    def test_remove_vertice(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.elimina_vertice(client,1)

    def test_remove_arista(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.elimina_conexion(client,1,2)

    def test_find_path(self):
        self.__graph_dict.add_vertice(client,'n')
        self.__graph_dict.add_vertice(client,'m')
        self.__graph_dict.add_vertice(client,'t')
        self.__graph_dict.add_arista(client,['n','m'])
        self.__graph_dict.add_arista(client,['m','t'])
        self.assertEqual(self.__graph_dict.find_path(client,'n','t'), ['n', 'm', 't'], "Camino correcto")


if __name__ == '__main__':
    unittest.main()
