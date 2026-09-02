precio_comida = float(input("Ingrese el precio de la comida: "))
precio_bebida = float(input("Ingrese el precio de la bebida: "))
cantidad_personas = int(input("Ingrese la cantidad de personas: "))

total_cuenta = precio_comida + precio_bebida
valor_por_persona = total_cuenta / cantidad_personas

print("Total de la cuenta: $", total_cuenta)
print("Valor por persona: $", valor_por_persona)
