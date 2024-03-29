##
# atividade 40
# aluno: Apollo
# Data: 24/03/2024
##Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartidoroporcionalmente ao valor que cada um deu para a realização da aposta. Faça u mprograma que leia quanto cada apostador investiu, o valor do prêmio, e imprima uanto cada um ganharia do prêmio com base no valor investido.

amigo1 = float(input("Digite o valor pago pelo primeiro amigo: "))
amigo2 = float(input("Digite o valor pago pelo segundo amigo: "))
amigo3 = float(input("Digite o valor pago pelo terceiro amigo: "))
premio = float(input("Digite o valor total do prêmio: "))

total_pago = amigo1 + amigo2 + amigo3
parteamigo1 = amigo1 / total_pago
parteamigo2 = amigo2 / total_pago
parteamigo3 = amigo3 / total_pago
valoramigo1 = parteamigo1 * premio
valoramigo2 = parteamigo2 * premio
valoramigo3 = parteamigo3 * premio

print(f"Amigo 1 iria ganhar: R${valoramigo1:.2f}")
print(f"Amigo 2 iria ganhar: R${valoramigo2:.2f}")
print(f"Amigo 3 iria ganhar: R${valoramigo3:.2f}")