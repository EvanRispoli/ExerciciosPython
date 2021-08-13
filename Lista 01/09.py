# Exercicio 9
# Crie um algoritmo que calcule a área de um quadrado,
# sendo que o comprimento do lado é informado pelo usuário.
# A área do quadrado é calculada elevando-se o lado ao quadrado.

def areaQuadrado (lado):
    areaQuadrado = lado**2
    areaQuadrado = round(areaQuadrado, 2)
    return areaQuadrado

lado = float(input('Informe o comprimento do lado do quadrado: '))

print(f'A area do quadrado e de {areaQuadrado(lado)} u.m.')