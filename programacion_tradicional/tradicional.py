# Función para registrar los datos de la mascota
def registrar_mascota():
    print("=== Registro de Mascota ===")
    nombre = input("Ingrese el nombre de la mascota: ")
    edad = input("Ingrese la edad de la mascota: ")
    tipo = input("Ingrese el tipo de mascota (perro, gato, etc.): ")
    
    
    # Guardamos los datos en variables
    mascota = {
        "nombre": nombre,
        "edad": edad,
        "tipo": tipo,
     
    }
    
    return mascota


# Función para mostrar los datos de la mascota
def mostrar_mascota(mascota):
    print("\n=== Información de la Mascota ===")
    print(f"Nombre: {mascota['nombre']}")
    print(f"Edad: {mascota['edad']}")
    print(f"Tipo: {mascota['tipo']}")
    


# Función principal
def main():
    mascota = registrar_mascota()
    mostrar_mascota(mascota)


# Ejecutar el programa
main()
