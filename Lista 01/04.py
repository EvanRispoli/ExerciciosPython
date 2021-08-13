# Exercicio 4
# Crie um algoritmo que recebe um valor de temperatura em Celsius e o converte para Fahrenheit.

def converte_temperatura(celsius):
    converte_temperatura = (celsius*9/5 +32)
    converte_temperatura = round(converte_temperatura,2)
    return converte_temperatura

celsius = float(input("Digite o a temperatura em Celsius: "))
print(f"a temperatura de {celsius} graus celcius e : {converte_temperatura(celsius)} Fahrenheit")