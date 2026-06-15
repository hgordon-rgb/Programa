# Proyecto: Programación Tradicional y Orientada a Objetos en Python

## Descripción
Este proyecto contiene dos programas desarrollados en Python con el objetivo de comparar dos enfoques de programación:

1. **Programación Tradicional** (uso de funciones y variables).
2. **Programación Orientada a Objetos (POO)** (uso de clases y objetos).

Ambos programas permiten registrar y mostrar la información de una mascota.

---

##  Estructura del proyecto

programacion_tradicional/
└── tradicional.py
programacion_poo/
├── main.py
└── mascota.py

---

##  Programa 1: Programación Tradicional

### Características
- Uso de funciones.
- Solicitud de datos por teclado.
- Uso de variables para almacenar información.
- No se utilizan clases ni objetos.

### Funciones principales
- `registrar_mascota()`: solicita los datos al usuario.
- `mostrar_mascota()`: muestra la información organizada.

---

##  Programa 2: Programación Orientada a Objetos (POO)

### Características
- Uso de clase `Mascota`.
- Creación de objetos.
- Definición de atributos:
  - nombre
  - especie
  - edad
- Implementación de métodos:
  - `mostrar_informacion()`
  - `hacer_sonido()`

### Archivos
- `mascota.py`: contiene la clase.
- `main.py`: crea objetos y ejecuta métodos.

---

##  Ejecución de los programas

### Programa 1
cd programacion_tradicional
python tradicional.py

### Programa 2
cd programacion_poo
python main.py

## Ejemplo de salida
=== Información de la Mascota ===
Nombre: Firulais
Especie: Perro
Edad: 3
Firulais hace un sonido...

---

## Conceptos aplicados

### Programación Tradicional
- Variables
- Funciones
- Entrada de datos por teclado

### Programación Orientada a Objetos
- Clases
- Objetos
- Atributos
- Métodos
- Abstracción

---

## Conclusión
El proyecto permite comprender la diferencia entre la programación tradicional y la programación orientada a objetos, demostrando cómo la POO facilita la organización, reutilización y escalabilidad del código.

