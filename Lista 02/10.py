#  Crie um algoritmo que valide uma data, formada por dia, mês e ano.
#  Por exemplo, a data 30/02 é sempre inválida; mas a data 29/02/2012 é válida.

from datetime import datetime

def data_valida(data):
    try:
        datetime.strptime(data, '%d/%m/%Y')
        return "Data valida"
    except ValueError:
        return "Data invalida"

data = input("Digite uma data: ")
print(data_valida(data))
