# -*- coding: utf-8 -*-
import unittest, json, requests
from requests import *

# Completar
url = 'https://iv1819-twitterlocationflow.herokuapp.com'

class testAPI(unittest.TestCase):
	def test_root(self):
		response = requests.get(url)
		self.assertEqual(response.status_code,200, "Código correcto")
		self.assertEqual(response.json()['status'],'OK',"Estado correcto")

	def test_status(self):
		response = requests.get(url+'/status')
		self.assertEqual(response.status_code, 200, "Código correcto")
		self.assertEqual(response.json()['status'], 'OK', "Estado correcto")




		

if __name__ == '__main__':
	unittest.main()
