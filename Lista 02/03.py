'''
Crie um algoritmo que leia dois números e mostre o maior número.
'''

x = float(input('Informe o primeiro numero: '))
y = float(input('Informe o segundo numero: '))
if x > y:
    print(f'O maior numero e {x}')

elif x == y :
    print('Os dois numeros sao iguais')

else:
    print(f'O maior numero e {y}')