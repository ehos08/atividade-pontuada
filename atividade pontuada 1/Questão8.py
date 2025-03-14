import os 
os.system ("clear")

cor = input(""" Selecione a cor do CD
            
                Verde       |  Azul          | Amarelo        | Vermelho
            valor: R$10.00  | valor: R$20.00 | valor: R$30.00 | valor: R$40.00
""").lowerr()
match cor:
    case "verde":
        print(" O valor a ser pago pelo CD será de R$10.00")
    case "azul":
        print(" O valor a ser pago pelo CD será de R$20.00")
    case "amarelo":
        print(" O valor a ser pago pelo CD será de R$30.00")
    case "vermelho":
        print(" O valor a ser pago pelo CD será de R$40.00")