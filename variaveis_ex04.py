'''
Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).
'''
faturamento = 15000
custos_fixos = 5000
percentual_imposto = 0.15
percentual_meta = 0.30

imposto = faturamento * percentual_imposto
lucro_liquido = ((faturamento - custos_fixos) - imposto)
margem_lucro = lucro_liquido / faturamento

meta_atigingida = margem_lucro > percentual_meta

print(f'Imposto sobre o faturamento R$ {imposto} reais.')
print(f'Lucro liquido R$ {lucro_liquido} reais.')
print(f'Margem de lucro {margem_lucro:.1%}.')
print(f'Meta atingida? {meta_atigingida}')
