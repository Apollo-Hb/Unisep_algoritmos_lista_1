##
# atividade 26
# aluno: Apollo
# Data: 24/03/2024
#Faça um programa que leia o valor de um produto e imprima o valor com desconto,tendo em vista que o desconto foi de 12%. 

valorDoproduto = float(input("Digite o valor do produto: "))
desconto = valorDoproduto * 0.12
valorComdesconto = valorDoproduto - desconto

print(f"O valor com desconto é: R${valorComdesconto:.2f}")


