##
# atividade 37
# aluno: Apollo
# Data: 24/03/2024
##Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.

segundos = float(input("Digite um valor inteiro em segundos: "))

horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(f"{horas} horas, {minutos} minutos e {segundos} segundos.")