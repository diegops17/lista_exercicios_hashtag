'''
Exercício 1: Padronizador de Nomes de Produtos (Setor de E-commerce) Muitas
vezes, os nomes dos produtos entram no sistema de qualquer jeito (ex: "iPHonE 13", "
macbook air "). Crie uma função chamada padronizar_texto que receba uma string
como parâmetro e retorne esse texto sem espaços extras nas extremidades e com todas as
palavras com a primeira letra maiúscula (formato de título). Teste a função com uma lista de
nomes bagunçados.
produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", "
caixa de som bluetooth " ]
'''
produtos_baguncados = [ " iphone 13 ", "MACBOOK PRO ", " aIrPoDs Pro", "iPad mini ", "caixa de som bluetooth " ]

def padronizar_texto(produto):
        produto = produto.strip().title()
        return produto

produtos_padronizados = []
for p in produtos_baguncados:
    produtos_padronizados.append(padronizar_texto(p))
    print(padronizar_texto(p))


print(produtos_padronizados)

#list compresi
produtos_padronizados2 = [padronizar_texto(p) for p in produtos_baguncados]
print(produtos_padronizados2)

#Usando MAP bem legal, aplica uma função para uma lista de valores

produtos_padronizados3 = list(map(padronizar_texto, produtos_baguncados))
print(produtos_padronizados3)