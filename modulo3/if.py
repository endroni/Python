#Lendo os valores
number1 = int(input("Digite um número: "))
number2 = int(input("Digite outro número: "))
number3 = int(input("Só mais um número: "))

# Considerando que o primeiro número é o maior
larget_number = number1

# Verificando qual número é maior
if number2 > larget_number: larget_number = number2
if number3 > larget_number: larget_number = number3

# Exibindo o maior número
print("O maior número é: ", larget_number)