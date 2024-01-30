# custom
from shapes import SelfCreatingShape


class Circle(SelfCreatingShape):

    # Override
    @classmethod
    @property
    def identifier(cls) -> str:
        return "circle"

    # Override
    def draw(self):
        print("Drawing circle.")
