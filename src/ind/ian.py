'''
Created on 06/02/2016

@author: ernesto
problema: https://www.hackerrank.com/challenges/the-indian-job
'''
import logging
import array
nivel_log = logging.DEBUG
logger_cagada = None
    
def imprime_matrix(matrix, buf):    
    for fila in matrix:
        for elem in fila:
            buf += ("%s\t" % elem)
        buf += ("\n")
    return buf
    
def es_suma_posible(numeros, suma):
    num_numeros = 0
    numeros_ordenados = []
    matrix_posiblidades = None
    buf = ""
    
    num_numeros = len(numeros)
    
    matrix_posiblidades = [ [ False for i in range(num_numeros + 1) ] for j in range(suma + 1) ]

    matrix_posiblidades[0][:] = [True] * (num_numeros + 1)
    matrix_posiblidades[:][0] = [False] * (suma + 1)
    
    numeros_ordenados = sorted(numeros)
    
    logger_cagada.debug("los numeros ordenados %s" % numeros_ordenados)
    
    for suma_actual in range(suma + 1):
        for idx_num_actual, numero_actual in enumerate(numeros_ordenados, start=1):
            matrix_posiblidades[suma_actual][idx_num_actual] = matrix_posiblidades[suma_actual][idx_num_actual - 1]
            if(numero_actual <= suma_actual):
                matrix_posiblidades[suma_actual][idx_num_actual] |= matrix_posiblidades[suma_actual - numero_actual][idx_num_actual - 1]
    
    logger_cagada.debug("la matrix de posiblidades\n%s" % imprime_matrix(matrix_posiblidades, buf))
    
    return matrix_posiblidades[suma][num_numeros]

if __name__ == '__main__':
    numeros = array.array("I", [3, 34, 4, 12, 5, 2])
    suma = 15
    resultado = False
    
    logging.basicConfig(level=nivel_log)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    
    resultado = es_suma_posible(numeros, suma)
    
    logger_cagada.debug("la cagada es %s" % resultado)
    
    
    print("caca")
