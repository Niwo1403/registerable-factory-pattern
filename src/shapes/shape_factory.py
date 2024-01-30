# std
from typing import Dict, Type, Any, Set
from warnings import warn
from inspect import isabstract
# custom
from .shape import Shape
from .shape_creator import ShapeCreator


class ShapeFactory:

    __shape_creators: Dict[Any, Type[ShapeCreator]] = {}
    __registered_shape_creators = False

    @classmethod
    def reload_shape_creators(cls) -> None:
        cls.__shape_creators = {}
        cls.__registered_shape_creators = False
        cls._register_shape_creator_subclasses()

    @classmethod
    def create_shape(cls, identifier: Any, *args, **kwargs) -> Shape:
        if not cls.__registered_shape_creators:
            cls._register_shape_creator_subclasses()
        if identifier not in cls.__shape_creators:
            raise KeyError(f"Unknown identifier {identifier}.")
        shape = cls.__shape_creators[identifier].create_instance(*args,
                                                                 **kwargs)
        return shape

    @staticmethod
    def _get_shape_creator_subclasses() -> Set[Type[ShapeCreator]]:
        def get_all_subclasses(cls: Type[ShapeCreator]
                               ) -> Set[Type[ShapeCreator]]:
            cls_subclasses = set(cls.__subclasses__())
            cls_sub_subclasses = [
                subclass
                for subclasses in cls_subclasses
                for subclass in get_all_subclasses(subclasses)]
            return cls_subclasses.union(cls_sub_subclasses)
        return get_all_subclasses(ShapeCreator)

    @classmethod
    def _register_shape_creator_subclasses(cls) -> None:
        if cls.__registered_shape_creators:
            warn("Shape creators already registered!")
        shape_creator_subclasses = cls._get_shape_creator_subclasses()
        for shape_creator_subclass in shape_creator_subclasses:
            if isabstract(shape_creator_subclass):
                continue
            identifier = shape_creator_subclass.identifier
            if identifier is None:
                raise ValueError("Passed shape_creator must have "
                                 "a specified identifier.")
            if identifier in cls.__shape_creators:
                raise ValueError(f"Identifier {identifier} already used.")
            cls.__shape_creators[identifier] = shape_creator_subclass
        cls.__registered_shape_creators = True
