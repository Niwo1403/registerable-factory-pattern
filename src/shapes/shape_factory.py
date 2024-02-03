# std
from typing import Dict, Type, Any
from inspect import isabstract
# custom
from .shape import Shape
from ._shape_creator import _ShapeCreator


class ShapeFactory:

    __shape_creators: Dict[Any, Type[_ShapeCreator]] = {}

    @classmethod
    def create_shape(cls, identifier: Any, *args, **kwargs) -> Shape:
        if identifier not in cls.__shape_creators:
            raise KeyError(f"Unknown identifier {identifier}.")
        shape = cls.__shape_creators[identifier].create_instance(*args,
                                                                 **kwargs)
        return shape

    @classmethod
    def register_shape_creator(cls,
                               shape_creator: Type[_ShapeCreator]) -> None:
        if isabstract(shape_creator):
            return
        if shape_creator.IDENTIFIER is None:
            raise ValueError(f"Can't register {shape_creator}, passed "
                             "shape_creator must have a specified identifier.")
        if shape_creator.IDENTIFIER in cls.__shape_creators:
            raise ValueError(f"Can't register {shape_creator}, identifier "
                             f"{shape_creator.IDENTIFIER} already used.")
        cls.__shape_creators[shape_creator.IDENTIFIER] = shape_creator
