import csv

arquivo = 'Listagem_dos_Filmes.csv'
dados = []

with open(arquivo, 'r', encoding='utf-8') as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        # Remove a coluna vazia
        linha.pop('', None)
        dados.append(linha)

nome_dataset = "Listagem dos Filmes"
colunas = list(dados[0].keys())

print("Nome do dataset:", nome_dataset)
print("Quantidade de registros:", len(dados))
print("Colunas:", colunas)

print("\nPrimeiros 5 registros:\n")
for i in range(5):
    print("Ano:", dados[i]['Ano de exibição'])
    print("Título:", dados[i]['Título da obra'])
    print("Gênero:", dados[i]['Gênero'])
    print("Público:", dados[i]['Público no ano de exibição'])
    print("Renda:", dados[i]['Renda (R$) no ano de exibição'])
    print("\n")

### PARTE 2

coluna1 = 'Público no ano de exibição'
coluna2 = 'Renda (R$) no ano de exibição'

def analisar_coluna(nome_coluna):
    valores = []

    for linha in dados:
        valor = linha[nome_coluna]

        if valor != '':
            try:
                numero = float(valor)
                valores.append(numero)
            except:
                pass

    quantidade = len(valores)

    if quantidade > 0:
        minimo = min(valores)
        maximo = max(valores)
        media = sum(valores) / quantidade

        print("\n ESTATÍSTICAS DESCRITIVAS")
        print("\nColuna:", nome_coluna)
        print("Quantidade de valores válidos:", quantidade)
        print("Valor mínimo:", minimo)
        print("Valor máximo:", maximo)
        print("Média:", media)
    else:
        print("\nColuna:", nome_coluna, "não possui dados válidos")


analisar_coluna(coluna1)
analisar_coluna(coluna2)

# PARTE 3 - FILTROS

def converter_numero(valor):
    try:
        valor = valor.replace('.', '').replace(',', '.')
        return float(valor)
    except:
        return None


# FILTRO 1
print("\n FILTRO 1 ")
print("Filmes com público maior que 100000")

resultado1 = []

for linha in dados:
    publico = converter_numero(linha['Público no ano de exibição'])

    if publico is not None and publico > 100000:
        resultado1.append(linha)

print("Quantidade encontrada:", len(resultado1))

for i in range(min(10, len(resultado1))):
    print("Ano:", resultado1[i]['Ano de exibição'])
    print("Título:", resultado1[i]['Título da obra'])
    print("Gênero:", resultado1[i]['Gênero'])
    print("Público:", resultado1[i]['Público no ano de exibição'])
    print("Renda:", resultado1[i]['Renda (R$) no ano de exibição'])
    print("\n")

# FILTRO 2
print("\n FILTRO 2")
print("Filmes com renda maior que 1.000.000")

resultado2 = []

for linha in dados:
    renda = converter_numero(linha['Renda (R$) no ano de exibição'])

    if renda is not None and renda > 1000000:
        resultado2.append(linha)

print("Quantidade encontrada:", len(resultado2))

for i in range(min(10, len(resultado2))):
    print("Ano:", resultado2[i]['Ano de exibição'])
    print("Título:", resultado2[i]['Título da obra'])
    print("Gênero:", resultado2[i]['Gênero'])
    print("Público:", resultado2[i]['Público no ano de exibição'])
    print("Renda:", resultado2[i]['Renda (R$) no ano de exibição'])
    print("\n")


# FILTRO 3
print("\n FILTRO 3")
print("Filmes com público > 50000 e renda > 500000")

resultado3 = []

for linha in dados:
    publico = converter_numero(linha['Público no ano de exibição'])
    renda = converter_numero(linha['Renda (R$) no ano de exibição'])

    if (publico is not None and renda is not None and 
        publico > 50000 and renda > 500000):
        resultado3.append(linha)

print("Quantidade encontrada:", len(resultado3))

for i in range(min(10, len(resultado3))):
    print("Ano:", resultado3[i]['Ano de exibição'])
    print("Título:", resultado3[i]['Título da obra'])
    print("Gênero:", resultado3[i]['Gênero'])
    print("Público:", resultado3[i]['Público no ano de exibição'])
    print("Renda:", resultado3[i]['Renda (R$) no ano de exibição'])
    print("\n")

# FILTRO INTERATIVO

print("\n ESCOLHA O GÊNERO DO FILME")
print("\n Os gêneros são: Animação, documentário e ficção")

genero_usuario = input("Digite o gênero: ").lower()

resultado = []

for linha in dados:
    genero = linha['Gênero']

    if genero and genero_usuario in genero.lower():
        resultado.append(linha)

print("Quantidade encontrada:", len(resultado))

for i in range(min(10, len(resultado))):
    print("Ano:", resultado[i]['Ano de exibição'])
    print("Título:", resultado[i]['Título da obra'])
    print("Gênero:", resultado[i]['Gênero'])
    print("Público:", resultado[i]['Público no ano de exibição'])
    print("Renda:", resultado[i]['Renda (R$) no ano de exibição'])
    print("\n")
    
with open('lista_filme.txt', 'w', encoding='utf-8') as arquivo:
  arquivo.write('Nome: Listagem de Filmes\n')
  arquivo.write('O nosso tema trata sobre alguns filmes que foram lançados no ano de 2019, apresentando o nome, gênero, país, nacionalidade(brasileira ou estrangeira), empresa distribuidora, público e renda.\n')
  arquivo.write("O total de registros são de 70 filmes e conta com 9 colunas.\n")  
  arquivo.write("Na coluna: Público no ano de exibição, foram obtidas como valor mínimo: 6, valor máximo:1622344 e a média foi de:87214,05. \n")  
  arquivo.write("Na coluna: Renda(R$) no ano de exibição, foram obtidas como valor mínimo: 21, valor máximo:24330901 e a média foi de:1351881,59.\n")
  arquivo.write("Os resultados dos filtros da parte 3, são: FILTRO 1:\n")
  arquivo.write("Filmes com público maior que 100000\n")
  arquivo.write("Quantidade encontrada: 23\n")
  arquivo.write("Ano: 2019\n")
  arquivo.write("Título: A Batalha Das Correntes\n")
  arquivo.write("Gênero: Ficção\n")
  arquivo.write("Público: 19579.0\n")
  arquivo.write("Renda: 425304.0 \n")
  arquivo.write("FILTRO 2:\n")
  arquivo.write("Filmes com renda maior que 1.000.000\n")
  arquivo.write("Quantidade encontrada: 28\n")
  arquivo.write("Ano: 2019\n")
  arquivo.write("Título: 3 Faces\n")
  arquivo.write("Gênero: Ficção\n")
  arquivo.write("Público: 6289.0\n")
  arquivo.write("Renda: 103805.0\n")
  arquivo.write("FILTRO 3:\n")
  arquivo.write("Filmes com público > 50000 e renda > 500000\n")
  arquivo.write("Quantidade encontrada: 29\n")
  arquivo.write("Ano: 2019\n")
  arquivo.write("Título: 3 Faces\n")
  arquivo.write("Gênero: Ficção\n")
  arquivo.write("Público: 6289.0\n")
  arquivo.write("Renda: 103805.0\n")
  arquivo.write("Ao analisarmos nosso dataset, observamos que todos os filmes são do ano de 2019, a maioria dos filmes são de ficção e os países que mais produziram filmes nesse dataset foram:Brasil com 23 filmes e o Estados Unidos com 20 filmes.")

  
