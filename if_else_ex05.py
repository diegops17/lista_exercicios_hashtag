'''
Exercício 5: Sistema de Triagem de E-mails (Setor de Customer Experience) Crie um
sistema que ajude a filtrar para qual departamento uma reclamação deve ir. O usuário deve
digitar o assunto do e-mail.
● Se no assunto aparecer a palavra "pagamento" ou "boleto", exiba: "Encaminhado
para o Financeiro".
● Se no assunto aparecer a palavra "entrega" ou "atraso", exiba: "Encaminhado para a
Logística".
● Caso não seja nenhum desses, exiba: "Encaminhado para o Suporte Geral". Dica:
Use o operador in para verificar se a palavra está dentro do texto.
'''

assunto = str(input('Informe o assunto da reclamação: ')).strip().lower()
lista_finaceiro = ['pagamento', 'boleto']
lista_logistica = ['entrega', 'atraso']
setor = ''

if  'pagamento' in assunto or 'boleto' in assunto:
    setor = 'Financeiro'

elif 'entrega' in assunto or 'atraso' in assunto:
    setor = 'Logística'

else:
    setor = 'Suporte Geral'
print(f'Encaminhado para o(a) {setor}')