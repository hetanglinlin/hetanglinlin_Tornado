import tornado.web
import tornado.ioloop

from user.views import RegisterHandler


def make_app():
    return tornado.web.Application(handlers=[
        (r'/register/', RegisterHandler)
    ],
        # 相对路径和绝对路径都可以
    template_path='templates',
    static_path='static'
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()


