def total_mes(ventas, mes):
    return sum(ventas.get(mes, []))
def promedio_general(ventas):
    valores = [valor for mes in ventas.values() for valor in mes]
    if not valores:
        return 0
    return sum(valores) / len(valores)
def mejor_mes(ventas):
    if not ventas:
        return None
    return max(ventas, key=lambda mes: sum(ventas[mes]))
def filtrar_ventas_altas(ventas, limite):
    resultado = []
    for mes in ventas.values():
        for valor in mes:
            if valor > limite:
                resultado.append(valor)
    return resultado
def reporte_final(ventas):
    print("Total por mes:")
    for mes, valores in ventas.items():
        print(f"{mes.capitalize()}: {total_mes(ventas, mes)}")

    promedio = promedio_general(ventas)
    mejor = mejor_mes(ventas)
    print(f"Promedio general trimestral: {promedio}")
    print(f"Mejor mes: {mejor}")
    print(f"Ventas mayores al límite: {filtrar_ventas_altas(ventas, 1500)}")
if __name__ == '__main__':
    ventas = {
        'enero': [1200, 1500, 800, 900],
        'febrero': [1000, 1100, 1200],
        'marzo': [1800, 1700, 1600, 2000],
    }
    reporte_final(ventas)
