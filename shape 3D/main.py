import pyvista as pv
from Shapes3D import Cylinder, Cone, Pyraimid 

class Shapes3D:
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    def render_shapes(self):
        plotter = pv.Plotter()
        for shape in self.shapes:
            plotter.add_mesh(shape.get_mesh())
        plotter.show()
