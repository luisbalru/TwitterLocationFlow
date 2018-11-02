# coding=utf-8

import unittest

from TwitterGraph import TwitterGraph

class TestTwitterGraph(unittest.TestCase):
    """ Clase creada para pasar tests a TwitterGraph """

    def setUp(self):
        self.__graph_dict = TwitterGraph()

    def test_should_initialize_object_OK(self):
        self.assertIsInstance(self.__graph_dict,TwitterGraph, "Objeto creado correctamente")

    def test_should_have_graph_stored_correctly( self):
        self.assertIsInstance( self.__graph_dict.grafo(), dict, "El objeto graph_dict contiene un diccionario")

    def test_add_vertice_correctamente(self):
        with self.assertRaises(TypeError):
            self.__graph_dict.add_vertice(1)

    def test_add_arista_correctamente(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.add_arista([1,2])

    def test_remove_vertice(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.elimina_vertice(1)

    def test_remove_arista(self):
        with self.assertRaises(ValueError):
            self.__graph_dict.elimina_conexion(1,2)

    def test_grado_vertice(self):
        with self.assertRaises(KeyError):
            self.__graph_dict.grado_vertice(1)

    def test_find_path(self):
        self.__graph_dict.add_vertice('n')
        self.__graph_dict.add_vertice('m')
        self.__graph_dict.add_vertice('t')
        self.__graph_dict.add_arista(['n','m'])
        self.__graph_dict.add_arista(['m','t'])
        self.assertEqual(self.__graph_dict.find_path('n','t'), ['n', 'm', 't'], "Camino correcto")

    def test_find_all_paths(self):
        self.__graph_dict.add_vertice('n')
        self.__graph_dict.add_vertice('m')
        self.__graph_dict.add_vertice('aux')
        self.__graph_dict.add_vertice('t')
        self.__graph_dict.add_arista(['n','m'])
        self.__graph_dict.add_arista(['n','aux'])
        self.__graph_dict.add_arista(['aux','t'])
        self.__graph_dict.add_arista(['m','t'])
        self.assertEqual(self.__graph_dict.find_all_paths('n','t'),[['n', 'm', 't'], ['n', 'aux', 't']], "Caminos correctos")

    def test_isolated_vertex(self):
        self.__graph_dict.add_vertice('n')
        self.assertEqual(self.__graph_dict.vertices_aislados(),['n'], "El único vértice aislado es 'n'")
