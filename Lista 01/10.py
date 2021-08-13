# Exercicio 10
# Crie um algoritmo que calcule a área de um retângulo,
# sendo que os comprimentos da altura e da base são informados pelo usuário.
# A área do retângulo é calculada multiplicando-se a altura pela base.

def areaRetangulo (base, altura):
    areaRetangulo = base * altura
    areaRetangulo = round(areaRetangulo, 2)
    return areaRetangulo

base = float(input('Informe o valor da base do retangulo: '))
altura = float(input('Informe o valor da altura do retangulo: '))

print(f'A area do retangulo e de {areaRetangulo(base, altura)} u.m.')