"""Tarea 4: Procesamiento de coordenadas de servomotores."""

ANGULOS_EJE_ROBOT = [45.5, 90.2, 12.3, 179.9] * 4000


def procesar_coordenadas_servo():
    """Versión original: convierte a texto y luego a entero."""
    angulos_enteros = []

    for angulo in ANGULOS_EJE_ROBOT:
        cadena_texto = str(angulo)
        parte_entera = cadena_texto.split(".")[0]
        valor_final = int(parte_entera)
        angulos_enteros.append(valor_final)

    return angulos_enteros


def procesar_coordenadas_servo_optimizado():
    """Convierte directamente los ángulos decimales a enteros."""
    return [int(angulo) for angulo in ANGULOS_EJE_ROBOT]


if __name__ == "__main__":
    resultado_original = procesar_coordenadas_servo()
    resultado_optimizado = procesar_coordenadas_servo_optimizado()

    print(f"¿Resultados iguales?: {resultado_original == resultado_optimizado}")
    print(f"Ángulos procesados: {len(resultado_optimizado)}")