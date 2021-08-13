# Crie um algoritmo que receba um número inteiro, que representa um determinado mês do ano,
# e mostre o nome do mês correspondente. Por exemplo, se for informado o número 2, algoritmo
# deverá exibir fevereiro. O algoritmo deve validar se a entrada está correta.

month = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

numeroMes = int(input("Digite o número do mês desejado: "))

print(month[numeroMes-1])


