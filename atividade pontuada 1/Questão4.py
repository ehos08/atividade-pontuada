import os 
os.system ("clear")

print ("""
       Maçã                   |       Morango
R$ 1,80 por Kg (até 5kg)      |  R$ 2,50 por Kg (até 5Kg)                           
R$ 1,50 por Kg (acima de 5Kg) |  R$ 2,20 por Kg (acima de 5Kg)          
""")
fruta = input("Informe a fruta que você deseja:").lower()

match fruta:
    case "maçã":
        quantidade = int(input("Digite a quantidade desejada (em Kg):"))
        resultadoM1 = quantidade * 1.80
        resultadoM2 = quantidade * 1.50
        if quantidade >= 10 or resultadoM2 > 15:
         descontoM2 = (quantidade * 1.50)*0.1
         print (f"A quantidade de {quantidade}Kg de maçãs custará R${resultadoM2}. ")
        elif quantidade <= 5:
           print(f"A quantidade de {quantidade}Kg de maçãs custará R${resultadoM1}.")
        elif quantidade < 5:
           resultadoM1 = quantidade * 1.50
           print(F"A quantidade de {quantidade}Kg de maçãs custará R${resultadoM1}.")
    
    case "morango":
        quantidade = int(input("Digite a quantidade desejada (em Kg):"))
        resultadoG1 = quantidade * 2.50
        resultadoG2 = quantidade * 2.20
        if quantidade >= 10 or resultadoG2 > 15:
         descontoG2 = (quantidade * 2.50)*0.1
         print (f"A quantidade de {quantidade}Kg de maçãs custará R${resultadoG2}. ")
        elif quantidade <= 5:
           print(f"A quantidade de {quantidade}Kg de maçãs custará R${resultadoG1}.")
        elif quantidade < 5:
           resultadoG1 = quantidade * 2.20
           print(F"A quantidade de {quantidade}Kg de maçãs custará R${resultadoG1}.")