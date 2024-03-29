##
# atividade 43
# aluno: Apollo
# Data: 24/03/2024
##O cardápio de uma lanchonete é dado abaixo. Prepare um algoritmo que leia a quantidade de cada item que você consumiu e calcule a conta final.

QH = float(input("Digite a quantidade de hamburguer:" ))
QC = float(input("Digite a quantidade de chessehamburguer:" ))
QF = float(input("Digite a quantidade de fritas:" ))
QR = float(input("Digite a quantidade de refrigerante:" ))
QM = float(input("Digite a quantidade de milkshake:" ))
Total = (QH * 3.00) + (QC * 2.50) + (QF * 2.50) + (QR * 1.00) + (QM * 3.00)
print(f"o valor total da conta: {Total:.2f}")