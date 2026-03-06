'''
Exercício 3: Divisão de Cargas (Logística/Transporte)
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)
'''

quant_caixas = 1250
limite_caminhao = 12

quant_caminhao_cheio = quant_caixas // limite_caminhao
caixas_restantes = quant_caixas % limite_caminhao

print(f'Quantidade de caminhões cheios: {quant_caminhao_cheio}')
print(f'Caixas resantes: {caixas_restantes}')