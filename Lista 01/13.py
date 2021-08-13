# Exercicio 13
'''
Crie um algoritmo que calcule o volume de uma caixa d’água cilíndrica,
sendo que os comprimentos do raio e a altura são informados pelo usuário.
O volume é calculado multiplicando-se pi, o raio ao quadrado e a altura.
'''

def volumeCilindro (raio, altura):
    volumeCilindro = altura * 3.141592 * raio**2
    volumeCilindro= round(volumeCilindro,2)
    return volumeCilindro

raio = float( input('Informe o valor do raio do reservatorio: '))
altura = float( input('Informe o valor da altura do reservatorio: '))
print(f'O volume calculado para o reservatorio de agua co raio {raio} '
      f'e altura {altura} e de : {volumeCilindro(raio, altura)} u.v.')