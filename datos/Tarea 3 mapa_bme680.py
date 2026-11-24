mapa_bme680 = {
    "0x60": {
        "status": True,
        "calib_val": 12,
        "limit": 100
    },
    "0x61": {
        "status": True,
        "calib_val": 55,
        "limit": 200
    },
    "0x62": {
        "status": False,
        "calib_val": 88,
        "limit": 90
    }
}

maximo_intentos = 3
intento = 0
consulta_exitosa = False

while intento < maximo_intentos and not consulta_exitosa:
    direccion = input(
        "Ingrese una dirección: "
    ).strip()

    registro = mapa_bme680.get(direccion)

    if registro is not None:
        print("\nRegistro encontrado")
        print(f"Dirección: {direccion}")
        print(f"Estado: {registro.get('status')}")
        print(f"Calibración: {registro.get('calib_val')}")
        print(f"Límite: {registro.get('limit')}")
        consulta_exitosa = True
    else:
        intento += 1
        restantes = maximo_intentos - intento

        print("Dirección no encontrada.")
        print(f"Intentos restantes: {restantes}")

if not consulta_exitosa:
    print(
        "\nConsulta finalizada: "
        "máximo de intentos alcanzado."
    )