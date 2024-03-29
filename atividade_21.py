##
# atividade 20
# aluno: Apollo
# Data: 24/03/2024
##Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro

numero = int(input("Digite um número inteiro: "))

triplo = 3 * numero
dobro = 2 * numero
sucessor_triplo = triplo + 1
antecessor_dobro = dobro - 1
soma = sucessor_triplo + antecessor_dobro

print(f"A soma do sucessor do triplo com o antecessor do dobro eh. {soma}")

