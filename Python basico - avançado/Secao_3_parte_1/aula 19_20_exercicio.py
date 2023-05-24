primeiro_valor = input('Digite um valor')
segundo_valor = input('Digite outro valor')

if segundo_valor > primeiro_valor:
    print(f'o segundo valor {segundo_valor} é maior que o primeiro valor {primeiro_valor}')
elif primeiro_valor>segundo_valor:
    print(f'o primeiro valor {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'os valores {primeiro_valor} e {segundo_valor} são iguais')
else:
    print('informação invalida')