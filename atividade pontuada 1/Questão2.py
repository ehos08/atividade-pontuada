import os 
os.system ("clear")

nome = input("Informe seu nome: ")
sexo = input("Informe seu sexo (Masculino = M| Feminino = F):").upper()
estado_civil = input("Informe seu estado civil (Casado(a) | Solteiro(a) | Viúvo(a)): ").upper()

if sexo == "F" and estado_civil == "CASADA":
    tempo = input("Informe há quanto tempo você está casada: ") 
    print (f"\n{nome} \n {sexo} \n {estado_civil} \n casada há {tempo} anos")
else:
    print (f"\n{nome} \n {sexo} \n {estado_civil}")
    
