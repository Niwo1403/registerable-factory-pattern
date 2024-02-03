# custom
from shapes import SelfCreatingShape


class Rectangle(SelfCreatingShape):

    IDENTIFIER = "rectangle"

    # Override
    def draw(self):
        print("Drawing rectangle.")
