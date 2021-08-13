# (Python Brasil) Faça um Programa para um caixa eletrônico. O programa deverá perguntar
# ao usuário o valor do saque e depois informar quantas notas de cada valor serão fornecidas.
# As notas disponíveis serão as de 1, 2, 5, 10, 20, 50 e 100, 200 reais. O valor mínimo é de
# 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
# existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
# uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100,
# uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

cedulas = [200,100, 50, 20, 10, 5, 2, 1]
min_saque = 10
max_saque = 600
valor = 0

while valor < min_saque or valor > max_saque:
  valor = int(input(f"Informe um valor entre {min_saque} e {max_saque}: "))
  if valor < min_saque or valor > max_saque:
    print("Valor inválido.")

i = 0 # índice da lista de cédulas
while valor > 0:
  cedula = cedulas[i] # Pelo índice, vejo que tipo de cédula vou usar
  num_cedulas = int(valor/cedula) # retorna sempre a parte inteira do valor.
  if num_cedulas > 0:
    print(f"{num_cedulas} cédula(s) de R${cedula}.")
    # Calcular quanto falta:
    valor = valor % cedula # Cálculo via resto da divisão
  # Também seria possível calcular assim:
  # valor = valor - num_cedulas * cedula
  # print(f"Agora, faltam R${valor}.")
  i += 1
