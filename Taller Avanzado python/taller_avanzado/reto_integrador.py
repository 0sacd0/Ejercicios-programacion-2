def sistema_ventas_integrador():
    print('\n=== Reto integrador: Sistema de ventas ===')
    ventas = []
    total_bruto = 0.0
    total_descuentos = 0.0
    total_recargos = 0.0
    total_recibido = 0.0
    cantidad_descuentos = 0
    pagos = {'efectivo': 0, 'tarjeta': 0, 'transferencia': 0}

    while True:
        print('\nSISTEMA DE VENTAS')
        print('1. Registrar una venta')
        print('2. Consultar resumen de ventas')
        print('3. Consultar venta mayor y menor')
        print('4. Aplicar cierre de caja')
        print('5. Salir')
        opcion = int(input('Seleccione una opción: '))

        if opcion == 1:
            cliente = input('Nombre del cliente: ')
            cantidad = int(input('Cantidad de productos: '))
            precios = []
            for i in range(cantidad):
                precio = float(input(f'Precio del producto {i + 1}: '))
                precios.append(precio)
            metodo = input('Medio de pago (efectivo, tarjeta, transferencia): ').lower().strip()
            subtotal = sum(precios)
            descuento = 0.0
            if subtotal > 500000:
                descuento = subtotal * 0.10
                cantidad_descuentos += 1
            cargo = 0.0
            if metodo == 'tarjeta':
                cargo = subtotal * 0.02
                pagos['tarjeta'] += 1
            elif metodo == 'transferencia':
                pagos['transferencia'] += 1
            elif metodo == 'efectivo':
                pagos['efectivo'] += 1
            else:
                print('Medio de pago inválido.')
                continue

            total_venta = subtotal - descuento + cargo
            ventas.append({
                'cliente': cliente,
                'subtotal': subtotal,
                'descuento': descuento,
                'cargo': cargo,
                'total': total_venta,
                'metodo': metodo,
            })
            total_bruto += subtotal
            total_descuentos += descuento
            total_recargos += cargo
            total_recibido += total_venta
            print(f'Venta registrada correctamente. Total: ${total_venta:,.0f}')

        elif opcion == 2:
            if not ventas:
                print('Todavía no existen ventas.')
                continue
            print('\nRESUMEN DE VENTAS')
            print(f'Cantidad de ventas realizadas: {len(ventas)}')
            print(f'Valor total antes de descuentos: ${total_bruto:,.0f}')
            print(f'Total de descuentos: ${total_descuentos:,.0f}')
            print(f'Total de recargos: ${total_recargos:,.0f}')
            print(f'Dinero definitivo recibido: ${total_recibido:,.0f}')
            print(f'Promedio de ventas: ${total_recibido / len(ventas):,.0f}')
            print(f'Venta más alta: ${max(v["total"] for v in ventas):,.0f}')
            print(f'Venta más baja: ${min(v["total"] for v in ventas):,.0f}')
            print('Cantidad de pagos por medio:')
            for medio, cantidad in pagos.items():
                print(f'  {medio}: {cantidad}')
            print(f'Cantidad de clientes que recibieron descuento: {cantidad_descuentos}')

        elif opcion == 3:
            if not ventas:
                print('Todavía no existen ventas.')
                continue
            venta_mayor = max(ventas, key=lambda v: v['total'])
            venta_menor = min(ventas, key=lambda v: v['total'])
            print(f'Venta mayor: {venta_mayor["cliente"]} -> ${venta_mayor["total"]:,.0f}')
            print(f'Venta menor: {venta_menor["cliente"]} -> ${venta_menor["total"]:,.0f}')

        elif opcion == 4:
            if not ventas:
                print('Todavía no existen ventas.')
                continue
            print('\nCIERRE DE CAJA')
            print(f'Ventas realizadas: {len(ventas)}')
            print(f'Valor total antes de descuentos: ${total_bruto:,.0f}')
            print(f'Total de descuentos: ${total_descuentos:,.0f}')
            print(f'Total de recargos: ${total_recargos:,.0f}')
            print(f'Total recibido: ${total_recibido:,.0f}')
            print('Caja cerrada correctamente.')

        elif opcion == 5:
            print('Programa finalizado.')
            break
        else:
            print('Opción inválida.')
