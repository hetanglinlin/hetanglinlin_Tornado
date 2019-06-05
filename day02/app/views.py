import tornado.web

from app.models import init_db, Student
from utils.settings import session


class IndexHandler(tornado.web.RequestHandler):

    # http行为方法
    def get(self, *args, **kwargs):

        # self.write('index')
        item1 = ['Python', 'Vue', 'Flask']

        self.render('index.html', item1=item1)


class InitDBHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):
        init_db()
        self.write('初始化表成功')


class StuHandler(tornado.web.RequestHandler):

    def get(self, *args, **kwargs):

        stus = session.query(Student).filter_by(s_name='木下').all()
        print(stus)
        stus = session.query(Student).filter(Student.s_name=='木下').all()
        print(stus)
        # order_by,limit, contains, in_, notin_,count, and_,not_,or_
        self.write('查询数据成功')

    def post(self, *args, **kwargs):
        # flask中db.session.add()/add_all()
        # stu = Student()
        # stu.s_name = '木下'
        # session.add(stu)
        # session.commit()

        names = ['小明', '小童', '大雄', '哥斯拉2', '皮卡丘']
        stus = []
        for name in names:
            stu = Student()
            stu.s_name = name
            stus.append(stu)
        session.add_all(stus)
        session.commit()
        self.write('创建数据成功')

    def patch(self, *args, **kwargs):
        # Student.query.filter()
        stu = session.query(Student).filter(Student.s_name == '小明').first()
        print(stu)
        stu.s_name = '新垣结衣'
        session.add(stu)  # 可不写
        session.commit()
        self.write('修改数据成功')

    def delete(self, *args, **kwargs):
        stu = session.query(Student).get(4)
        print(stu)
        session.delete(stu)
        session.commit()
        self.write('删除数据成功')


