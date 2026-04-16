'''
Exercício 4: Performance de Vendas Regionais (Setor de Dashboard) Crie uma função
chamada analisar_vendas que receba uma lista de números (vendas). A função deve
retornar o total vendido e a média das vendas. Dado o dicionário dados_filiais =
{"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}:
1. Percorra o dicionário.
2. Para cada filial, use a função e faça o unpacking do resultado.
3. Exiba: "Filial [Nome] -> Total: R$[valor], Média: R$[valor]".
'''
dados_filiais = {"Matriz": [10000, 15000, 20000], "Filial Sul": [5000, 7000]}

def analisar_vendas(lista_vendas):
    total  = sum(lista_vendas)
    media = total / len(lista_vendas)

    return total, media

for f in dados_filiais:
    total, media = analisar_vendas(dados_filiais[f])
    #print(f)

    print(f'Filial {f} -> Total: R${total}, Média: R${media}')


