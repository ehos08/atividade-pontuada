import os 
os.system ("clear")

a = int(input("Digite um número :"))
b = int(input("Digite um número igual ao anterior para soma, e um diferente ao anterior para multiplicar: "))
soma = a + b 
multi = a * b
resultado = int

if a == b:
    resultado = soma
    print (f"A soma entre {a} e {b} é igual a {resultado}") 
elif a < b or a > b:
    resultado = multi
    print(f"A multiplicação entre {a} e {b} é igual a {resultado}")
else: print ("números inválidos")
