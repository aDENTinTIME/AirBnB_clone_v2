#!/usr/bin/python3
'''
    Define class FileStorage
'''
import json
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class FileStorage:
    '''
        Serializes instances to JSON file and deserializes to JSON file.
    '''
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        '''
            Return the dictionary
        '''
        #print("in filestorage.py all")
        #print(self.__objects)
        return self.__objects
        """
        if cls:
            new_dict = {}
            for key, val in self.__objects.items():
                if val.__class__.__name__ == cls.__name__:
                    new_dict[key] = val
            return new_dict
        else:
            return self.__objects
        """
    def new(self, obj):
        '''
            Set in __objects the obj with key <obj class name>.id
            Aguments:
                obj : An instance object.
        '''
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        value_dict = obj
        FileStorage.__objects[key] = value_dict

    def save(self):
        '''
            Serializes __objects attribute to JSON file.
        '''
        objects_dict = {}
        for key, val in FileStorage.__objects.items():
            objects_dict[key] = val.to_dict()
        #print("in save of filestorage.py")
        #print(FileStorage.__objects)
        #print(objects_dict)
        #print("STOP")
        with open(FileStorage.__file_path, mode='w', encoding="UTF8") as fd:
            json.dump(objects_dict, fd)

    def reload(self):
        '''
            Deserializes the JSON file to __objects.
        '''
        try:
            with open(FileStorage.__file_path, encoding="UTF8") as fd:
                FileStorage.__objects = json.load(fd)
            for key, val in FileStorage.__objects.items():
                class_name = val["__class__"]
                class_name = classes[class_name]
                FileStorage.__objects[key] = class_name(**val)
            #print("in file_storage.py reload")
            #print(FileStorage.__objects)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        delete object from __objects if it's inside
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + str(obj.id)
            if key in self.__objects:
                del self.__objects[key]
        self.save()

        """
        if obj is not None:
            self.__objects.pop(obj.__class__.__name__
        + "." + str(obj.id), None)
            self.save()
        """
