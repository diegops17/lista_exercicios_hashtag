'''
Exercício 1: Atualização de Cadastro de Clientes (Setor de CRM) Você tem um
dicionário com o faturamento acumulado de alguns clientes: clientes = {"Lira":
5000, "Alon": 3000, "Julia": 4500}. O cliente "Alon" fez uma nova compra de R$
1.500,00. Crie um código que:
1. Atualize o valor do cliente "Alon" somando o novo valor ao faturamento antigo.
2. Adicione um novo cliente chamado "Marcos" com um faturamento inicial de R$
2.000,00.
3. Exiba o dicionário atualizado.
'''
clientes = {"Lira":5000, "Alon": 3000, "Julia": 4500}

nova_compra = 1500

clientes['Alon'] += nova_compra
print(f'Valor atualizado Alon R$ {clientes['Alon']} reais')

clientes['Marcos'] = 2000

print(clientes)