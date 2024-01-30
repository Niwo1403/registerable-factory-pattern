# std
from abc import ABC, abstractmethod
# custom
from .shape import Shape


class ShapeCreator(ABC):

    # noinspection PyPropertyDefinition
    # PyCharm doesn't detect the classmethod annotation if it's a property
    @classmethod
    @property
    @abstractmethod
    def identifier(cls) -> str:
        pass  # properties shouldn't raise NotImplementedError

    @classmethod
    @abstractmethod
    def create_instance(cls, *args, **kwargs) -> Shape:
        raise NotImplementedError("create_instance classmethod must be "
                                  "overwritten in subclasses.")
