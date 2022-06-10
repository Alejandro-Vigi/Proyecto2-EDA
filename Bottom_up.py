"""
 * @brief Realizado el 06/06/2022
 * Osnaya Martinez Emmanuel
 * Palacios Barcelos Juan Antonio
 * Romero Molina David
 * Vigi Garduño Marco Alejandro
"""


"""
 * @brief Funcion que calcula el fibonacci
 * @param numero recibe un numero
 * @return f2 al finalizar
 """
 
def fibonacci_iterativo_v1(numero):
    f1=0
    f2=1
    tmp=0
    for i in range(1,numero-1):
        tmp = f1+f2
        f1=f2
        f2=tmp
    return f2

#Prueba de impresion
print(fibonacci_iterativo_v1(6))