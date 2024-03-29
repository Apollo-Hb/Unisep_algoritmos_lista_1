##
# atividade 33
# aluno: Apollo
# Data: 24/03/2024
##Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.

alturadegrau = float(input("Digite a altura do degrau: "))
alturadesejada = float(input("Digite a altura desejada: "))

numdegraus = alturadesejada / alturadegrau

print(f"Você deverá subir {(numdegraus)} degraus para atingir a altura que voce quer.")