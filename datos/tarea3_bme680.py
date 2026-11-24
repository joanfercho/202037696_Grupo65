"""Tarea 3: Mapa de registros del sensor BME680 (I2C)."""

MAPA_BME680 = {
    "0x60": {"status": True, "calib_val": 12, "limit": 100},
    "0x61": {"status": True, "calib_val": 55, "limit": 200},
    "0x62": {"status": False, "calib_val": 88, "limit": 90},
}


def consultar_registro(maximo_intentos=3):
    """Consulta un registro con un máximo de intentos fallidos."""
    intento = 0
    consulta_exitosa = False

    while intento < maximo_intentos and not consulta_exitosa:
        direccion = input("Ingrese una dirección: ").strip()
        registro = MAPA_BME680.get(direccion)

        if registro is not None:
            print("\nRegistro encontrado")
            print(f"Dirección: {direccion}")
            print(f"Estado: {registro.get('status')}")
            print(f"Calibración: {registro.get('calib_val')}")
            print(f"Límite: {registro.get('limit')}")
            consulta_exitosa = True
        else:
            intento += 1
            print("Dirección no encontrada.")
            print(f"Intentos restantes: {maximo_intentos - intento}")

    if not consulta_exitosa:
        print("\nConsulta finalizada: máximo de intentos alcanzado.")


if __name__ == "__main__":
    consultar_registro()