senha = input('Senha: ')

if senha == '123456':
    print('Acesso Permitido')
else:
    print('Senha Incorreta')

if not senha:
    print('Senha Vazia')

print(not True)
print(not False)