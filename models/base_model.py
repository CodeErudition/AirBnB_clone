#!/usr/bin/python3
""" This module defines a BaseModel Class"""

from datetime import datetime
import uuid
import models


class BaseModel():
    """
    This class represents the base model of
    the this project
    """
    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            for key, value in kwargs.items():
                if key != '__class__':
                    satattr(self, key, value,)
                else:
                    self.id = str(uuid.uuid4())
                    self.created_at datetime.now()
                    self.updated_at datetime.now()
                    models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute `updated_at` with
        the current datetime.
        """
        self.updated_at = datetime.now()
        model.storage.save()

    def __str__(self):
        """
        Returns a string representation of the BaseModel.

        Returns:
            str: The string representation of the BaseModel.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of `__dict__`
        of the instance.Includes `__class__` and converts `created_at`
        and `updated_at` to ISO format.
        """
        dict_data = dict(self.__dict__)
        dict_data["__class__"] = self.__class__.__name__
        dict_data["created_at"] = self.__dict__created_at.isoformat()
        dict_data["updated_at"] = self.__dict__updated_at.isoformat()
        return (dict_data)
