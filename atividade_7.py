###
# atividade 7
# aluno: Apollo
# Data: 18/03/2024
##Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.

F = float(input("Digite a temperatura em Fahrenheit: "))
C = (F - 32) * 5 / 9
print(f"A temperatura em Celsius é: {C:.2f}°C")
