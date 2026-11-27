"""Cálculo de áreas de figuras geométricas (versión refactorizada)."""
import math


def area_circulo(radio):
    """Devuelve el área de un círculo."""
    return math.pi * radio ** 2


def area_rectangulo(base, altura):
    """Devuelve el área de un rectángulo."""
    return base * altura


def area_triangulo(base, altura):
    """Devuelve el área de un triángulo."""
    return base * altura / 2


def mostrar_area(nombre_figura, area):
    """Muestra el área con un formato único."""
    print(f"Área del {nombre_figura}: {area:.2f}")


def main():
    mostrar_area("círculo", area_circulo(2))
    mostrar_area("rectángulo", area_rectangulo(4, 5))
    mostrar_area("triángulo", area_triangulo(6, 3))


if __name__ == "__main__":
    main()
