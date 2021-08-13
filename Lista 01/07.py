# Exercicio 7
# Crie um algoritmo que calcule a gorjeta a ser paga de
# uma conta de restaurante. A gorjeta é calculada como sendo
# 10% do valor da conta, que deve ser informado pelo usuário.

def valor_gorjeta ( valor_conta, gorjeta):
    valor_gorjeta = valor_conta * gorjeta
    return valor_gorjeta

valor_conta = float(input("Informe o valor da conta: "))
gorjeta = 0.1

print(f'O valor da gorjeta e de: {valor_gorjeta(valor_conta, gorjeta)} reais')
