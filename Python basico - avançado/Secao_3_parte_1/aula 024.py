nome = 'Fernando'

print(nome[2])
print('nan' in nome)
print('dos' in nome)
print(10*'-')
print('rnan' not in nome)
print('zero' not in nome)


nome = input("Digite o seu nome: ")
encontrar = input("Digite o que deseja encontrar: ")

if encontrar in nome :
    print(f'{encontrar} esta em {nome}')

else:
    print(f'{encontrar} não esta em {nome}')