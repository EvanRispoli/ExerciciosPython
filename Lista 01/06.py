#Exercicio 6
# Crie um algoritmo para calcular a média de duas notas
# digitadas pelo usuário, sendo que a segunda nota tem peso dois.

def media_ponderada(nota1, nota2, peso):
    media_ponderada = (nota1 + nota2 * peso )/(peso)
    media_ponderada = round(media_ponderada, 2)
    return media_ponderada


nota1 = float(input('Informe a primeira nota do aluno: '))
nota2 = float(input("Digite a segunda nota do aluno: "))
peso = int(input("Digite o peso da segunda nota: "))

print(f'A media ponderada das notas do aluno e : {media_ponderada(nota1, nota2, peso)}')
