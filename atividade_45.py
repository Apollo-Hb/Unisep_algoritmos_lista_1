##
# atividade 45
# aluno: Apollo
# Data: 24/03/2024
##Para isso solicite o nome do aluno, a nota da prova e a nota qualitativa. Sabe-se que a nota da prova tem peso 2 e a nota qualitativa peso 1. Mostre a média como resultado.

nome = float(input("Digite o nome do aluno: "))
nota_prova = float(input("Digite a nota da prova: "))
nota_qualitativa = float(input("Digite a nota qualitativa: "))

media = (2 * nota_prova + 1 * nota_qualitativa) / 3

print(f"A media do aluno, na disciplina de ED eh: {media:.2f}")