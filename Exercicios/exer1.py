nome = input("Qual seu nome?")
print(f"Obrigado por responder a pergunta {nome} ")

escolha = int(input("Qual sua bebida favorita?\n1-Água\n2-Cerveja\n3-Vinho\n4-Leite"))

if(escolha==1):
    print(f"Você escolheu {escolha} Água")
elif(escolha==2):
    print(f"Você escolheu {escolha} Cerveja")
elif(escolha==3):
    print(f"Você escolheu {escolha} Vinho")
elif(escolha==4):
    print(f"Você escolheu {escolha} Leite")
else:
    print("Número inválido")
    
idade = int(input("Que ano voce Nasceu? "))
ano = 2023 - idade
print(f"Você tem {ano} anos ")

salario_minimo = float(input("Qual valor do salário minimo? "))
quant = float(input("Quantos salários gostaria de ganhar?"))
pretensao = salario_minimo*quant
print(f"Voce pretende ganhar R$ {pretensao}")

salario1 = float(input("Digite o seu salario "))
salario2 = float(input("Digite o salario minimo"))
idade = int(input("Digite sua idade "))
calculo1 = salario2*2
if(salario1>calculo1 and idade>18):
    print(True)
else:
    print(False)
