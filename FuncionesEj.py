frutas = [
    {'fruta': 'Manzana', 'niveles': [8, 9, 7, 10, 8]},
    {'fruta': 'Pera', 'niveles': [5, 4, 6, 5, 5]},
    {'fruta': 'Mango', 'niveles': [9, 8, 9, 10, 7]}
]

print("---BASE DE DATOS CARGADA---")
print(f"Total de frutas en stock: {len(frutas)}")

def calcular_promedio(lista_calidad):
    """ Calcula el promedio de una lista de floats """
    if len(lista_calidad) == 0:
        return 0
    suma = 0
    for i in lista_calidad:
        suma += i 
    return suma / len(lista_calidad)

# Prueba de promedio para la primera fruta (Manzana)
print("Prueba promedio Manzana: ", calcular_promedio(frutas[0]['niveles']))

def generar_reporte():
    print("\n--- REPORTE FINAL DE CALIDAD ---\n")
    for f in frutas:
        prom = calcular_promedio(f['niveles'])

        # Lógica de clasificación similar a Aprobado/Reprobado
        estado = "Exportación" if prom >= 7.0 else "Venta Local"
        
        print(f"Fruta: {f['fruta']} | Calidad: {prom:.1f} | Estado: {estado}")

if __name__ == "__main__":
    generar_reporte()