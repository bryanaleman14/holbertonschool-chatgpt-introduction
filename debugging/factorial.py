#!/usr/bin/python3

import sys

def factorial(n):
    if n <= 0:
        return "Error"
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

if __name__ == "__main__":
    if len(sys.argv) !=2:
        print("Uso: {} <numero>".format(sys.argv[0]))
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print("El argumento debe ser un numero entero")
        sys.exit(1)

f = factorial(n)
print(f"El factorial de {n} es {f}")
