# Exercicio 11
'''
Crie um algoritmo que calcule a área de um círculo,
sendo que o comprimento do raio é informado pelo usuário.
A área do círculo é calculada multiplicando-se pi e o raio ao quadrado.
'''

def areaCirculo (raio):
    areaCirculo = 3.141592 * raio**2
    areaCirculo= round(areaCirculo,2)
    return areaCirculo

raio = float( input('Informe o valor do raio do circulo: '))
print(f'A area do circulo de raio {raio} mede : {areaCirculo(raio)} u.m.')