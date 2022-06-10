"""
 * @brief Realizado el 06/06/2022
 * Osnaya Martinez Emmanuel
 * Palacios Barcelos Juan Antonio
 * Romero Molina David
 * Vigi Garduño Marco Alejandro
"""

#Memoria inicial
memoria = {1:0, 2:1, 3:1}

"""
 * @brief Funcion que calcula el fibonacci
 * @param numero recibe un numero
 * @return f2 al finalizar
 """
 
 
def fibonacci_iterativo_v2(numero):
    f1=0
    f2=1
    for i in range(1, numero-1):
        f1,f2=f2,f1+f2    #Asignación paralela
    return f2 


"""
 * @brief Funcion que calcula el fibonacci mediante top-down
 * @param numero recibe un numero
 * @return memoria[numero] al finalizar
 """
 
 
def fibonacci_top_down(numero):
    if numero in memoria:      #Si el número ya se encuentra calculado, se regresa el valor ya ya no se hacen más cálculos
        return memoria[numero]
    f = fibonacci_iterativo_v2(numero-1) + fibonacci_iterativo_v2(numero-2)
    memoria[numero] = f
    return memoria[numero]

#Prueba de impresion
print(fibonacci_top_down(12))