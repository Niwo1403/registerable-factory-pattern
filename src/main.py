from shapes import ShapeFactory, SelfCreatingShape


# Only using existing shapes


draw_shapes = ["rectangle", "rectangle", "circle", "square"]
for ds in draw_shapes:
    shape = ShapeFactory.create_shape(ds)
    shape.draw()


# Adding new shape from outside the module


# Add new shape
class Polygon(SelfCreatingShape):

    IDENTIFIER = "polygon"

    def __init__(self, corners: int):
        self.corners = corners

    # Override
    def draw(self):
        print(f"Drawing polygon with {self.corners} corners.")


# Use new shape
# __init__ arguments must be passed to ShapeFactory.create_shape
shape = ShapeFactory.create_shape("polygon", 11)
shape.draw()
shape.draw()

print("Known shapes:", ShapeFactory.get_identifiers())
