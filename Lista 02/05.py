'''
Crie um algoritmo que leia três números e mostre-os em ordem crescente.
'''

lista = []
lista.append(int(input('Digite o primeiro numero: ')))
lista.append(int(input('Digite o segundo numero: ')))
lista.append(int(input('Digite o terceiro numero: ')))
lista.sort()

print(lista)