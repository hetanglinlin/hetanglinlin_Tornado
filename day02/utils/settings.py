from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 连接数据库mysql的格式
url = 'mysql+pymysql://root:@127.0.0.1:3306/tornado1901'

# 创建数据库的链接
engine = create_engine(url)

# 表示模型和数据库中表的关联关系的基类
Base = declarative_base(bind=engine)

# 生成事务session
SessionMaker = sessionmaker(bind=engine)
session = SessionMaker()





