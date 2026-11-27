"""Función para determinar si un número es primo."""
import math


def es_primo(numero: int) -> bool:
    """Devuelve True si el número es primo, False en caso contrario."""
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = math.isqrt(numero)
    for divisor in range(3, limite + 1, 2):
        if numero % divisor == 0:
            return False
    return True
