'''
Exercício 5: Conversor de Moeda Interativo (Setor de Importação) A empresa precisa
converter preços de uma lista em Dólar para Real.
1. Crie uma função chamada converter_para_real que receba um preço em dólar
e a cotação do dia, retornando o valor em real.
2. Crie uma segunda função chamada processar_lista_precos que receba uma
lista de preços em dólar e a cotação. Dentro dela, use a primeira função para
calcular o valor de cada item e exiba: "O item custa R$[valor]". Teste com a lista
precos_usd = [100, 50, 250] e cotação de 5.20.
'''

def converter_para_real(valor_dolar: float, cotacao_dolar: float):
    valor_real = valor_dolar * cotacao_dolar
    return valor_real

def processar_lista_precos(lista_valores_dolar: list, cotacao: float):
    
    for valor in lista_valores_dolar:
        valor = converter_para_real(valor, cotacao)
        print(f'O item custa R$ {valor:.2f}')

precos_usd = [100, 50, 250]

cotacao = 5.20
processar_lista_precos(precos_usd, cotacao)