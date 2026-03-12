'''
Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os
seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"].
O gerente pediu para:
1. Adicionar o item "webcam" ao final da lista.
2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa
alteração na lista.
3. Verificar se "impressora" está no estoque. O programa deve exibir True ou
False.
4. Remover o "mouse" da lista, pois saiu de linha.
'''
estoque = ["monitor", "teclado", "mouse", "headset"]

estoque.append('webcam')
posicao_teclado = estoque.index('teclado')
estoque[posicao_teclado] = 'teclado mecanico'
impressora_estoque = "impressora" in estoque

print(estoque)
print(f'Impressora está no estoque: {impressora_estoque}')

item_removido = estoque.remove('mouse')
print(estoque)