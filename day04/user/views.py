import tornado.web


class RegisterHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        self.render('register.html')