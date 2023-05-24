doces = ("cocada", "mariola", "chocolate", "goiabada", "bala", "cocada", "gelatina", "cocada")
"cocada".count(doces)
numeros = []
soma = 0
multiplicacao = 1

while True:
    numero = int(input("Informe um número (zero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

if numeros:
    for numero in numeros:
        soma += numero
        multiplicacao *= numero

    numeros.sort()
    menor = numeros[0]
    maior = numeros[len(numeros)-1]

    print("Soma: ", soma)
    print("Multiplicação: ", multiplicacao)
    print("Maior número: ", maior)
    print("Menor número: ", menor)

    palavras = []

while True:
    palavra = input("Informe uma palavra (zero para sair): ")
    if palavra == "0":
        break
    palavras.append(palavra)

palavra_contar = input("Informe a palavra que deseja contar: ")
qtd = palavras.count(palavra_contar)
print(f"Temos {qtd} ocorrências de {palavra_contar}.") 


numeros = []
lista_unica = []
lista_repetidos = []

while True:
    numero = int(input("Informe um número (zero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for x in numeros:
    if x not in lista_unica:
        lista_unica.append(x)
    else:
        if x not in lista_repetidos:
            lista_repetidos.append(x)

print("Números informados: ", numeros)
print("Números sem repetição:", lista_unica)
print("Somente números que se repetiram:", lista_repetidos)


numeros = []
lista_pares = []
lista_impares = []

while True:
    numero = int(input("Informe um número (zero para sair): "))
    if numero == 0:
        break
    numeros.append(numero)

for numero in numeros:
    if numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print("Pares:", lista_pares)
print("Ímpares:", lista_impares)