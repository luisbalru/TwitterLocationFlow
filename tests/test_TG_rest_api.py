# -*- coding: utf-8 -*-
import unittest, json, requests
from requests import *

# Completar
url = 'https://'

assert context

class testAPI(unittest.TestCase):
	def test_root(self):
		response = requests.get(url)
		self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
        	self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

	def test_status(self):
		response = requests.get(url + '/status')
        	self.assertEqual(response.status_code, 200, "Devuelve codigo correcto.")
		self.assertEqual(response.json()['status'], 'OK', "Devuelve estado correcto.")

	