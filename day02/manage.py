import os

import tornado.web
import tornado.ioloop
from tornado.options import options, define, parse_command_line
from tornado_jinja2 import Jinja2Loader

from app.views import IndexHandler, InitDBHandler, StuHandler

define('port', default=8000, type=int)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
jinja2loader = Jinja2Loader('templates')

def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler),
        (r'/initdb/', InitDBHandler),
        (r'/stu/', StuHandler),
    ],
    static_path=os.path.join(BASE_DIR, 'static'),
    template_path=os.path.join(BASE_DIR, 'templates'),
    template_loader=jinja2loader
    )

if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(port=options.port, address='localhost')
    tornado.ioloop.IOLoop.current().start()



