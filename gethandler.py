import tornado.web
import Books
import json

class GetHandler(tornado.web.RequestHandler):
    def initialize(self,books):
        self.books = books

    def get(self):
       self.write(self.books.json_list())
       












