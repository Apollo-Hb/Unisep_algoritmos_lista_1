##
# atividade 44
# aluno: Apollo
# Data: 24/03/2024
##Elabore um algoritmo para calcular e imprimir o salário do vendedor num dado mês recebendo como dados de entrada o nome do vendedor, o número de carros vendidos e o valor total das vendas.

nome_vendedor = input("Informe o nome do vendedor: ")
num_carros_vendidos = float(input("Informe o número de carros vendidos: "))
valor_total_vendas = float(input("Informe o valor total das vendas: "))

salario = 500.00
comissao_por_carro = 50.00
comissao_por_venda = 0.05 * valor_total_vendas

salario_total = salario + (comissao_por_carro * num_carros_vendidos) + comissao_por_venda

print(f"salario total: {salario_total:.2f}")