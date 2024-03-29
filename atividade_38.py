##
# atividade 38
# aluno: Apollo
# Data: 24/03/2024
##Faça um programa que leia o horário (hora, minuto e segundo) do início e a duração em segundo, de uma experiência atômica bélica. O programa deve resultar com onovo horário (hora, minuto e segundo) do término da mesma.

# Solicitar informações do usuário
hora = int(input("Digite a hora de inicio: "))
minuto = int(input("Digite o minuto de inicio: "))
segundo = int(input("Digite o segundo de inicio: "))
duracao = int(input("Digite a duracao em segundos: "))


TotalSegundos = hora * 3600 + minuto * 60 + segundo
TotalSegundos2 = TotalSegundos + duracao
HoraFinal = TotalSegundos2 // 3600
MinutosFaltantes = TotalSegundos2 % 3600
MinutosFinais= MinutosFaltantes // 60
SegundosFinais = MinutosFaltantes % 60

print(f"O novo horário de término é: {HoraFinal:02d}:{MinutosFinais:02d}:{SegundosFinais:02d}")

