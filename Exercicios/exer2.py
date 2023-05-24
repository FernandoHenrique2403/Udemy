nome = input("Digite o seu nome ")
sobrenome  = input("Digite seu sobrenome ")
nome_completo = nome+" "+sobrenome
print(nome_completo)

palavra = input("Digite a palavra ")
print((palavra+" ")*20)

nome_produto = input("Nome do Produto: ")
preco = float(input("Digite o preco do produto "))
quantidade = int(input("Digite a quantidade do produto "))
total = preco*quantidade 
print(f"O produto {nome_produto} custa {preco}, você comprou {quantidade} e vai pagar {total}.")