'''
Exercício 5: Reajuste Geral de Preços (Setor Comercial) Devido à inflação, a empresa
decidiu aumentar o preço de todos os seus produtos em um percentual decidido pelo
usuário. O catálogo atual é: precos = {"celular": 1500, "tablet": 2500,
"notebook": 5000}.
1. Peça ao usuário para digitar o percentual de aumento (ex: 10 para 10%).
2. Use um loop para atualizar cada preço dentro do dicionário.
3. Ao final, exiba o novo catálogo de preços formatado.
'''

precos = {"celular": 1500, "tablet": 2500, "notebook": 5000}
percentual = int(input('informe o percetual de aumento: '))
percentual = percentual / 100

for preco in precos:
    aumento = precos[preco] * percentual
    precos[preco] += aumento

print(precos)