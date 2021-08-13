# Recrie o algoritmo de cálculo de média das notas, mas, desta vez, calcule a média ponderada,
# sabendo que a primeira  nota possui peso 1, a segunda nota possui peso 2 e a terceira nota
# possui peso 3.

def media_ponderada(nota1, peso1, nota2, peso2, nota3, peso3):
    media_ponderada = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3)/(peso1 + peso2 + peso3)
    return media_ponderada

nota1 = float(input('Informe a primeira nota do aluno: '))
peso1 = int(input("Digite o peso da primeira nota "))
nota2 = float(input("Digite a segunda nota do aluno: "))
peso2 = int(input("Digite o peso da segunda nota: "))
nota3 = float(input('Digite a terceira nota do aluno: '))
peso3 = int(input("Digite o peso da terceira nota "))

print(f'A media ponderada das notas do aluno e : {round(media_ponderada(nota1, peso1, nota2, peso2,nota3, peso3), 2)}')