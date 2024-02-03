# std
from typing import Type
from abc import ABCMeta, ABC
# custom
from .shape_factory import ShapeFactory
from ._shape_creator import _ShapeCreator


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


class ShapeCreator(_ShapeCreator, ABC, metaclass=ShapeCreatorMeta):
    pass
