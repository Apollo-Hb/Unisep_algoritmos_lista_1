##
# atividade 42
# aluno: Apollo
# Data: 24/03/2024
##. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a porcentagem do distribuidor e dos impostos, ambos aplicados ao custo de fábrica.Supondo que a porcentagem do distribuidor seja de 12% e a dos impostos de 45%,prepare um algoritmo para ler o custo de fábrica do carro e imprimir o custo ao consumidor.

Custo = float(input("Digite um valor do custo de fabrica de um carro:" ))
distribuidor = Custo * 0.12
impostos = Custo * 0.45
Custo_consumidor = Custo + distribuidor + impostos
print(f"O custo para o consumidor final eh: {Custo_consumidor:.2f}")
