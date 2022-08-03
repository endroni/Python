# break - example

print("A instrução break:")
for i in range(1, 6):
    if i == 3:
        break
    print("Laço do loop.", i)
print("Sai do loop.")


# continue - example

print("\nA instrução continue:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Laço do loop.", i)
print("Sai do loop.")