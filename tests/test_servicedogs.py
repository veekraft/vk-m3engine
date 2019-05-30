import os
import unittest
import m3engine_dog
import pytest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        m3engine_dog.app.testing = True
        self.app = m3engine_dog.app.test_client()

    def tearDown(self):
		pass
    #sample get with no parameters - testing for text in a HTML page
    #def test_dogview(self):
    #    response = self.app.get('/', follow_redirects=True)
    #    self.assertEqual(response.status_code, 200)
    #    self.assertIn(b'Dell Technologies', response.data)
        
    #Sample get with parameters
    def test_dogview(self):
        parameters = {'userid': '1234','sd_regid': 'abcd'}
        response = self.app.get('/api/v1/dog/view', follow_redirects=True, query_string=parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'fido', response.data)

    def test_dogadd(self):
        response = self.app.post('/api/v1/dog/add', data=dict(userid='1234',data='Fido'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SUCCESS', response.data)

    def test_dogdelete(self):
        parameters = {'userid': '1234','sd_regid': 'abcd'}
        response = self.app.delete('/api/v1/dog/delete', data=parameters)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SUCCESS', response.data)

    def test_dogupdate(self):
        response = self.app.put('/api/v1/dog/update', data=dict(userid='1234',sd_regid='abcd', data='udpdated data'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'SUCCESS', response.data)
