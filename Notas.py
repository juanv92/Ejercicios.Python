estudiantes = [
    {'nombre':'Juan','notas':[3,0,4,0,3,0]},
    {'nombre':'Ana','notas':[5,0,4,0,4,8]},
    {'nombre':'Andres','notas':[3,5,3,5,4,8]}
]

print("---BASE DE DATOS CARGADA---")
print(f"Total de estudiantes: {len(estudiantes)}")

def calcular_promedio(lista_notas):
    """ Calcula el promedio de una lista de floats"""
    if len(lista_notas) == 0:
        return 0
    suma = 0
    for i in lista_notas:
        suma += i 
    return suma/len(lista_notas)

print("Prueba promedio Juan: ",calcular_promedio(estudiantes[0]['notas']))

def generar_reporte():
    print("\n--- REPORTE FINAL ---\n")
    for est in estudiantes:
        prom = calcular_promedio(est['notas'])

        estado = "Aprobado" if prom >= 3.0 else "Reprobado"
        print(f"Estudiantes: {est['nombre']} | Estado: {estado}")

if __name__ == "__main__":
    generar_reporte(estudiantes)