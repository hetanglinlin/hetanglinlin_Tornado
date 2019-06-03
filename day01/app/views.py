from datetime import datetime, timedelta

import tornado.web

# 请求
# 在django中: request.GET.get()   request.POST.get()
# 在flask中: request.args.get()/getlist()
#           request.form.get()/getlist()
# 在tornado中: request.get_argument()/get_arguments()
#    get                     request.get_query_argument()
#    post/put/patch/delete   request.get_body_argument()


class MyRequestHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        # 获取参数
        # self.request.argument(key)  self.request.query_argument(key)
        # 获取key为name对应的一个value值
        self.get_argument('name')
        # 获取key为name对应的所有value值，并组装成列表
        self.get_arguments('name')

        self.get_query_argument('name')
        self.get_query_arguments('name')

        self.write('请求')

    def post(self, *args, **kwargs):
        # 不管get还是post，都可以从get_argument中取值
        self.get_argument('username')
        self.get_arguments('username')

        # get_body_argument这种方式取值不能获取get方式传参，
        # 只能获取post取值？
        self.get_body_argument('username')
        self.get_body_arguments('username')

        # 方式
        self.request.method
        # 上传文件
        self.request.files
        # 请求路径
        self.request.path
        # cookie
        self.request.cookies
        # 远程地址
        self.request.remote_ip

        self.write('post请求')

    def patch(self, *args, **kwargs):
        # 取值方式和post一致

        self.write('patch请求')


class MyResponseHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        # 在django中，return HttpResponse() / redirect/ HttpResponseRedirect
        # 在flask中，return make_response('响应内容', 200) / return '响应内容'

        # 设置状态码
        self.set_status(200)
        # 重定向 302
        # self.redirect('/req/')
        # 设置cookie的内容
        # self.set_cookie('token', '1234567890', expires_days=1)
        # self.set_cookie('token', '1234567890', expires=datetime.now() + timedelta(days=1))
        # self.clear_cookie('token')
        # self.clear_all_cookies()

        # 设置加密cookie的内容, 超时时间默认30天
        # self.set_secure_cookie('token', 'qwertyuiop')

        # 响应json数据
        self.write({'code':200, 'msg': '请求成功'})

        # 模板
        self.render('login.html')

        self.write('响应')


class ActionMethodHandler(tornado.web.RequestHandler):
    # HTTP行为方法
    def get(self, *args, **kwargs):
        self.write('只用于获取')

    def post(self, *args, **kwargs):
        self.write('只用于创建')

    def patch(self, *args, **kwargs):
        self.write('只用于修改部分字段')

    def put(self, *args, **kwargs):
        self.write('只用于修改全部字段')

    def delete(self, *args, **kwargs):
        self.write('只用于删除')


class Days1Handler(tornado.web.RequestHandler):

    # def get(self, *args, **kwargs):
    #     print(args)
    #     self.write('多参数路由')

    def get(self, year, month, days):
        self.write('{}年{}月{}日'.format(year, month, days))


class Days2Handler(tornado.web.RequestHandler):

    def get(self, days, month, year):
        self.write('{}年{}月{}日'.format(year, month, days))






