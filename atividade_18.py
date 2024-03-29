##
# atividade 18
# aluno: Apollo
# Data: 24/03/2024
##

notag1 = float(input("Digite a nota da G1: "))
notag2 = float(input("Digite a nota da G2: "))

media_semestre = (notag1 + notag2 * 2) / 3
if media_semestre >= 7.0:
    print("aprovado")
else:
    print("reprovado")
print(f"Media do semestre: {media_semestre:.2f}")