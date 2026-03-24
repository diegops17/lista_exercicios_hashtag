'''
Exercício 3: Cálculo de Desconto Progressivo (Setor de Vendas) Um e-commerce
aplica descontos automáticos no carrinho. Crie um programa que receba o valor total da
compra e aplique a seguinte lógica:
● Compras a partir de R$ 500,00: 15% de desconto.
● Compras a partir de R$ 200,00 (e menos de 500): 10% de desconto.
● Compras abaixo de R$ 200,00: Sem desconto. O programa deve exibir o valor do
desconto e o valor final a pagar, formatados em R$.
'''

valor_total_compra = float(input('Valor total compra R$ '))
valor_final = 0

if valor_total_compra <= 200:
    percentual_desconto = 0

elif valor_total_compra < 500:
    percentual_desconto = 0.10

else:
    percentual_desconto = 0.15

valor_desconto = (valor_total_compra * percentual_desconto) 
valor_final = valor_total_compra - valor_desconto



print(f'''Valor final pagar R$ {valor_final:.2f} reais, 
      desconto de R$ {valor_desconto:.2f} reais equivale a {percentual_desconto:.0%}''')