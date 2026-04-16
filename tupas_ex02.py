'''
Exercício 2: Resumo de Folha de Pagamento (Setor de RH) Crie uma função chamada
calcular_folha que receba o salário bruto de um funcionário. A função deve calcular e
retornar dois valores:
1. O valor do desconto de impostos (fixado em 10%).
2. O salário líquido (salário bruto - desconto). Após criar a função, chame-a para um
salário de **R$ 5.000,00**, faça o unpacking do retorno e exiba: "Desconto:
R$[valor] | Salário Líquido: R$[valor]".
'''

def calcular_folha(salario_bruto):
    desconto_imposto = 0.10
    desconto = salario_bruto * desconto_imposto
    salario_liquido = salario_bruto - desconto

    return (desconto, salario_liquido)

salario = 5000
desconto, salario_liquido = calcular_folha(salario)
print(f'Desconto: R${desconto} | Salário Líquido: R${salario_liquido}')