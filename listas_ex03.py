'''
Exercício 3: Organização de Preços (Ordenação e Slicing) Uma importadora listou os
preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma
reunião, você deve:
1. Ordenar a lista do maior para o menor preço.
2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova
lista chamada top_fretes.
3. Exibir a lista original ordenada e a lista dos top_fretes.
'''
fretes = [50, 80, 20, 150, 40]
lista_ordenada = sorted(fretes, reverse=True)

top_fretes = []
top_fretes = lista_ordenada[:2]

print(f'Lista ordenada {lista_ordenada}')
print(f'Top fretes: {top_fretes}')
