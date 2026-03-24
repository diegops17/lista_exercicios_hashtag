'''
Exercício 4: Análise de Metas Combinadas (Setor Comercial) Uma empresa paga bônus
se a meta individual do vendedor E a meta da loja forem batidas.
1. Peça as vendas do vendedor e a meta individual dele.
2. Peça as vendas totais da loja e a meta da loja.
3. Se o vendedor bater a meta dele E a loja bater a meta total, o bônus é de 20% sobre
as vendas do vendedor.
4. Caso contrário, o bônus é zero. Exiba a mensagem: "Seu bônus este mês é de:
R$[valor]"
'''

vendas_vendedor = float(input('Informe suas vendas: '))
meta_vendedor = float(input('Informe sua meta: '))

vendas_loja = float(input('Informe as vendas da loja: '))
meta_loja = float(input('Informe as metas da loja: '))

bonus = 0

if vendas_vendedor > meta_vendedor and vendas_loja > meta_loja:
    bonus = 0.20
else:
    bonus = 0

valor_bonus = vendas_vendedor * bonus

print(f'Seu bônus este mês é de: R${valor_bonus:.2f}')