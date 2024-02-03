# std
from abc import ABC, abstractmethod
# custom
from .shape import Shape


class BaseShapeCreator(ABC):

    IDENTIFIER = None

    @classmethod
    @abstractmethod
    def create_instance(cls, *args, **kwargs) -> Shape:
        raise NotImplementedError("create_instance classmethod must be "
                                  "overwritten in subclasses.")
