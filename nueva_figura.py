"""Extensión: se agrega Cuadrado SIN modificar figuras_solid.py."""
from figuras_solid import Figura, Circulo, Rectangulo, Triangulo, ReporteAreas


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado ** 2

    def nombre(self):
        return "Cuadrado"


if __name__ == "__main__":
    figuras = [Circulo(2), Rectangulo(4, 5), Triangulo(6, 3), Cuadrado(3)]
    ReporteAreas().imprimir(figuras)
