from typing import Callable

def sum(n: int, constructor: Callable) -> int:
    suma = 0
    for i in range(1, n+1): suma += constructor(i)
    return suma

def prove(constructor: Callable, sumatoria: Callable, up_to: int) -> bool:
    left_operand = sum(up_to - 1, constructor) + constructor(up_to)
    right_operand = sumatoria(up_to)

    return left_operand == right_operand

##numerito cualquiera

print(prove(lambda a: a*2+3, lambda a: pow(a, 2)+4*a+4, 5))





