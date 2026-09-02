import math 

A = math.ceil(2 + (3 * (6 / 2)))
B = math.ceil((4 + 6) / (2 + 3))
C = math.ceil((4 / 2) ** 5)
D = math.ceil((4 / 2) ** (5 + 1))
E = math.ceil((-3) ** 2)
F = math.ceil(-(3 ** 2))

print(A)
print(B)
print(C)
print(D)
print(E)
print(F)
# Bloque 1: Operaciones enteras, jerarquía y signos unarios
expresiones_1 = {
    "a": 2 + 3 + 1 + 2,
    "b": 2 + 3 * 1 + 2,
    "c": (2 + 3) * 1 + 2,
    "d": (2 + 3) * (1 + 2),
    "e": +---6,
    "f": -+-+6,
}

# Bloque 2: Operaciones con números flotantes, división y notación científica
expresiones_2 = {
    "a": 1 / 2 / 4.0,
    "b": 1 / 2.0 / 4.0,
    "c": 1 / 2.0 / 4,
    "d": 1.0 / 2 / 4,
    "e": 4**.5,
    "f": 4.0 ** (1 / 2),
    "g": 4.0 ** (1 / 2) + 1 / 2,
    "h": 4.0 ** (1.0 / 2) + 1 / 2.0,
    "i": 3e3 / 10,
    "j": 10 / 5e-3,
    "k": 10 / 5e-3 + 1,
    "l": 3 / 2 + 1,
}

for bloque, exps in [("BLOQUE 1", expresiones_1), ("BLOQUE 2", expresiones_2)]:
    print(f"\n--- {bloque} ---")
    for item, res in exps.items():
        print(f"{item}) Resultado: {res:<8} | Tipo: {type(res).__name__}")