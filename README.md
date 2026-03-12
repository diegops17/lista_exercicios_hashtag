# lista_exercicios_hashtag
Resolução da lista de exercicios da hashtag

##### VARIAVEIS #####
# Exercício 1: Cálculo de Bônus de Vendas (RH/Vendas)
Cenário: Uma empresa decidiu dar um bônus de 10% sobre o faturamento total para a
equipe de vendas. Objetivo: Calcule o valor do bônus e o faturamento final da empresa
após subtrair esse bônus.
● Faturamento inicial: 50.000
● Percentual de bônus: 0.10

# Exercício 2: Controle de Estoque de E-commerce (Logística)
Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no
estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um
fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final.

# Exercício 3: Divisão de Cargas (Logística/Transporte)
Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada
caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão
totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma
última viagem menor? (Use %)

# Exercício 4: Análise de Margem de Lucro (Financeiro)
Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$
5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro
líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana
chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

# Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos)
Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente
quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de
divisão inteira e resto da divisão para converter os 40 meses.


##### STRINGS #####
# Exercício 1: Relatório de Margem de Lucro (Setor Financeiro) Uma empresa de varejo
precisa de um resumo rápido sobre a performance de um produto. Dado o faturamento de
R$ 45.000,00 e o custo de R$ 23.500,00, crie um programa que calcule o lucro e a margem
de lucro (lucro dividido pelo faturamento). Exiba uma mensagem formatada onde o lucro
use o separador de milhar e duas casas decimais, e a margem seja exibida como uma
porcentagem inteira.

# Exercício 2: Padronização de Dados de CRM (Setor de Vendas) Um vendedor cadastrou
um cliente com os dados desorganizados no sistema: nome = " mArCoS aNtOnIo
rOcHa " e email = " MARCOS.ROCHA@GMAIL.COM ". Para evitar duplicidade e erros
de envio, você deve:
1. Remover os espaços extras no início e fim das duas variáveis.
2. Deixar o nome apenas com as primeiras letras de cada palavra em maiúsculo
(formato de nome próprio).
3. Deixar o e-mail todo em letras minúsculas. Exiba os resultados finais no console.

# Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome
e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o
domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br.
Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo
endereço de e-mail.

# Exercício 4: Extração de Username para Log (Setor de Segurança) Para criar um log de
acessos, o sistema precisa extrair apenas a parte do nome do usuário de um e-mail
corporativo (tudo o que vem antes do @). Dado o e-mail
beatriz.oliveira@grupocorp.com, use a função .find() e o fatiamento de texto
para extrair e exibir apenas o nome beatriz.oliveira.

# Exercício 5: Personalização de E-mail de Marketing (Setor de Marketing) O marketing
quer enviar um e-mail de boas-vindas. O cliente forneceu o nome completo: lucas
ferreira souza. Você deve extrair apenas o primeiro nome para usar na saudação (ex:
"Olá, Lucas!"). O código deve:
1. Encontrar a posição do primeiro espaço.
2. Fatiar o texto para pegar apenas o primeiro nome.
3. Formatar o nome com a primeira letra maiúscula.
4. Exibir a mensagem: "Olá, [Primeiro Nome], seja bem-vindo ao nosso clube!"


#### INPUTS ####
# Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de
serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o
valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
1. Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
2. Limpar o texto removendo o "R$" e trocando a vírgula por ponto.
3. Converter para número decimal (float).
4. Calcular o valor do imposto (15% do valor bruto).
5. Exibir uma mensagem formatada com f-string mostrando o valor do imposto com
duas casas decimais.

# Exercício 2: Sistema de Cadastro de Colaborador (Setor de RH) Ao cadastrar um novo
funcionário, o RH precisa extrair o primeiro nome para criar um crachá e padronizar o
e-mail. Crie um programa que:
1. Peça o nome completo do colaborador.
2. Peça o e-mail pessoal do colaborador.
3. Extraia o primeiro nome (deixe-o com a primeira letra maiúscula).
4. Padronize o e-mail (remova espaços extras e deixe tudo em letras minúsculas).
5. Exiba a mensagem: "Cadastro concluído: [Primeiro Nome]. E-mail de acesso: [E-mail
padronizado]".

# Exercício 3: Análise de Metas de Vendas (Setor Comercial) Um gerente quer comparar o
desempenho de duas filiais. O programa deve:
1. Pedir o faturamento da Loja A e o faturamento da Loja B (o usuário pode digitar
números decimais).
2. Calcular o faturamento total das duas lojas.
3. Calcular a média de faturamento entre elas.
4. Exibir uma única mensagem formatada informando o total e a média, utilizando o
separador de milhar e duas casas decimais.


#### LISTAS ####
# Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as
vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um
programa que exiba um pequeno relatório contendo:
1. O total de vendas na semana.
2. A média de vendas diária.
3. O valor da melhor venda e da pior venda do período.

# Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os
seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"].
O gerente pediu para:
1. Adicionar o item "webcam" ao final da lista.
2. O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa
alteração na lista.
3. Verificar se "impressora" está no estoque. O programa deve exibir True ou
False.
4. Remover o "mouse" da lista, pois saiu de linha.

# Exercício 3: Organização de Preços (Ordenação e Slicing) Uma importadora listou os
preços de frete em dólar: fretes = [50, 80, 20, 150, 40]. Para apresentar em uma
reunião, você deve:
1. Ordenar a lista do maior para o menor preço.
2. Pegar os 2 fretes mais caros (usando fatiamento/slicing) e armazenar em uma nova
lista chamada top_fretes.
3. Exibir a lista original ordenada e a lista dos top_fretes.

# Exercício 4: Sistema de Logística (Busca e Extensão) A empresa "LogTrack" tem uma
rota de entregas: rota = ["Sao Paulo", "Campinas", "Jundiai",
"Sorocaba"]. Novas cidades foram adicionadas por uma empresa parceira:
novas_cidades = ["Itu", "Valinhos"]. Seu script deve:
1. Unir as duas listas em uma só (usando extend).
2. Identificar em qual posição (índice) está a cidade de "Sorocaba".
3. Exibir a lista completa e a posição encontrada.
4. Exibir uma mensagem final: “Sorocaba é a Xª cidade da rota”

# Exercício 5: Atualização de Preços Interativa (Input + Lista) Você tem uma lista de
preços de produtos: precos = [100.0, 250.0, 500.0] e uma com o nome: vinhos
= ["Branco", "Tinto","Champagne"]. Crie um programa interativo que:
1. Peça para o usuário digitar qual o nome do produto.
2. Peça para o usuário digitar o novo preço.
3. Atualize o preço na lista e exiba as listas completas com os nomes e os preços