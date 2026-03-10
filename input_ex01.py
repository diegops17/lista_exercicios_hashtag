''''
Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
3. Converter para número decimal (float).
4. Calcular o valor do imposto (15% do valor bruto).
5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
duas casas decimais.
'''

percentual_imposto = 0.15
valor_bruto = input('Digite o valor bruto R$ ')
valor_bruto = valor_bruto.replace('R$', '').replace('.', '').replace(',', '.')

valor_imposto = float(valor_bruto) * percentual_imposto
print(f'Valor do imposto R$ {valor_imposto:,.2f} reais')