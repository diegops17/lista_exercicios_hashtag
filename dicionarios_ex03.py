'''Exercício 3: Análise de Faturamento por Região (Setor Financeiro) Dada a lista de
faturamento por região: vendas_regiao = {"Norte": 15000, "Sul": 22000,
"Leste": 18000, "Oeste": 25000}. Seu programa deve:
1. Extrair todos os valores (faturamentos) para uma lista.
2. Calcular e exibir o faturamento total da empresa (soma de todas as regiões).
3. Calcular e exibir o faturamento médio das regiões.'''

vendas_regiao = {"Norte": 15000, "Sul": 22000, "Leste": 18000, "Oeste": 25000}
lista_fatuamento = list(vendas_regiao.values())

#for faturamento in vendas_regiao.values():
#    lista_fatuamento.append(faturamento)

faturamento_total = sum(lista_fatuamento)

print(f'Faturamento total da empresa R$ {faturamento_total:.2f} reais')

for c in vendas_regiao.keys():
    print(f'Fatuamento médio do {c}: R$ {vendas_regiao[c] / len(lista_fatuamento):.2f} reais')