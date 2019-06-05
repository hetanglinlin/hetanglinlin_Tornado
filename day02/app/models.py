from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean, \
    DateTime, Text, Date
from sqlalchemy.orm import relationship

from utils.settings import Base


def init_db():
    # 将模型映射成表
    Base.metadata.create_all()


def drop_db():
    # 删除模型映射的表
    Base.metadata.drop_all()


class Student(Base):
    # 自增的主键id值
    id = Column(Integer, primary_key=True, autoincrement=True)
    # 定义唯一且不能为空且长度不超过10的s_name字段
    s_name = Column(String(10), unique=True, nullable=False)
    # 创建时间，类似django中auto_now_add
    create_time = Column(DateTime, default=datetime.now)
    # 修改时间, 类似django中auto_now
    operate_time = Column(DateTime, default=datetime.now,
                          onupdate=datetime.now)

    __tablename__ = 'stu'


    def __repr__(self):
        return '<Student ({})>'.format(self.id)


