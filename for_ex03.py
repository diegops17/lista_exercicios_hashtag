'''
Exercício 3: Verificação de Estoque Crítico (Setor de Logística) Dada a lista de produtos
estoque_produtos = ["monitor", "teclado", "mouse", "headset",
"gabinete"] e a lista correspondente de quantidades estoque_quantidades = [5,
12, 2, 8, 15]. O estoque mínimo para qualquer item é 8 unidades. Crie um programa
que percorra as listas e, para cada item que esteja abaixo do mínimo, imprima: "ALERTA: O
produto [nome] está com apenas [quantidade] unidades no estoque!".
'''
estoque_produtos = ["monitor", "teclado", "mouse", "headset", "gabinete"] 
estoque_quantidades = [5, 12, 2, 8, 15]


for chave, quantidade in enumerate(estoque_quantidades):
    if quantidade < 8:
        produto = estoque_produtos[chave]
        print(f"ALERTA: O produto {produto} está com apenas {quantidade} unidades no estoque!")

