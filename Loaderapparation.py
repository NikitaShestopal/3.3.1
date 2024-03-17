from Parallelogram import Parallelogram
from Cone import Cone
from Triangle import Triangle
from Rectangle import Rectangle
from Trapezoid import Trapezoid
from Circle import Circle
from Ball import Ball
from TriangularPyramid import TriangularPyramid
from QuadrangularPyramid import QuadrangularPyramid
from RectangularParallelepiped import RectangularParallelepiped
from TriangularPrism import TriangularPrism


class apparation:
    def __init__(self):
        pass

    @staticmethod
    def read_figures(file_name):
        figures = []
        with open(file_name, 'r') as file:
            for line in file:
                data = line.split()
                figure_type = data[0]
                params = list(map(float, data[1:]))
                if figure_type == 'Triangle':
                    figures.append(Triangle(*params))
                elif figure_type == 'Rectangle':
                    figures.append(Rectangle(*params))
                elif figure_type == 'Trapeze':
                    figures.append(Trapezoid(*params))
                elif figure_type == 'Parallelogram':
                    figures.append(Parallelogram(*params))
                elif figure_type == 'Circle':
                    figures.append(Circle(*params))
                elif figure_type == 'Ball':
                    figures.append(Ball(*params))
                elif figure_type == 'TriangularPyramid':
                    figures.append(TriangularPyramid(*params))
                elif figure_type == 'QuadrangularPyramid':
                    figures.append(QuadrangularPyramid(*params))
                elif figure_type == 'RectangularParallelepiped':
                    figures.append(RectangularParallelepiped(*params))
                elif figure_type == 'Cone':
                    figures.append(Cone(*params))
                elif figure_type == 'TriangularPrism':
                    figures.append(TriangularPrism(*params))
        return figures

    @staticmethod
    def find_max_volume_figure(figures):
        max_volume = 0
        max_volume_figure = None
        for figure in figures:
            volume = figure.volume()
            if volume is not None and volume > max_volume:
                max_volume = volume
                max_volume_figure = figure
        return max_volume_figure