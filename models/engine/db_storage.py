#!/usr/bin/python3
from models.base_model import Base, BaseModel
from sqlalchemy import create_engine
from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
import sys
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class DBStorage:
    """ A storage for the database"""
    __engine = None
    __session = None

    def __init__(self):
    
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST', 'localhost')
        db = getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                .format(user, password, host, db), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        classes = {
               'BaseModel': BaseModel, 'User': User, 'Place': Place,
               'State': State, 'City': City, 'Amenity': Amenity,
               'Review': Review
              }
        cls_dict = {}
        if cls:
            name = sys.module[__name__]
            cls = getattr(name, cls)
            output = self.__session.query(cls).all()
        else:
            output = []
            for class_name in classes:
                output.extend(self.__session.query(classes[class_name])).all()
        for obj in output:
            key = '{}.{}'.format(type(obj).__name__, obj.id)
            cls_dict[key] = obj
        return cls_dict

    def new(self, obj):
        self.__session.add(obj)
  
    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)
