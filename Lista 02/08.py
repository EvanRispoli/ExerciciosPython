# Os endereços IP versão 4 são divididos em cinco classes: A, B, C, D e E.
# Os endereços no intervalo de 0 a 127 são classe A, de 128 a 191 são classe B,
# de 192 a 223 são classe C, de 224 a 239 são classe D e a partir de 240 são classe E.
# Crie um algoritmo que leia o primeiro octeto, no formato decimal, de um endereço IP e informe a sua classe.

classes = ["A", "B", "C", "D","E"]
banda = [127, 191, 223, 239,255 ]

endereco = input('informe o endereco de IP: ')

endereco = endereco[0] + endereco[1] + endereco[2]
endereco = int(endereco)

if endereco <= banda[0]:
    ip = classes[0]

elif endereco <= banda[1]:
    ip = classes[1]

elif endereco <= banda[2]:
    ip = classes[2]

elif endereco <= banda[3]:
    ip = classes[3]

else:
    ip = classes[4]

print(f'A classe do IP informado e: {ip}')


