from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    #数据库中的表
    __tablename__='ych_table'

    Id = Column(String(20),primary_key=True)
    name = Column(String(20))

#向数据库中插入数据
def insertData():
    engine = create_engine('mysql+pymysql://root:115@817&@localhost:3306/ych')
    DBSession = sessionmaker(bind=engine)
    # 创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = User(Id='5', name='Bob')
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

#从数据库中查询
def selectData():
    engine = create_engine('mysql+pymysql://root:115@817&@localhost:3306/ych')
    DBSession = sessionmaker(bind=engine)
    session = DBSession()
    user = session.query(User).filter(User.Id=='5').one()
    print('type:',type(user))
    print('name:',user.name)
    session.close()

selectData() 

# class User(Base):
#     __tablename__ = 'user'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # 一对多:
#     books = relationship('Book')

# class Book(Base):
#     __tablename__ = 'book'

#     id = Column(String(20), primary_key=True)
#     name = Column(String(20))
#     # “多”的一方的book表是通过外键关联到user表的:
#     user_id = Column(String(20), ForeignKey('user.id'))