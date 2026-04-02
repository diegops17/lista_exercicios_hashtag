'''
Exercício 1: Automação de Convites (Setor de Eventos/RH) A empresa terá um
treinamento e você precisa simular o envio de 10 lembretes no console fazendo a contagem
regressiva para aparecer no sistema da empresa. Use a função range() para imprimir 10
vezes a mensagem: "Lembrete: O treinamento de Python começa em X minutos.
'''
import time

for i in range(10, 0, -1):
    print(f'Lembrete: O treinamento de Python começa em {i} minutos.')
    time.sleep(0.1)