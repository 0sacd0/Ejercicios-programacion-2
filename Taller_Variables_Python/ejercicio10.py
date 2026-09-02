nombre = input("Ingrese el nombre del empleado: ")
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
valor_hora = float(input("Ingrese el valor de cada hora: "))

salario = horas_trabajadas * valor_hora

print("Empleado:", nombre)
print("Salario: $", salario)
