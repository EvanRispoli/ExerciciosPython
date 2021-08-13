# Exercicio 5
# Um motorista deseja abastecer um valor X em reais, de combustível.
# Escreva um algoritmo para ler o preço do litro do combustível e o
# valor que o motorista deseja abastecer. Em seguida, informe quantos
# litros foram abastecidos.

def converte_valor (valor_desejado, preco_combusivel):
    converte_valor = valor_desejado / preco_combusivel
    converte_valor = round(converte_valor,2)
    return converte_valor

valor_desejado = float(input("Informe o valor para realizar o pagamento: "))
preco_combustivel = float(input("Informe o preco do combustivel : "))

print(f'A quantidade de combustivel abasteceido e de {converte_valor(valor_desejado, preco_combustivel)} litros')