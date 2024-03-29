##
# atividade 28
# aluno: Apollo
# Data: 24/03/2024
##

PremioTotal = 780000.00
primeiro_ganhador = 0.46 * PremioTotal
segundo_ganhador = 0.32 * PremioTotal
terceiro_ganhador = PremioTotal - (primeiro_ganhador + segundo_ganhador)

print(f"Valor do prêmio para o primeiro ganhador: R${primeiro_ganhador:.2f}")
print(f"Valor do prêmio para o segundo ganhador: R${segundo_ganhador:.2f}")
print(f"Valor do prêmio para o terceiro ganhador: R${terceiro_ganhador:.2f}")
