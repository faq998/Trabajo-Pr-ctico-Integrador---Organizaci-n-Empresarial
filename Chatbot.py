# Trabajo Práctico Integrador - Organización Empresarial
# Simulación del proceso de nominación de Gas Natural

print("=" * 60)
print("SISTEMA DE NOMINACIÓN DE GAS NATURAL")
print("=" * 60)

# Solicitud de cantidad de GN
while True:
    cantidad = input("\nIngrese la cantidad de GN solicitada (DAM3): ")

    # Validación de dato vacío
    if cantidad == "":
        print("Error: debe ingresar una cantidad.")
        continue

    # Validación de dato numérico
    if not cantidad.isdigit():
        print("Error: debe ingresar un valor numérico.")
        continue

    cantidad = int(cantidad)

    # Validación contractual
    if cantidad > 2000:
        print("Error: la cantidad supera el límite contractual de 2000 DAM3.")
        continue

    break

print(f"\nSolicitud enviada a Trafigura por {cantidad} DAM3.")

# Respuesta simulada de Trafigura
print("\nSeleccione la respuesta de Trafigura:")
print("1 - Disponibilidad completa")
print("2 - Disponibilidad parcial")
print("3 - Sin disponibilidad")

opcion = input("Opción: ")

if opcion == "1":
    disponible = cantidad

elif opcion == "2":
    disponible = int(cantidad * 0.7)

else:
    disponible = 0

# Evaluación de disponibilidad
if disponible == 0:
    print("\nTrafigura informa disponibilidad nula.")
    print("Proceso finalizado.")
else:
    print(f"\nTrafigura informa {disponible} DAM3 disponibles.")

    print("\nRespuesta de CAMMESA:")
    print("1 - Operar con Gas Natural")
    print("2 - Operar con Gas Oil")

    combustible = input("Opción: ")

    if combustible == "1":
        print("\nCAMMESA operará con Gas Natural.")
        print("Se informa a Trafigura que el volumen será utilizado.")

    else:
        print("\nCAMMESA operará con Gas Oil.")
        print("Se informa a Trafigura que el volumen no será utilizado.")

    print("\nSe informa a las centrales el combustible de operación.")
    print("Proceso finalizado.")

print("\nFin de la simulación.")