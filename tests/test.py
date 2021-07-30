import unittest

import requests


class TestCase(unittest.TestCase):

  def testMaintenancePage(self):
    response = requests.get('http://nginx/maintenance')

    self.assertEqual(503, response.status_code)

  def testRootPage(self):
    response = requests.get('http://nginx/')

    self.assertEqual(503, response.status_code)

  def testcomponents(self):
    response = requests.get('http://nginx/maintenance/Gotham-Bold.eot')
    self.assertEqual(200, response.status_code)

    response = requests.get('http://nginx/maintenance/maintenance.css')
    self.assertEqual(200, response.status_code)
    
    response = requests.get('http://nginx/maintenance/Gotham-Bold.svg')
    self.assertEqual(200, response.status_code)

    response = requests.get('http://nginx/maintenance/Gotham-Bold.ttf')
    self.assertEqual(200, response.status_code)

    response = requests.get('http://nginx/maintenance/normalize.css')
    self.assertEqual(200, response.status_code)




if __name__ == '__main__':
    unittest.main()