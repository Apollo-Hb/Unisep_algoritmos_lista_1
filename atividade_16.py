##
# atividade 16
# aluno: Apollo
# Data: 24/03/2024
##Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três números lidos.
num1 = float(input("Digite um numero:"))
num2 = float(input("Digite um segundo numero:"))
num3 = float(input("Digite um terceiro numero:"))


Valor1 = num1 ** 2
valor2 = num2 ** 2
valor3 = num3 ** 2
valores = Valor1 + valor2 + valor3

print(f"A soma dos quadrados dos tres numeros eh: {valores:.2f}")