import os 
os.system ("clear")

print ("""
       arroz                  |       feijão
R$ 1,80 por Kg (até 5kg)      |  R$ 2,50 por Kg (até 5Kg)                           
R$ 1,50 por Kg (acima de 5Kg) |  R$ 2,20 por Kg (acima de 5Kg)          
""")
fruta = input("Informe o produto que você deseja: ").lower()

match fruta:
    case "arroz":
        quantidade = int(input("Digite a quantidade desejada (em Kg): "))
        precoA = 5.50 
        resultadoA = quantidade * precoA
        descontoA1 = resultadoA - (resultadoA * 0.02)
        if quantidade <= 5:
         print (f"A quantidade de {quantidade}Kg de arroz custará R${resultadoA}, com R${descontoA1} de desconto.")
         resultado_desconto = resultadoA - descontoA1
         print(f"Totalizando R${resultado_desconto}.")
        elif quantidade >5 or quantidade <= 10:
           descontoA2 = resultadoA - (resultadoA * 0.03)
           print(f"A quantidade de {quantidade}Kg de arroz custará R${descontoA2}.")
        elif quantidade > 10:
           descontoA3 = resultadoA (resultadoA * 0.05)
           print(f"A quantidade de {quantidade}Kg de arroz custará R${descontoA3}.")



    case "feijão":
        quantidade = int(input("Digite a quantidade desejada (em Kg):"))
        precoA = 7.00 
        resultadoF = quantidade * precoA
        if quantidade <= 5:
         descontoF1 = resultadoF*0.02
         print (f"A quantidade de {quantidade}Kg de feijão custará R${descontoF1}. ")
        elif quantidade >5 or quantidade <= 10:
           descontoF2 = resultadoF*0.03
           print(f"A quantidade de {quantidade}Kg de feijão custará R${descontoF2}.")
        elif quantidade > 10:
           descontoF3 = resultadoF * 0.05
           print(f"A quantidade de {quantidade}Kg de feijão custará R${descontoF3}.")
           
    case _: 
         ("Opção inválida!")