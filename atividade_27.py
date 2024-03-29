##
# atividade 27
# aluno: Apollo
# Data: 24/03/2024
#Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um monstruoso aumento de 1.77%.

SalarioAtual = float(input("Digite o salário atual do funcionário: "))
aumento = SalarioAtual * 0.0177
NovoSalario = SalarioAtual + aumento

print(f"O novo salário é: R${NovoSalario:.2f}")
