# std
from abc import ABC
# custom
from .interfaces import Shape, ShapeCreator


class SelfCreatingShape(Shape, ShapeCreator, ABC):

    # Override
    @classmethod
    def create_instance(cls, *args, **kwargs) -> Shape:
        # noinspection PyArgumentList
        # SelfCreatingShape takes no arguments,
        # but args & kwargs required for subclass arguments
        # -> arguments must be handled by subclass (by defining __init__)
        return cls(*args, **kwargs)
