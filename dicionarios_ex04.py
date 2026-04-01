'''
Exercício 4: Sistema de RH – Média de Desempenho (Setor de RH) O RH armazena as
últimas 3 notas de desempenho de cada funcionário em um dicionário: desempenho =
{"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}. O gestor
quer saber a média da funcionária "Paula". Crie um código que:
1. Acesse a lista de notas da "Paula".
2. Calcule a média das notas (soma das notas dividida pela quantidade de notas).
3. Exiba o resultado: "A média de Paula foi [media]".
'''
desempenho =  {"Lira": [8, 9, 7], "Paula": [10, 9, 10], "Tiago": [6, 7, 8]}

nome_colaborador = 'Paula'

notas_colaborador = desempenho[nome_colaborador]
soma_notas_colaborador = sum(notas_colaborador)
media_notas_colaborador = soma_notas_colaborador / len(notas_colaborador)

print(f'Notas de {nome_colaborador}: {desempenho[nome_colaborador]}')
print(f'Soma das notas: {soma_notas_colaborador}')
print(f'Média: {media_notas_colaborador:.1f}')