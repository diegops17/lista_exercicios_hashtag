'''
Exercício 5: Atualização de Preços Interativa (Input + Lista) Você tem uma lista de
preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos
= ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
1. Peça para o usuário digitar qual o nome do produto.
2. Peça para o usuário digitar o novo preço.
3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços
'''
precos = [100.0, 250.0, 500.0]
vinhos = ["Branco", "Tinto","Champagne"]

nome_vinho = str(input('Nome do produto: ')).strip().lower()
novo_preco = float(input('Valor do produto: '))

vinhos.append(nome_vinho)
precos.append(novo_preco)

print(f'Vinhos: {vinhos}')
print(f'Preços: {precos}')