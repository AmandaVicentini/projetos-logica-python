#Elabore um programa que leia 3 notas, calcule e
#escreva a media ponderada delas considerando os pesos 5, 2.5 e
#2.5 A maior nota deve ter peso 5.

nota1 = float(input("Digite sua nota 1:"))
nota2 = float(input("Digite sua nota 2:"))
nota3 = float(input("Digite sua nota 3:"))

if nota1<0 or nota1>10 : print("Valor Inválido para a nota 1")
if nota2<0 or nota2>10 : print("Valor Inválido para a nota 2")
if nota3<0 or nota3>10 : print("Valor Inválido para a nota 3")

else:
  maior = nota1
  if nota2 > maior : maior = nota2
  if nota3 > maior : maior = nota3
  media = 5 * maior / 10 + (2.5 * (nota1 + nota2 + nota3 - maior) / 10)
  print("Média Ponderada:" , media)
