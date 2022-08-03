# Esse programa conta a quantidade de números impares
# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.

odd_numbers = 0
even_numbers = 0

# Leia o primeiro número
number = int(input("Digite um número, ou 0 para sair: "))

# 0 encerra o programa
while number != 0:
    # Verifica se o número é impar
    if number % 2 == 1:
        # Incrementa os ímpares 
        odd_numbers += 1
    else:
        # Incrementa o total de números
        even_numbers += 1
    # Entra com o próximo número
    number = int(input("Digite um número, ou 0 para sair: "))

# Print results.
print("Total de números ímpares:", odd_numbers)
print("Total de números:", even_numbers)

