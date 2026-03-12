'''
Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as
vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um
programa que exiba um pequeno relatório contendo:
1. O total de vendas na semana.
2. A média de vendas diária.
3. O valor da melhor venda e da pior venda do período.
'''

vendas = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas)
media_vendas = total_vendas / len(vendas)
melhor_venda = max(vendas)
pior_venda = min(vendas)

print(f'Total Vendas R$ {total_vendas}')
print(f'Média Vendas R$ {media_vendas}')
print(f'Melhor Venda R$ {melhor_venda}')
print(f'Pior Venda R$ {pior_venda}')
