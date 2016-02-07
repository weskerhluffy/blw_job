'''
Created on 06/02/2016

@author: ernesto
problema: https://www.hackerrank.com/challenges/the-indian-job
'''
import logging
import array
import fileinput
#nivel_log = logging.DEBUG
nivel_log = logging.ERROR
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
    
    numeros_ordenados = numeros
    
    logger_cagada.debug("los numeros ordenados %s" % numeros_ordenados)
    
    for suma_actual in range(suma + 1):
        for idx_num_actual, numero_actual in enumerate(numeros_ordenados, start=1):
            matrix_posiblidades[suma_actual][idx_num_actual] = matrix_posiblidades[suma_actual][idx_num_actual - 1]
            if(numero_actual <= suma_actual):
                matrix_posiblidades[suma_actual][idx_num_actual] |= matrix_posiblidades[suma_actual - numero_actual][idx_num_actual - 1]
    
    logger_cagada.debug("la matrix de posiblidades\n%s" % imprime_matrix(matrix_posiblidades, buf))
    
    return matrix_posiblidades[suma][num_numeros]

def blw_job_main(necesidades_rateros, siesta_guardia):
    total_necedades_rat = 0
    minimo_formable = 0
    
    total_necedades_rat = sum(necesidades_rateros)
    
    if(total_necedades_rat > siesta_guardia * 2):
        return False
    
    if(necesidades_rateros[-1] > siesta_guardia):
        return False
    
    minimo_formable = total_necedades_rat - siesta_guardia
    
    logger_cagada.debug("lo minimo q c debe poder formar es %u" % minimo_formable)
    
    for num_prueba_formable in reversed(list(range(minimo_formable, siesta_guardia + 1))):
        resultado = False
        logger_cagada.debug("probando si %u se puede formar" % num_prueba_formable)
        resultado = es_suma_posible(necesidades_rateros, num_prueba_formable)
        logger_cagada.debug("con suma %u c pudo? %s" % (num_prueba_formable, resultado))
        if(resultado):
            return True
        
    return False
        
    

if __name__ == '__main__':
    resultado = False
    suma = 0
    num_casos_uso = 0
    num_ladronzuelos = 0
    siesta_guardia = 0
    num_linea = 0
    necesidades_rateros = array.array("I")
    linea = []
    
    
    logging.basicConfig(level=nivel_log)
    logger_cagada = logging.getLogger("asa")
    logger_cagada.setLevel(nivel_log)
    
    lineas = list(fileinput.input())
    
    num_casos_uso = int(lineas[0])
    
    num_linea = 1
    for _ in range(num_casos_uso):
        necesidades_rateros = array.array("I")
        
        (num_ladronzuelos, siesta_guardia) = [int(x.strip()) for x in lineas[num_linea].split(" ")]
        num_linea += 1
        necesidades_rateros.extend(sorted([int(x.strip()) for x in lineas[num_linea].split(" ")]))
        num_linea += 1
        assert(num_ladronzuelos == len(necesidades_rateros))
        logger_cagada.debug("el num de ladrones %u, la siesta del guardia %u" % (num_ladronzuelos, siesta_guardia))
        logger_cagada.debug("las necesidades d los rateros %s" % necesidades_rateros)
    
        resultado = blw_job_main(necesidades_rateros, siesta_guardia)
    
        logger_cagada.debug("la cagada es %s" % resultado)
        
        if(resultado):
            print("YES")
        else:
            print("NO")
    
    