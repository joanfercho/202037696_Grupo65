"""Tarea 2: Control de temperatura en autoclave (sensor MAX31855)."""


def simular_autoclave(temperatura=110, maximo_muestras=15):
    """Simula el control del autoclave y muestra cada lectura."""
    sistema_activo = True
    numero_muestras = 0

    while sistema_activo and numero_muestras < maximo_muestras:
        print(f"Muestra {numero_muestras + 1}")
        print(f"Temperatura registrada: {temperatura} °C")

        if temperatura > 130:
            print("ALERTA CRÍTICA: Parada de emergencia")
            sistema_activo = False
        elif temperatura < 115:
            print("Estado: Calentando autoclave")
            temperatura += 2
        elif temperatura <= 121:
            print("Estado: Fase estable de esterilización")
            temperatura += 1
        else:
            print("Estado: Enfriamiento activo")
            temperatura -= 3

        numero_muestras += 1

    if numero_muestras == maximo_muestras:
        print("\nSimulación finalizada: límite de muestras alcanzado.")
    else:
        print("\nSimulación finalizada por seguridad física.")


if __name__ == "__main__":
    simular_autoclave()