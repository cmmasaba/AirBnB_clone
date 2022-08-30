#!/usr/bin/python3
"""Defines all common attributes and methods for
other classes
"""

import models
from uuis import uuid4
from datetime import datetime


class BaseModels:
    """Represents the Basemodels of the AirBnB project"""

    def __init__(self, *args, **kwargs):
        """Initialize a new base model
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(knargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def save(self):
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
