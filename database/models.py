from database import Base
import datetime
from sqlalchemy import String, Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

# Таблица пользователя
class User(Base):
    __tablename__ = 'user'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    city = Column(String)
    birthday = Column(String)
    profile_photo = Column(String)
    reg_date = Column(DateTime, default=datetime.datetime.now())


class Post(Base):
    __tablename__ = 'post'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))
    post_text = Column(String, nullable=True)
    likes = Column(Integer, default=0)
    publish_date = Column(DateTime, default=datetime.datetime.now())
    user_fk = relationship(User)


class PostPhoto(Base):
    __tablename__ = 'post_photo'
    photo_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    photo_path = Column(String, nullable=False)
    post_fk = relationship(Post)


class PostComment(Base):
    __tablename__ = 'post_comment'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('post.post_id'))
    user_id = Column(Integer, ForeignKey('user.user_id'))
    comment_text = Column(String, nullable=False)
    publish_date = Column(DateTime, default=datetime.datetime.now())
    user_fk = relationship(User)
    post_fk = relationship(Post)

