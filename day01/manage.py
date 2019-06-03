import os

import tornado.web
import tornado.ioloop
from tornado.options import options, define, parse_command_line

from app.views import MyRequestHandler, MyResponseHandler, \
    ActionMethodHandler, Days1Handler, Days2Handler

define('port', default=8000, type=int)


def make_app():
    return tornado.web.Application(handlers=[
        (r'/req/', MyRequestHandler),
        (r'/res/', MyResponseHandler),
        (r'/action_method/', ActionMethodHandler),
        (r'/days1/(\d+)/(\d+)/(\d+)/', Days1Handler),
        # /<int:year>/<int:month>/<int:days>/
        (r'/days2/(?P<year>\d+)/(?P<month>\d+)/(?P<days>\d+)/', Days2Handler),
    ],
    # debug=True,
    cookie_secret='aosjduqeyrowej',
    )

if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
