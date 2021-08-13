# Crie um algoritmo que calcule e mostre o novo valor de um salário
# a partir das seguintes regras: salários de até R$ 1.000,00 inclusive
# recebem 30% de aumento, salários de até R$ 2.000,00 inclusive recebem 25%,
# salários de até R$ 3.000,00 inclusive recebem 20%, salários de até R$ 4.000,00
# inclusive recebem 15% e salários acima de R$ 4.000,00 recebem 10%.

aumento = [30, 25, 20, 15, 10]
limites = [1000, 2000, 3000, 4000]
salario = float(input('Inform seu salario: '))
novoSalario = 0

if salario <= limites[0]:
    novoSalario = salario*(1 + aumento[0]/100)

elif salario <= limites[1]:
    novoSalario = salario * (1 + aumento[1] / 100)

elif salario <= limites[2]:
    novoSalario = salario * (1 + aumento[2] / 100)

elif salario <= limites[3]:
    novoSalario = salario * (1 + aumento[3] / 100)

else:
    if salario > limites[3]:
        novoSalario = salario * (1 + aumento[4] / 100)

novoSalario = round(novoSalario, 2)
print(f'O novo salario calculado e de: R${novoSalario}')
