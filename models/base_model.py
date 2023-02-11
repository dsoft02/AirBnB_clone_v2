!#/usr/bin/python3
"""Definiton of the BaseModel class."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
	"""This is BaseModel of the AirBnb clone."""

	def __init__(self, *args, **kwargs):
		"""Initizialises a BaseModel.

		Args:
			*args (any): Unused.
            **kwargs (dict): Key/value pairs of attributes.
		"""
		tform = "%Y-%m-%dT%H:%M:%S.%f"
		self.id = str(uuid4())
		self.created_at = datetime.today()
		self.updated_at = datetime.today()

	def save(self):
		"""Updates updated_at to the current day"""
		self.updated_at = datetime.today()

	def to_dict(self):
		"""Returns a dictionary of the BaseModel instance.
		Includes the key/value pair __class__ representing
        the class name of the object.
		"""
		class_dict = self.__dict__.copy()
		class_dict["created_at"] = self.created_at.isoformat()
		class_dict["updated_at"] = self.updated_at.isoformat()
		class_dict["__class__"]  = self.__class__.__name__
		return class_dict

	def __str__(self):
		"""Return the print/str representation of the BaseModel instance."""
		class_name = self.__class__.__name__
		return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


