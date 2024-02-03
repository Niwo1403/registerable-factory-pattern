# std
from typing import Type
from abc import ABCMeta, ABC
# custom
from shapes.shape_factory import ShapeFactory
from .base_shape_creator import BaseShapeCreator


class ShapeCreatorMeta(ABCMeta, type):

    IDENTIFIER = None

    def __init__(cls: Type["ShapeCreator"], name, bases, attrs):
        super().__init__(name, bases, attrs)
        if cls.IDENTIFIER is not None:
            ShapeFactory.register_shape_creator(cls)

    def __setattr__(cls, name, value):
        if name == "IDENTIFIER":
            raise AttributeError("Can't modify .IDENTIFIER")
        return super().__setattr__(name, value)


class ShapeCreator(BaseShapeCreator, ABC, metaclass=ShapeCreatorMeta):
    pass
