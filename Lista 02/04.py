'''
Crie um algoritmo que leia três números e mostre o maior número.
👼 Desconsidere a hipótese de números iguais
😈 Considere-a, para um problema mais difícil.

'''

lista = []
lista.append(int(input('Digite o primeiro numero: ')))
lista.append(int(input('Digite o segundo numero: ')))
lista.append(int(input('Digite o terceiro numero: ')))
lista.sort()

#print(lista[len(lista)-1])
print(f'O maior numero digitado foi  {max(lista)}')

