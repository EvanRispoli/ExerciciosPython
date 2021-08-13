# Exercicio 8
# Crie um algoritmo que calcule o novo valor de um salário a partir de um
# valor percentual de reajuste. O valor atual do salário e o valor percentual
# do reajuste devem ser informados pelo usuário como, por exemplo, 7,3%

def novoSalario(a, b):
    novoSalario = salario * (1 + reajuste/100)
    novoSalario = round(novoSalario, 2)
    return novoSalario


salario = float(input('Informe o salario atual : '))
reajuste = float(input('Informe o percentual de reajuste: '))

print(f' O valor do salario reajustado e de: {novoSalario(salario, reajuste)}')
