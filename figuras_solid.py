"""Figuras geométricas aplicando SRP y Open/Closed."""
import math
from abc import ABC, abstractmethod


class Figura(ABC):
    """Abstracción: toda figura sabe calcular su área."""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def nombre(self) -> str:
        pass


class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def nombre(self):
        return "Círculo"


class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def nombre(self):
        return "Rectángulo"


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura / 2

    def nombre(self):
        return "Triángulo"


class CalculadoraAreas:
    """Responsabilidad única: sumar áreas de cualquier lista de figuras."""

    def area_total(self, figuras):
        return sum(figura.area() for figura in figuras)


class ReporteAreas:
    """Responsabilidad única: mostrar resultados en pantalla."""

    def imprimir(self, figuras):
        for figura in figuras:
            print(f"{figura.nombre()}: {figura.area():.2f}")
        total = CalculadoraAreas().area_total(figuras)
        print(f"Área total: {total:.2f}")


if __name__ == "__main__":
    figuras = [Circulo(2), Rectangulo(4, 5), Triangulo(6, 3)]
    ReporteAreas().imprimir(figuras)
