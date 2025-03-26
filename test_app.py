from app import app
import unittest

class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        
    def test_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_search(self):
        response = self.client.post('/', data={
            'search_expr': 'cancer AND recruiting',
            'title': 'Test Map',
            'max_studies': '10'
        })
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
