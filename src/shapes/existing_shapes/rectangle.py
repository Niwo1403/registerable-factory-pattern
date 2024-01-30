# custom
from shapes import SelfCreatingShape


class Rectangle(SelfCreatingShape):

    # Override
    @classmethod
    @property
    def identifier(cls) -> str:
        return "rectangle"

    # Override
    def draw(self):
        print("Drawing rectangle.")
