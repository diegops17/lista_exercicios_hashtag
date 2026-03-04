'''
Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. 
Objetivo: Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.
Faturamento inicial: 50.000
Percentual de bônus: 0.10
'''

faturamento_inicial = 50000
percentual_bonus = 0.1

valor_bonus = faturamento_inicial * percentual_bonus
faturamento_final = faturamento_inicial - valor_bonus

print(f'Valor do bônus R$ {valor_bonus} reais.')
print(f'Faturamento final R$ {faturamento_final} reais.')