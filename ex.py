# Camila de Souza Santana e Sophia Teixeira Ramada

produtos = [
    {
    "nome": "Notebook",
    "preco": 4500.0,
    "quantidade": 10,
    "categoria": "Informática"
    },
    {
    "nome": "Mouse",
    "preco": 80.0,
    "quantidade": 15,
    "categoria": "Periféricos"
    },
    {
    "nome": "Teclado",
    "preco": 250.0,
    "quantidade": 7,
    "categoria": "Periféticos"
    },
    {
    "nome": "Monitor",
    "preco": 500.0,
    "quantidade": 6,
    "categoria": "Informática"
    },
    {
    "nome": "Impressora",
    "preco": 3500.0,
    "quantidade": 16,
    "categoria": "Informática"
    }
]

print("==================================")
print("MENU")
print("==================================")

# Iniciando menu

menu = True
while menu:
    print("\n1- Listar Produtos")
    print("2- Cadastrar Produto")
    print("3- Buscar Produto")
    print("4- Exibir análise do estoque")
    print("5- Ordenar Produtos")
    print("6- Remover Produto")
    print("7- Sair")
    op = int(input("O que deseja fazer"))

    match op:
        case 1:
            # Usa laço para percorrer todos os produtos e exibir suas informações
            for produto in produtos:
                print("\nProduto:", produto["nome"])
                print("Preço:", produto["preco"])
                print("Quantidade:", produto["quantidade"])
                print("Categoria:", produto["categoria"])

        case 2:
            # Tratamento de erro caso o usuário digite um valor inválido
            print("Cadastro de produto:")
            try:
                nome = input("Nome do produto: ").strip()
                if nome == "":
                    raise ValueError("O nome do produto não pode ser vazio.")
                
                preco = float(input("Preço: "))
                if preco <= 0:
                    raise ValueError("O preço deve ser maior que zero.")

                quantidade = int(input("Quantidade: "))
                if quantidade < 0:
                    raise ValueError("A quantidade não pode ser negativa.")

                categoria = input("Categoria: ").strip()
                if categoria == "":
                    raise ValueError("A categoria não pode ser vazia.")

                novo_produto = {
                    "nome": nome,
                    "preco": preco,
                    "quantidade": quantidade,
                    "categoria": categoria
                }

                produtos.append(novo_produto)
                print("Produto adicionado com sucesso!")
            # Caso seja um valor inválido, apresenta erro
            except ValueError as e:
                print("Erro ao cadastrar:", e)

        case 3:
            # Trata valor informado para comparação
            produto_busca = input("Digite o nome do produto:").strip().lower()
            encontrado = True

            for produto in produtos:
                if produto["nome"].lower() == produto_busca:
                    print("Produto:", produto["nome"])
                    print("Preço:", produto["preco"])
                    print("Quantidade:", produto["quantidade"])
                    print("Categoria:", produto["categoria"])
                    encontrado = False

            if encontrado:
                print("Produto não encontrado.")


        case 4:
            print("Análise de estoque:")
            print("Produtos cadastrados:", len(produtos))

            # Compara valores do estoque e exibe
            valor_total = 0
            for produto in produtos:
                valor = produto["preco"] * produto["quantidade"]
                valor_total = valor_total + valor
            print("\nValor total do estoque:", valor_total)

            # Atribui o primeiro valor para a variável e compara com os outros com o laço
            maior = produtos[0]["preco"]
            nome_produto = produtos[0]["nome"]
            for produto in produtos:
                if produto["preco"] > maior:
                    maior = produto["preco"]
                    nome_produto = produto["nome"]
            print("\nProduto com maior preço:")
            print("Produto:", nome_produto)
            print("Preço:", maior)

            # Atribui o primeiro valor para a variável e compara com os outros com o laço
            menor = produtos[0]["quantidade"]
            nome = produtos[0]["nome"]
            for produto in produtos:
                if produto["quantidade"] > menor:
                    menor = produto["quantidade"]
                    nome = produto["nome"]
            print("\nProduto com menor quantidade:")
            print("Produto:", nome)
            print("Quantidade:", menor)

            # Percorre todos os produtos e adiciona na variável de contagem
            valor_total_estoque = 0
            for produto in produtos:
                valor = produto["quantidade"]
                valor_total_estoque = valor_total_estoque + valor
            print("\nQuantidade total em estoque:", valor_total_estoque)


        case 5:
            # Cria uma nova lista e altera a ordem dos itens para usar o sort e ordenar pelo preço
            print("Preços ordenados:")
            ordem = []
            for produto in produtos:
                ordem.append((produto["preco"], produto)) #Uso de tupla
        
            ordem.sort()
            for preco, produto in ordem:
                print("\nProduto:", produto["nome"])
                print("Preço:", produto["preco"])
                print("Quantidade:", produto["quantidade"])
                print("Categoria:", produto["categoria"])

        case 6:
            # Percorre os produtos e deleta caso o nome digitado tenha sido encontrado
            produto_busca = input("Digite o nome do produto:").strip().lower()
            encontrado = True
            for produto in produtos:
                if produto["nome"].lower() == produto_busca:
                    produtos.remove(produto)
                    print("Produto removido")
                    encontrado = False

            if encontrado:
                print("Produto não encontrado")

        case 7:
            print("Saindo")
            menu = False


        case _:
            print("Opção inválida")
