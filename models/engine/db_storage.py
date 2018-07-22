#!/usr/bin/python3
"""create class DBStorage"""
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


database = getenv("HBNB_MYSQL_DB")
user = getenv("HBNB_MYSQL_USER")
host = getenv("HBNB_MYSQL_HOST")
password = getenv("HBNB_MYSQL_PWD")
hbnb_env = getenv("HBNB_ENV")

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class DBStorage:
    """class DBStorage"""
    __engine = None
    __session = None
    __dbobjects = {}

    def __init__(self):
        """initialize instances"""
        if hbnb_env == 'test':
            self.__table__.drop()
        else:
            self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format
                                        (database, user, host, password),
                                        pool_pre_ping=True)

    def all(self, cls=None):
        """return dictionary of instance attributes
        Args:
            cls (obj): memory address of class
        Returns:
            dictionary of objects
        """

        if cls is None:
            for k, v in classes.items():
                for obj in self.__session.query(val).all():
                    print(obj)
                    key = str(cls.__name__) + "." + str(obj.id)
                    val = obj
                    self.__dbobjects[key] = val
        else:
            if cls.__name__ in classes:
                for obj in self.session.query(classes[cls.__name__]).all():
                    print(obj)
                    key = str(cls.__name__) + "." + str(obj.id)
                    val = obj
                    self.__dbobjects[key] = val
        return self.__dbobjects

    def new(self, obj):
        """
        add object to current database session
        Args:
            obj (obj): an object
        """
        self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        Args:
            obj (obj): an object
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database and the current database session
        """
        Base.metadata.create_all(engine)
        self.__session = sessionmaker(engine, expire_on_commit=True)
        Session = scoped_session(self.__session)
