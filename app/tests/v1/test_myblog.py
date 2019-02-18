"""This is the main/default python testing library"""
"""importing the instance of our app since we want to test the app"""
import json
import unittest
from app.run import app


"""TestMyBlogg-OUR TEST CLASS -INHERIT Unittest.test case"""
class TestMyBlogApp(unittest.TestCase):
    """docstring for TestMyBlogAPP"""
    """setup method is used to construct all out tests"""
    """Test client is basically meant to run the app and execute all its routes then compare the output with the assert"""

    def setUp(self):
        self.app=app
        self.client=self.app.test_client()
        self.data ={
            "title":"Caleb is a good programmer",
            "description":"He is currently good at Python and aspiring to be great at JS"

        }
        
        self.da ={
            "title":"UPDATED:Caleb is a good programmer",
            "description":"UPDATED:He is currently good at Python and aspiring to be great at JS"
        }


    def post(self, path='/blog', data={}):
        if not data:
            data = self.data

        resp = self.client.post(path='/blog', data=json.dumps(self.data), content_type='application/json')
        return resp

    def test_posting_a_blog(self):
         #resp=self.client.post(path='/blog',data=json.dumps(self.data), content_type='application/json')
        
        resp = self.post()
        self.assertEqual(resp.status_code, 201)
        self.assertTrue(resp.json['blog_id'])
        self.assertEqual(resp.json['msg'], 'Created')

    def test_getting_all_blogs(self):
        resp = self.client.get(path='/blog', content_type='application/json')
        self.assertEqual(resp.status_code, 200)

    def test_getting_a_single_blog(self):
        post = self.post()
        int_id = int(post.json['blog_id'])
        path = '/blog/1'
        response = self.client.get(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_editing_a_blog(self):
        post = self.client.post(path='/blog', data=json.dumps(self.data), content_type='application/json')
        int_id = int(post.json['blog_id'])
        path = '/blog/{}'.format(int_id)
        response = self.client.put(path, data=json.dumps(self.da), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_deleting_a_blog(self):
        post = self.client.post(path='/blog', data=json.dumps(self.data), content_type='application/json')
        int_id = int(post.json['blog_id'])
        path = '/blog/{}'.format(int_id)
        response = self.client.delete(path, content_type='application/json')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
