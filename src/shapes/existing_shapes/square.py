# custom
from shapes import SelfCreatingShape


class Square(SelfCreatingShape):

    # Override
    @classmethod
    @property
    def identifier(cls) -> str:
        return "square"

    # Override
    def draw(self):
        print("Drawing square.")
