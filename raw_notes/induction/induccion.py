from typing import Callable

def suma(n: int, constructor: Callable) -> int:
    return sum([constructor(i) for i in range(1, n+1)])

## sumatoria --> función cuyo valor se desea probar
## constructor --> considerando una sumatoria de i=0 a n donde cada
## elemento es (2n-1), por ejemplo, la ecuación que construye los elementos
## de la sumatoria, es decir 2n-1
def prove(constructor: Callable, sumatoria: Callable) -> bool:
    up_to = int(20)

    left_operand = suma(up_to - 1, constructor) + constructor(up_to)
    right_operand = sumatoria(up_to)

    return left_operand == right_operand

print(prove(lambda a: 2*a+3, lambda a: pow(a,2) + 4*a))
