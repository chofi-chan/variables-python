# PRIMER PUNTO DE LA TAREA
# Define una variable de cada tipo de primitivo
entero = 42
flotante = 3.14
cadena = "Hola, soy sofia"
booleano = True

# Concatena la cadena con las otras variables
cadena_resultado = cadena + " El valor del entero es: " + str(entero) + ", el valor del flotante es: " + str(flotante) + ", y el valor del booleano es: " + str(booleano)

#SEGUNDO PUNTO
#Enteros (int):
#En versiones de Python 3.x, los enteros son de precisión arbitraria, lo que significa que pueden crecer hasta el límite de memoria disponible en tu sistema. No hay un límite teórico para su tamaño. Esto es una ventaja significativa en comparación con algunos lenguajes de programación donde los enteros tienen un tamaño fijo (por ejemplo, 32 bits o 64 bits).

#Flotantes (float):
#Los números de punto flotante en Python se basan en el estándar de punto flotante IEEE 754 de doble precisión (64 bits). Por lo tanto, en la mayoría de las implementaciones de Python, el límite para los flotantes es aproximadamente ±1.797693e+308 para números cercanos a cero. Los flotantes también tienen un valor mínimo positivo cercano a cero, que es aproximadamente 5e-324.
 
#TERCER PUNTO
n = 4  
suma_pares = n * (n + 1)

#CUARTO PUNTO
# Imprimir los resultados de las tareas anteriores
print("Valor de la cadena concatenada:", cadena_resultado)
print("Suma de los primeros n números pares:", suma_pares)

