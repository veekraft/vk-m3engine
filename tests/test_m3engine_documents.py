import os
import unittest
import m3engine_documents
import pytest

class MyTestCase(unittest.TestCase):

    def setUp(self):
        m3engine_documents.app.testing = True
        self.app = m3engine_documents.app.test_client()

    def tearDown(self):
		pass


    def test_add_document(self):
        response = self.app.post('/api/v1/document/add', data=dict(
			documentid='1',
			docname='Fido Rabies Certificate',
			imageurl='https://www.ecsisawesomeawesome.com/fido.png'
		), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Fido', response.data)

    def test_document_searchbyid(self):
        response = self.app.get('/api/v1/document/searchbyid', query_string=dict(
			handlerid='1'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'handlerid', response.data)

# Method	Equivalent to
# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)
# .assertIs(), .assertIsNone(), .assertIn(), and .assertIsInstance() all have opposite methods, named .assertIsNot(), and so forth.

if __name__ == '__main__':
    unittest.main()
	
