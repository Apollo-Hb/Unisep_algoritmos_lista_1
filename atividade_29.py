##
# atividade 29
# aluno: Apollo
# Data: 24/03/2024
##


dias_trabalhados = float(input("Digite o numero de dias trabalhados: "))
valor_diario = 30.00
salario = dias_trabalhados * valor_diario
previdencia_social = salario * 0.11
imposto_renda = salario * 0.08
salario_liquido = salario - (previdencia_social + imposto_renda)

print(f"Desconto de Previdencia Social: R${previdencia_social:.2f}")
print(f"Desconto de Imposto de Renda: R${imposto_renda:.2f}")
print(f"Salario liquido: R${salario_liquido:.2f}")