print ("Você está apto(a) para entrar no exército?")
idade = int(input("Quantos anos você tem?: "))

peso = int(input("Quanto você pesa?: "))

altura = float(input("Qual é a sua altura?: "))

if idade >= 18 and peso >= 60 and altura >= 1.70:
  print ("Você esta apto(a) para se alistar.")

else:
  print ("Você não possui um ou mais requisito para se alistar")