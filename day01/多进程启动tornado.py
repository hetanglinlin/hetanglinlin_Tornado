"""
多进程tornado
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver
from tornado.options import options, define, parse_command_line

define('port', default=8080, type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('多进程启动tornado')


def make_app():
    return tornado.web.Application(handlers=[
        (r'/', IndexHandler),
    ])

if __name__ == '__main__':
    parse_command_line()
    app = make_app()
    # 单进程配置
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    # 多进程配置
    server = tornado.httpserver.HTTPServer(app)
    server.bind(options.port)
    # server.start(num_processes), num_processes表示启动的进程数量
    # 如果不写server.start()表示启动一个进程（单进程）
    # 如果写server.start()num_processes默认为1，表示启动一个进程

    # 如果server.start(0)表示创建的进程数会根据cpu的核数来决定
    # windows系统中由于底层os没有fork会报错，不使用
    # mac、ubuntu中也不常用这种多进程方式，由于不清楚是哪一个进程响应了请求
    server.start(1)
    tornado.ioloop.IOLoop.current().start()



