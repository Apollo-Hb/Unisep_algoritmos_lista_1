##
# atividade 32
# aluno: Apollo
# Data: 24/03/2024
##Escreva um programa de ajuda para vendedor.

valor_total = float(input("Digite o valor total da venda: "))

desconto = valor_total * 0.10
valor_com_desconto = valor_total - desconto
parcelas = 3
valor_parcela = valor_total / parcelas
comissao_vista = valor_com_desconto * 0.05
comissao_parcelada = valor_total * 0.05

print(f"Total a pagar com desconto de 10%: R${valor_com_desconto:.2f}")
print(f"Valor de cada parcela 3x sem juros: R${valor_parcela:.2f}")
print(f"Comissao do vendedor venda a vista: R${comissao_vista:.2f}")
print(f"Comissao do vendedor venda parcelada: R${comissao_parcelada:.2f}")
