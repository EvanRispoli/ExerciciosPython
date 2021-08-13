# Exercicio 1
# Crie um algoritmo que receba, como entrada, o valor de três notas de um aluno -
# com valor entre 0 e 10, e, em seguida, informe a média entre elas.

def media_notas(nota1, nota2, nota3):
    media_notas = (nota1+nota2+nota3)/3
    media_notas = round(media_notas,2)
    return media_notas

nota1 = float(input('informe a primeira nota do aluno: '))
nota2 = float(input('informe a segunda nota do aluno: '))
nota3 = float(input('informe a receira nota do aluno: '))

print(f'A media de notas do aluno e: {media_notas(nota1, nota2,nota3)}')

