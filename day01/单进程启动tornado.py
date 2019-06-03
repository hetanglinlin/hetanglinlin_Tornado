"""
tornado的最小应用文件
"""
import sys

import tornado.web
import tornado.ioloop
from tornado.options import options, define, parse_command_line

# 定义默认port参数
define('port', default=8001, type=int)


class IndexHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # 用于接收GET请求
        self.write('first tornado')


def make_app():
    # 返回Application对象，初始化handlers参数
    # handlers参数定义的就是路由配置(类似Django中的urls.py文件的功能)
    return tornado.web.Application(handlers=[
        (r'/', IndexHandler),
    ])


if __name__ == '__main__':
    # 解析命令行中的参数
    parse_command_line()
    # 获取应用对象
    app = make_app()
    # 监听端口
    # 注: 启动时，可通过127.0.0.1:8000访问地址，或者可通过内网IP地址:8000访问地址
    # 类似django中python manage.py runserver 0.0.0.0:8000
    # 类似flask中python manage.py runserver -h 0.0.0.0 -p 8000

    # 1. 接收命令行中自定义传入的参数，参数为端口
    print(sys.argv)
    # 2. 使用tornado自带模块进行启动命令行参数的获取
    app.listen(options.port)
    # 事件循环ioloop监听请求(启动)
    tornado.ioloop.IOLoop.current().start()
