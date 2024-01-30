from shapes import ShapeFactory, SelfCreatingShape


# Only using existing shapes


draw_shapes = ["rectangle", "rectangle", "circle", "square"]
for ds in draw_shapes:
    shape = ShapeFactory.create_shape(ds)
    shape.draw()


# Adding new shape from outside the module


# Add new shape
class Polygon(SelfCreatingShape):

    def __init__(self, corners: int):
        self.corners = corners

    # Override
    @classmethod
    @property
    def identifier(cls) -> str:
        return "polygon"

    # Override
    def draw(self):
        print(f"Drawing polygon with {self.corners} corners.")


# Update shapes (only once after all new ShapeCreator / SelfCreatingShape are loaded)
ShapeFactory.reload_shape_creators()

# Use new shape
# __init__ arguments must be passed to ShapeFactory.create_shape
shape = ShapeFactory.create_shape("polygon", 11)
shape.draw()
shape.draw()
