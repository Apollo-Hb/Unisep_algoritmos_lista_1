##
# atividade 35
# aluno: Apollo
# Data: 24/03/2024
##Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).Gere outro numero formado pelos dígitos invertidos do número lido. 

numero_lido = float(input("Digite um numero inteiro de tres digitos entre 100 e 999: "))

centenas = numero_lido // 100
dezenas = numero_lido // 10 % 10
unidades = numero_lido % 10
numero_gerado = unidades * 100 + dezenas * 10 + centenas

print(f"Numero gerado: {numero_gerado}")
