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
 
def cadastrar():
    try:
        id = int(input("Digite o ID: "))
        for i in produtos:
            if i["id"] == id:
                raise ValueError("o ID já existe")
 
        nome = input("Digite o nome do produto: ").strip()
        if nome == "":
            raise ValueError("o nome do produto não pode ser vazio.")
 
        categoria = input("Digite a categoria: ").strip()
        if categoria == "":
            raise ValueError("a categoria do produto não pode ser vazio.")
 
        preco = float(input("Informe o preço: "))
        if preco < 0:
            raise ValueError("o preço não pode ser negativo.")
 
        estoque = int(input("Informe o estoque: "))
        if estoque <= 0:
            raise ValueError("o estoque não pode ser menor ou igual a zero.")
 
        novo_produto = {
            "id": id,
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
             "estoque": estoque
        }
 
        produtos.append(novo_produto)
        print("O produto foi cadastrado!")
               
    except ValueError as e:
        print("Erro ao cadastrar:", e)

 
def listar():
    try:
        if len(produtos) == 0:
            raise ValueError("não existem produtos cadastrados")
        else:
            for produto in produtos:
                print("\nID: ", produto["id"])
                print("Produto: ", produto["nome"])
                print("Categoria: ", produto["categoria"])
                print("Preço: ", produto["preco"])
                print("Estoque: ", produto["estoque"])
    except ValueError as e:
        print("Erro ao listar:", e)
               
def consultar():
    try:
        id = int(input("Informe o ID do produto que deseja consultar: "))
        encontrado = False
        for produto in produtos:
            if produto["id"] == id:
                print("\nID: ", produto["id"])
                print("Produto: ", produto["nome"])
                print("Categoria: ", produto["categoria"])
                print("Preço: ", produto["preco"])
                print("Estoque: ", produto["estoque"])
                encontrado = True

        if not encontrado:
            raise ValueError("ID não encontrado.")
    except ValueError as e:
        print("Erro:", e)
 
def alterar():
    try:
        id = int(input("Informe o ID do produto que deseja alterar:"))
        for produto in produtos:
            if produto["id"] == id:
                print("1 - Nome")
                print("2 - Categoria")
                print("3 - Preço")
                print("4 - Estoque")
                campo = int(input("Informe o campo que você deseja alterar: "))
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

                    case _:
                        raise ValueError("opção inválida")    
                                       
    except ValueError as e:
        print("Erro ao alterar:", e)
 
def excluir():
    try:
        produto_busca = int(input("Informe o ID do produto que deseja excluir:"))
        encontrado = False
        for produto in produtos:
            if produto["id"] == produto_busca:
                produtos.remove(produto)
                print("Produto removido com sucesso!")
                encontrado = True

        if not encontrado:
            raise ValueError("ID do produto não encontrado")
    except ValueError as e:
        print("Erro ao excluir:", e)
                           
while True:  
 
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