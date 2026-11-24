# 202037696_Grupo65

Sistema integrado de control para planta industrial, desarrollado en Python
para el curso **Lenguajes Interpretados (202037696)** de la UNAD.
Consolida los módulos del reto en un solo repositorio, versionado con Git
y normalizado bajo el estándar PEP 8.

## Integrantes y roles

| Integrante | Rol | Módulo aportado |
|------------|-----|-----------------|
| Joan Fernando Prieto Lebro | [Rol asignado] | Tarea 2, 3 y 4 |
| [Nombre] | [Rol asignado] | [Módulo] |
| [Nombre] | [Rol asignado] | [Módulo] |

Roles: Líder de Integración, Auditor PEP 8, Redactor Técnico y Revisor de
Calidad.

## Estructura del proyecto

```
202037696_Grupo65/
├── README.md
├── main.py
├── control/
│   └── tarea2_autoclave.py
├── diccionarios/
│   └── tarea3_bme680.py
└── optimizacion/
    └── tarea4_servomotores.py
```

## Descripción de los módulos

- **control/tarea2_autoclave.py**: simula el control de temperatura de un
  autoclave de alimentos con el sensor MAX31855. Maneja las fases de
  calentamiento, estabilización, enfriamiento y parada de emergencia, con un
  límite de muestras para evitar ciclos infinitos.
- **diccionarios/tarea3_bme680.py**: mapa de registros del sensor BME680
  (I2C) en un diccionario anidado, con consulta segura mediante `.get()` y
  máximo de tres intentos.
- **optimizacion/tarea4_servomotores.py**: procesamiento de coordenadas de
  servomotores para brazos robóticos. La versión optimizada pasó de 6,6 ms a
  412 µs (16,02 veces más rápida) con los mismos resultados.
- **main.py**: menú principal que integra todos los módulos.

## Requisitos

- Python 3.10 o superior
- No requiere librerías externas

## Cómo ejecutar

Desde la raíz del repositorio:

```
python main.py
```

## Estándar de código

Todo el código sigue PEP 8:

- Indentación de 4 espacios
- Nombres de variables y funciones en `snake_case`
- Constantes en MAYÚSCULAS
- Líneas de máximo 79 caracteres

Se puede verificar con:

```
pip install flake8
flake8 .
```

## Control de versiones

Cada integrante subió su módulo con sus propios commits. El historial de
aportes se puede consultar en **Insights → Contributors**.

## Contexto académico

Universidad Nacional Abierta y a Distancia (UNAD) - Escuela de Ciencias
Básicas, Tecnología e Ingeniería (ECBTI). Tarea 5: Proyecto en GitHub y
Artículo de Sustentación.