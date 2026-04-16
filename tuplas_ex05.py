'''
Exercício 5: Gestão de Chamados de Suporte (Setor de TI) O sistema de chamados
precisa de um resumo diário. Crie uma função resumo_chamados que receba uma lista
com tempos de resposta (em minutos). Ela deve retornar a quantidade de chamados e o
tempo máximo de espera. Teste a função com a lista tempos = [15, 45, 10, 120,
30]. Desempacote os resultados e exiba uma mensagem formatada alertando sobre o
tempo máximo encontrado.
'''

def resumo_chamados(lista_tempo_resposta):
    quant_chamados = len(lista_tempo_resposta)
    tempo_max_esoera = max(lista_tempo_resposta)

    return quant_chamados, tempo_max_esoera


lista_tempos = [15, 45, 10, 120, 30]

quant_chamados, temp_espera = resumo_chamados(lista_tempos)

print(f'Total chamados: {quant_chamados}, Tempo máximo encontrado: {temp_espera}min')