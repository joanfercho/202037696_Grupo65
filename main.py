"""Sistema integrado de control para planta industrial."""

from control.tarea2_autoclave import simular_autoclave
from diccionarios.tarea3_bme680 import consultar_registro
from optimizacion.tarea4_servomotores import (
    procesar_coordenadas_servo_optimizado,
)


def mostrar_menu():
    """Muestra las opciones disponibles del sistema."""
    print("\n=== Sistema integrado ===")
    print("1. Simular autoclave (MAX31855)")
    print("2. Consultar registros del BME680")
    print("3. Procesar ángulos de servomotores")
    print("0. Salir")


def ejecutar_sistema():
    """Ejecuta el menú principal hasta que el usuario salga."""
    opcion = ""

    while opcion != "0":
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            simular_autoclave()
        elif opcion == "2":
            consultar_registro()
        elif opcion == "3":
            angulos = procesar_coordenadas_servo_optimizado()
            print(f"Ángulos procesados: {len(angulos)}")
        elif opcion != "0":
            print("Opción no válida.")


if __name__ == "__main__":
    ejecutar_sistema()