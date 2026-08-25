# Lista inicial de produtos do sistema
produtos = [
    {
    "id": 1,
    "nome": "Notebook",
    "preco": 4500.0,
    "estoque": 10,
    "categoria": "Informática"
    },
    {
    "id": 2,
    "nome": "Mouse",
    "preco": 80.0,
    "estoque": 15,
    "categoria": "Periféricos"
    },
    {
    "id": 3,
    "nome": "Teclado",
    "preco": 250.0,
    "estoque": 7,
    "categoria": "Periféticos"
    },
    {
    "id": 4,
    "nome": "Monitor",
    "preco": 500.0,
    "estoque": 6,
    "categoria": "Informática"
    },
    {
    "id": 5,
    "nome": "Impressora",
    "preco": 3500.0,
    "estoque": 16,
    "categoria": "Informática"
    }
]

# Função usada para cadastrar um novo produto
def cadastrar():
    try:
        id = int(input("Digite o ID: "))
        # Antes de cadastrar, verifica se o ID já está sendo usado
        for i in produtos:
            if i["id"] == id:
                raise ValueError("o ID já existe")
                
        # Pede o nome e verifica se o usuário realmente informou algum valor
        nome = input("Digite o nome do produto: ").strip()
        if nome == "":
            raise ValueError("o nome do produto não pode ser vazio.")
            
         # Faz a mesma validação para a categoria
        categoria = input("Digite a categoria: ").strip()
        if categoria == "":
            raise ValueError("a categoria do produto não pode ser vazio.")

        # O preço precisa ser um número e não pode ser negativo
        preco = float(input("Informe o preço: "))
        if preco < 0:
            raise ValueError("o preço não pode ser negativo.")

        # O estoque precisa ter pelo menos um produto
        estoque = int(input("Informe o estoque: "))
        if estoque <= 0:
            raise ValueError("o estoque não pode ser menor ou igual a zero.")

        # Cria um novo produto com os dados informados
        novo_produto = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
             "estoque": estoque
        }

        # Adiciona o novo produto na lista
        produtos.append(novo_produto)
        print("O produto foi cadastrado!")

    # Caso alguma informação esteja errada, mostra a mensagem de erro
    except ValueError as e:
        print("Erro ao cadastrar:", e)

# Função que mostra todos os produtos cadastrados
def listar():
    try:
        # Verifica se existe algum produto na lista
        if len(produtos) == 0:
            raise ValueError("não existem produtos cadastrados")
        else:
            # Percorre a lista e mostra os dados de cada produto
            for produto in produtos:
                print("\nID: ", produto["id"])
                print("Produto: ", produto["nome"])
                print("Categoria: ", produto["categoria"])
                print("Preço: ", produto["preco"])
                print("Estoque: ", produto["estoque"])
    except ValueError as e:
        print("Erro ao listar:", e)

# Função usada para procurar um produto pelo ID
def consultar():
    try:
        id = int(input("Informe o ID do produto que deseja consultar: "))
        encontrado = False
        # Procura na lista o produto que possui o ID informado
        for produto in produtos:
            if produto["id"] == id:
                print("\nID: ", produto["id"])
                print("Produto: ", produto["nome"])
                print("Categoria: ", produto["categoria"])
                print("Preço: ", produto["preco"])
                print("Estoque: ", produto["estoque"])
                # Marca que o produto foi encontrado
                encontrado = True

        # Se terminou a busca e não encontrou o ID, mostra um erro
        if not encontrado:
            raise ValueError("ID não encontrado.")
    except ValueError as e:
        print("Erro:", e)

# Função para alterar alguma informação de um produto
def alterar():
    try:
        id = int(input("Informe o ID do produto que deseja alterar:"))
        # Procura o produto que será alterado
        for produto in produtos:
            if produto["id"] == id:
                # Mostra as opções de alteração
                print("1 - Nome")
                print("2 - Categoria")
                print("3 - Preço")
                print("4 - Estoque")
                campo = int(input("Informe o campo que você deseja alterar: "))
                # Dependendo da opção escolhida, altera um campo diferente
                match campo:
                    case 1:
                        novo_nome = input("Informe o novo nome: ").strip()
                        if novo_nome == "":
                            raise ValueError("o nome não pode ser vazio")
                        produto["nome"] = novo_nome
                        print("Nome alterado com sucesso!")
                    case 2:
                        nova_categoria = input("Informe a nova categoria: ").strip()    
                        if nova_categoria == "":
                            raise ValueError("a categoria não pode ser vazio")
                        produto["categoria"] = nova_categoria 
                        print("Categoria alterada com sucesso!")                                                                         
                    case 3:
                        novo_preco = float(input("Informe o novo preço: "))
                        if novo_preco < 0:
                            raise ValueError("o preço não pode ser inferior a 0.")
                        produto["preco"] = novo_preco
                        print("Preço alterado com sucesso!")
                       
                    case 4:
                        novo_estoque = int(input("Informe o novo estoque: "))
                        if novo_estoque <= 0:
                            raise ValueError("o estoque não pode ser inferior a 0.")
                        produto["estoque"] = novo_estoque
                        print("Estoque alterado com sucesso!")

                    # Caso o usuário escolha uma opção que não existe
                    case _:
                        raise ValueError("opção inválida")    
                                       
    except ValueError as e:
        print("Erro ao alterar:", e)

# Função responsável por excluir um produto da lista
def excluir():
    try:
        produto_busca = int(input("Informe o ID do produto que deseja excluir:"))
        encontrado = False
        # Procura o produto pelo ID
        for produto in produtos:
            if produto["id"] == produto_busca:
                # Remove o produto encontrado da lista
                produtos.remove(produto)
                print("Produto removido com sucesso!")
                encontrado = True

        if not encontrado:
            raise ValueError("ID do produto não encontrado")
    except ValueError as e:
        print("Erro ao excluir:", e)

# O sistema fica rodando até o usuário escolher a opção de sair
while True:  

    # Exibe o menu principal
    print("\n========================================")
    print("          CRUD DE PRODUTOS")
    print("========================================")
    print("1 - Cadastrar produto")
    print("2 - Listar produtos")
    print("3 - Buscar produto")
    print("4 - Atualizar produto")
    print("5 - Excluir produto")
    print("6 - Sair")
    print("========================================")
 
    op = int(input("Escolha uma opção do menu: "))
    # Chama a função de acordo com a opção escolhida
    match op:
        case 1:
            cadastrar()
        case 2:
            listar()
        case 3:
            consultar()
        case 4:
            alterar()
        case 5:
            excluir()
        case 6:
            print("Saindo...")
            break
 
        case _:    
            print("Opção inválida.")
