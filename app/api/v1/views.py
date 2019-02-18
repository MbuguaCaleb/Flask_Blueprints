import time
import datetime
from flask_restful import Resource
from flask import request,make_response,jsonify



blog_list =[]

class Blogs(Resource):
    
    def post(self):
        req=request.get_json()

        new={

            "id":len(blog_list)+1,
            "title":req['title'],
            "description":req['description'],
            "date":datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%M-%d %H:%M:%s')
        }
        
        blog_list.append(new)

        return make_response(jsonify({

            "msg":"Created",
            "blog_id":new['id']

        }),201)

    """retrieving all blogs"""

    def get(self):
        
        return make_response(jsonify(
            {
                "msg":"OK",
                "blogs":blog_list

            }),200)



class SingleBlog(Resource):
    """docstring for SingleBlog"""

    def get(self, id):
        """retrieving a single blog based on id"""
        for blog in blog_list:
            if blog['id'] == id:
                return make_response(jsonify({
                    "msg": "ok",
                    "blog": blog
                }), 200)
            
            return make_response(jsonify({
                "msg": "Not found"
            }), 404)

    def delete(self,id):

        global blog_list

        blog_list = [blog for blog in blog_list if blog['id'] != id ]

        return make_response(jsonify({
            "msg":"Blog with id {} deleted".format(id)        
        }
        ),200 )

    """updating a given blog by specifying the id"""   

    def put(self, id):
        for blog in blog_list:
            if blog['id'] == id:
                req = request.get_json()
                blog['title'] = req['title']
                blog['description'] = req['description']
                blog['updated'] = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
                return make_response(jsonify({
                    "msg": "ok",
                    "blog": blog
                }), 200)


            updated_blog = {
                "id": id,
                "title": req['title'],
                "description": req['description'],
                "updated": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
            }
            blog_list.append(updated_blog)

            return make_response(jsonify({
                "msg": "ok",
                "blog": blog
            }), 201)