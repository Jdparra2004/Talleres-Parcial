import numpy as np
import scipy
from scipy.stats import uniform

# Parámetros del problema
l_min, l_max = 1, 3
t1_min, t1_max = 2, 4
t2_min, t2_max = 3, 5
valor_oferta = 1300000
costo_agente = 72000
costo_otros = 0.3 * valor_oferta
dias_en_un_mes = 30
num_simulaciones = 1000

# Función para simular la llegada de cotizaciones y el tiempo de respuesta de los agentes
def simular_cotizaciones(l_min, l_max, t1_min, t1_max, t2_min, t2_max, dias_en_un_mes):
    # Distribuciones de probabilidad para la llegada de cotizaciones y el tiempo de respuesta de los agentes
    llegada = uniform.rvs(l_min, l_max, size=dias_en_un_mes)
    tiempo_respuesta1 = uniform.rvs(t1_min, t1_max, size=dias_en_un_mes)
    tiempo_respuesta2 = uniform.rvs(t2_min, t2_max, size=dias_en_un_mes)

    # Número de cotizaciones solicitadas durante el mes
    cantidad_cotizaciones = np.sum(np.diff(np.append(0, np.argwhere(np.cumsum(llegada) <= dias_en_un_mes)), axis=0) == 1)

    # Tiempo de respuesta de cada cotización
    tiempo_respuesta = np.minimum(tiempo_respuesta1, tiempo_respuesta2)

    # Costo de cada cotización
    costo_cotizacion = costo_agente * 2 + costo_otros * valor_oferta / (tiempo_respuesta * 1000)

    # Utilidad bruta
    utilidad_bruta = (valor_oferta - costo_cotizacion) * cantidad_cotizaciones

    return utilidad_bruta

# Simulación de la llegada de cotizaciones y el tiempo de respuesta de los agentes
utilidades_brutas = np.zeros(num_simulaciones)
for i in range(num_simulaciones):
    utilidades_brutas[i] = simular_cotizaciones(l_min, l_max, t1_min, t1_max, t2_min, t2_max, dias_en_un_mes)

# Estadísticas de la utilidad bruta
utilidad_bruta_promedio = np.mean(utilidades_brutas)
utilidad_bruta_desviacion_estandar = np.std(utilidades_brutas)

# Resultados
print("Cantidad de cotizaciones solicitadas durante un mes: ", np.mean(utilidades_brutas) / valor_oferta)
print("Utilidad bruta asociada a un mes de operación: ")
print("Promedio: ", utilidad_bruta_promedio)
print("Desviación estándar: ", utilidad_bruta_desviacion_estandar)