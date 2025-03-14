import os 
os.system ("clear")

print ("""
       arroz              |       feijão
R$  por Kg (até 5kg)      |  R$  por Kg (até 5Kg)                           
R$  por Kg (acima de 5Kg) |  R$  por Kg (acima de 5Kg) 
R$                        |  R$   
""")
fruta = input("Informe o produto que você deseja: ").lower()

match fruta:
    case "arroz":
        quantidade = int(input("Digite a quantidade desejada (em Kg): "))
        precoA = 5.50 
        resultadoA = precoA * quantidade 
        resultado_desconto = (resultadoA - (resultadoA * 0.02))
        if quantidade <= 5:
         descontoA1 = resultadoA - resultado_desconto
         print (f"A quantidade de {quantidade}Kg de arroz custará R${resultadoA}, com R${descontoA1:.2f} de desconto.")
         print(f"Totalizando R${resultado_desconto:.2f}.")
        elif quantidade >5 or quantidade <= 10:
           descontoA2 = resultadoA - (resultadoA * 0.03)
           print(f"A quantidade de {quantidade}Kg de arroz custará R${descontoA2}.")
        elif quantidade > 10:
           descontoA3 = resultadoA (resultadoA * 0.05)
           print(f"A quantidade de {quantidade}Kg de arroz custará R${descontoA3}.")



    case "feijão":
        quantidade = int(input("Digite a quantidade desejada (em Kg): "))
        precoA = 7.00 
        resultadoF = precoA * quantidade 
        resultado_desconto = (resultadoF -(resultadoF * 0.02))
        if quantidade <= 5:
         descontoF1 = resultadoF * 0.02
         print (f"A quantidade de {quantidade}Kg de feijão custará R${resultadoF}, com desconto de R${descontoF1:.2f}. ")
         print(f"Totalizando R${resultado_desconto:.2f}.")
        elif quantidade >5 or quantidade <= 10:
           descontoF2 = resultadoF*0.03
           print(f"A quantidade de {quantidade}Kg de feijão custará R${descontoF2}.")
           print(f"Totalizando R${resultado_desconto:.2f}.")
        elif quantidade > 10:
           descontoF3 = resultadoF * 0.05
           print(f"A quantidade de {quantidade}Kg de feijão custará R${descontoF3}.")
           print(f"Totalizando R${resultado_desconto:.2f}.")
           
    case _: 
         ("Opção inválida!")