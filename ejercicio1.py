from pprint import pprint

# Caso 1: Lista de Listas

notas = [
    ["Calculo", 3.5, 2.5, 1.5],
    ["Quimica", 2.5, 3.0, 5.0],
    ["Deporte", 2.4, 2.0, 2.2],
    ["Logica", 1.5, 4.0, 4.5]
]

# 1.1 Calcula la nota final de cada materia (30%, 30% y 40%),
# y agregue el valor a los datos
def c11_final():
    global notas
    for i in range(len(notas)):
        nota1 = notas[i][1]*0.3 
        nota2 = notas[i][2]*0.3
        nota3 = notas[i][3]*0.4
        nota_final = nota1 + nota2 + nota3
        notas[i].append(nota_final)

# 1.2 Calcule el promedio de las notas del Estudiante
def c12_promedio():
    global notas
    suma_notas = 0
    for i in range(len(notas)):
        suma_notas += notas[i][4]
    print("El promedio de las notas del estudiante es de : ", suma_notas/len(notas))
    pass

# LLamar funciones, y mostrar Resultados
print("------------------- Punto 1 -------------------")
c11_final()
c12_promedio()
##########################################################
#Caso 2 Diccionario de Listas


notas = {
    "Calculo": [3.5, 2.5, 1.5],
    "Quimica": [2.5, 3.0, 5.0],
    "Deporte": [2.4, 2.0, 2.2],
    "Logica": [1.5, 4.0, 4.5]
}

# 2.1 Calcula la nota final de cada materia (30%, 30% y 40%),
# y agregue el valor a los datos
def c21_final():
    global notas
    for key, value in notas.items():
        nota1 = value[0]*0.3
        nota2 = value[1]*0.3
        nota3 = value[2]*0.4
        nota_final = nota1 + nota2 + nota3
        notas[key].append(nota_final) 

# 2.2 Calcule el promedio de las notas del Estudiante
def c22_promedio():
    global notas
    suma_notas = 0 
    for key, value in notas.items():
        suma_notas += value[3]
    print("El promedio de las notas del estudiante es de : ", suma_notas/len(notas))
#Llamar funciones, y mostrar Resultados
print("------------------- Punto 2 -------------------")
c21_final()
c22_promedio()