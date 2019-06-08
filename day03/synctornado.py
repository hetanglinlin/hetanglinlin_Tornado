import tornado.web
import tornado.ioloop
import tornado.httpclient


class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # https://www.baidu.com/s?wd=python
        wd = self.get_argument('wd')
        # 请求百度地址
        url = 'https://www.baidu.com/s?wd={}'.format(wd)
        # 获取客户端，fetch(url)获取源码
        client = tornado.httpclient.HTTPClient()
        print('同步测试')
        response = client.fetch(url)
        print(response)
        self.write('index')

def make_app():
    return tornado.web.Application(handlers=[
        (r'/index/', IndexHandler)
    ])

if __name__ == '__main__':
    app = make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()



