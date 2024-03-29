# atividade 30
# aluno: Apollo
# Data: 24/03/2024
##Faça um programa que leia o valor da hora de trabalho em reais e número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobreo valor calculado.




valor_hora = float(input("Digite o valor da hora de trabalho em reais: "))
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mes: "))

salario_bruto = valor_hora * horas_trabalhadas
acrescimo = salario_bruto * 0.10
salario_liquido = salario_bruto + acrescimo

print(f"O valor a ser pago ao funcionario eh: R${salario_liquido:.2f}")
