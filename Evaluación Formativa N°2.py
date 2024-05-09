import time

def main():
    # Precios de los Rolls
    precios = {
        1: 4500,
        2: 5000,
        3: 5200,
        4: 4800
    }

    # Diccionario para contabilizar los Rolls pedidos
    pedido = {
        1: 0,
        2: 0,
        3: 0,
        4: 0
    }

    # Menú de opciones
    while True:
        print("Menú:")
        print("1. Pikachu Roll - $4500")
        print("2. Otaku Roll - $5000")
        print("3. Pulpo Venenoso Roll - $5200")
        print("4. Anguila Eléctrica Roll - $4800")
        print("5. Terminar pedido")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "5":
            break

        try:
            opcion = int(opcion)
            if opcion < 1 or opcion > 5:
                raise ValueError
        except ValueError:
            print("Opción inválida. Por favor, seleccione una opción válida.")
            continue

        cantidad = input("Ingrese la cantidad: ")
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                raise ValueError
        except ValueError:
            print("Cantidad inválida. Por favor, ingrese un número entero positivo.")
            continue

        pedido[opcion] += cantidad

    # Calcular el subtotal del pedido
    subtotal = sum (pedido[roll] * precios[roll] for roll in pedido)

    # Verificar si hay código de descuento
    codigo_descuento = input("¿Tiene un código de descuento? (Ingrese 'soyotaku' o 'X' para salir): ")

    if codigo_descuento == "soyotaku":
        descuento = subtotal * 0.10
        total = subtotal - descuento
    elif codigo_descuento == "X":
        print("Saliendo del programa...")
        return
    else:
        print("Código no válido.")
        codigo_descuento = input("Ingrese nuevamente el código de descuento o 'X' para salir: ")
        if codigo_descuento == "soyotaku":
            descuento = subtotal * 0.10
            total = subtotal - descuento
        elif codigo_descuento == "X":
            print("Saliendo del programa...")
            return
        else:
            print("Código no válido. Saliendo del programa...")
            return

    # Mostrar detalle del pedido
    print("******************************")
    print("TOTAL PRODUCTOS:", sum(pedido.values()))
    print("******************************")
    for roll, cantidad in pedido.items():
        print(f"{roll}. {nombre_roll(roll)}: {cantidad}")
    print("******************************")
    print("Subtotal por pagar: ${}".format(subtotal))
    if codigo_descuento == "soyotaku":
        print("Descuento por código: ${}".format(descuento))
    print("TOTAL: ${}".format(total))
    print("******************************")
    time.sleep (2)
    

    # Preguntar al usuario si desea realizar otro pedido o salir del programa
    continuar = input("¿Desea realizar otro pedido? (Ingrese 'S' para sí o cualquier otra tecla para salir): ")
    if continuar.lower() == "s":
        main()
    else:
        print("Saliendo del programa...")

def nombre_roll(roll):
    rolls = {
        1: "Pikachu Roll",
        2: "Otaku Roll",
        3: "Pulpo Venenoso Roll",
        4: "Anguila Eléctrica Roll"
    }
    return rolls.get(roll, "Roll Desconocido")

if __name__ == "__main__":
    main()