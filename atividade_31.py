##
# atividade 31
# aluno: Apollo
# Data: 24/03/2024
##Receba o salário-base de um funcionário. Calcule e imprima o salário a receber,sabendo-se que esse funcionário em uma gratificação de 5% sobre o salário-base.Além disso, ele paga 7% de imposto sobre o salário-base.



salario_base = float(input("Digite o salario base do funcionario: "))

gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_receber = salario_base + gratificacao - imposto

print(f"O salário a receber é: R${salario_receber:.2f}")
