import os
os.system ("clear")
a = float (input("Digite um número: "))
b = float (input("Digite um número: "))
c = float (input("Digite um número maior que a soma dos dois anteriores: "))
soma = a + b 

if soma > c:
    print(f"A soma dos números é igual a {soma:.0f}, portanto é maior que {c:.0f}")
elif soma == c:
    print(f" A soma de {a:.0f} com {b:.0f} é igual a {c:.0f}")
else:
    print(f"A soma dos números é menor que {c:.0f}")
