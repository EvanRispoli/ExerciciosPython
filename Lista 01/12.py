#Exercicio 12

'''
Crie um algoritmo que calcule a área de uma esfera,
sendo que o comprimento do raio é informado pelo usuário.
A área da esfera é calculada multiplicando-se 4 vezes pi e o raio ao quadrado.
'''
import math


def areaEsfera (raio):
    areaEsfera = 4 * math.pi * raio**2
    areaEsfera= round(areaEsfera,2)
    return areaEsfera

raio = float( input('Informe o valor do raio da esfera: '))
print(f'A area da esfera de raio {raio} mede : {areaEsfera(raio)} u.m.')