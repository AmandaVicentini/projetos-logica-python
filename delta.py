#Implemente um programa que leia os valores a,b e c
#de uma formula de Bhaskara, calcule e escreva as suas raízes reais.

import math
a = float(input("Informe o valor de a:"))
b = float(input("Informe o valor de b:"))
c = float(input("Informe o valor de c:"))

delta = math.pow(b,2) - 4 * a * c
if delta<0 or a==0 : print("Valor inválido. Delta negativo ou divisão por zero.")
else:
  x1 = (-b + math.sqrt(delta))/(2*a)
  x2 = (-b - math.sqrt(delta))/(2*a)
  print("x1:" , x1)
  print("x2:" , x2)
