##
# atividade 36
# aluno: Apollo
# Data: 24/03/2024
##Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.

numero = float(input("Digite um numero inteiro de 4 digitos entre 1000 e 9999: "))

milhar = numero // 1000
centena = numero // 100 % 10
dezena = numero // 10 % 10
unidade = numero % 10

print(milhar)
print(centena)
print(dezena)
print(unidade)
