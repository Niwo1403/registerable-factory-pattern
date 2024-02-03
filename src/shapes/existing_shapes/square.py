# custom
from shapes import SelfCreatingShape


class Square(SelfCreatingShape):

    IDENTIFIER = "square"

    # Override
    def draw(self):
        print("Drawing square.")
