
# Exercicio 3
# Crie um algoritmo que recebe o valor da altura e do peso de uma pessoa e retorna seu IMC.
peso = float(input("Informe seu peso em quilogramas: "))
altura = float(input("Informe sua altura em metros: "))
imc = (peso/altura**2)
imc = round(imc,2)
print(f"O seu imc e de {imc}")
