# coding=utf-8

import unittest
import os,sys, traceback
from gremlin_python.driver import client, serializer
from .TwitterGraph import TwitterGraph

class TestTwitterGraph(unittest.TestCase):
    """ Clase creada para pasar tests a TwitterGraph """

    def setUp(self):
        self.__graph_dict = TwitterGraph()
        try:
            self.cliente = client.Client('wss://twitterlocationflow.gremlin.cosmosdb.azure.com:443/','g',
                                        username = os.environ['CLIENT_USERNAME'],
                                        password = os.environ['CLIENT_PASSWD'],
                                        message_serializer = serializer.GraphSONSerializersV2d0())
        except Exception as e:
            print('There was an exception: {0}'.format(e))
            traceback.print_exc(file=sys.stdout)
            sys.exit(1)


    def test_add_vertice_correctamente(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.add_vertice(self.cliente,1)

    def test_add_arista_correctamente(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.add_arista(self.cliente,[1,2])

    def test_remove_vertice(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.elimina_vertice(self.cliente,1)

    def test_remove_arista(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.elimina_conexion(self.cliente,1,2)

    def test_find_path(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.find_path(self.cliente,1,2)


if __name__ == '__main__':
    unittest.main()
