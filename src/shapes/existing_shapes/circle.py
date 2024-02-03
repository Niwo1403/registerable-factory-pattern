# custom
from shapes import SelfCreatingShape


class Circle(SelfCreatingShape):

    IDENTIFIER = "circle"

    # Override
    def draw(self):
        print("Drawing circle.")
