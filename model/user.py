# -*- coding: UTF-8 -*-
# author:      Liu Kun
# email:       liukunup@outlook.com
# timestamp:   2024/3/17 16:09
# description: XXX

from model import Base
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    # 表名
    __tablename__ = 'user'
    # 字段名
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String, nullable=True)
    #
    children = relationship("Address")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    # 字段名
    id = Column(Integer, primary_key=True)
    email = Column(String)
    #
    user_id = Column(Integer, ForeignKey('user.id'))

    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email={self.email!r})"
