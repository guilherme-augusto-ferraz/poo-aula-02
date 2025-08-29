class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_info(self):
        return f"Cliente: {self.nome} | Email: {self.email}"


class ClienteVIP(Cliente):
    def __init__(self, nome, email, desconto=0.1):
        super().__init__(nome, email)
        self.desconto = desconto  # 10% por padrão

    def calcular_desconto(self, valor):
        return valor * (1 - self.desconto)


class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_info(self):
        return f"{self.nome} - R${self.preco:.2f}"


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []

    def adicionar_produto(self, produto):
        self.itens.append(produto)

    def calcular_total(self):
        total = sum([p.preco for p in self.itens])
        if isinstance(self.cliente, ClienteVIP):
            total = self.cliente.calcular_desconto(total)
        return total

    def exibir_pedido(self):
        print("\n--- Pedido ---")
        print(self.cliente.exibir_info())
        print("Itens:")
        for p in self.itens:
            print(f" - {p.exibir_info()}")
        print(f"Total: R${self.calcular_total():.2f}")
        print("--------------\n")


# ============================
# Menu de Linha de Comando
# ============================

clientes = []
produtos = [ # Inicia o Array com alguns produtos já cadastrados
    Produto("Camisa", 50.0),
    Produto("Calça", 120.0),
    Produto("Tênis", 300.0)
]
pedidos = []

while True:
    print("===== Sistema de Vendas =====")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Clientes")
    print("3 - Criar Pedido")
    print("4 - Listar Produtos")
    print("5 - Listar Pedidos")
    print("0 - Sair")

    opcao = input("Escolha: ")

    # Cadastrar Cliente
    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")
        tipo = input("Cliente VIP? (s/n): ").lower()
        if tipo == "s":
            clientes.append(ClienteVIP(nome, email))
        else:
            clientes.append(Cliente(nome, email))
        print("Cliente cadastrado com sucesso!\n")

    # Listar Clientes
    elif opcao == "2":
        for i, c in enumerate(clientes):
            print(f"{i} - {c.exibir_info()}")
        print()

    # Criar Pedido
    elif opcao == "3":
        if not clientes:
            print("Cadastre um cliente primeiro!\n")
            continue

        # escolher cliente
        for i, c in enumerate(clientes):
            print(f"{i} - {c.exibir_info()}")
        idx = int(input("Escolha o cliente: "))
        cliente = clientes[idx]
        pedido = Pedido(cliente)

        # adicionar produtos
        while True:
            for i, p in enumerate(produtos):
                print(f"{i} - {p.exibir_info()}")
            idx_p = int(input("Escolha produto (-1 para finalizar): "))
            if idx_p == -1:
                break
            pedido.adicionar_produto(produtos[idx_p])

        pedidos.append(pedido)
        print("Pedido criado com sucesso!\n")

    # Listar Produtos
    elif opcao == "4":
        for p in produtos:
            print(p.exibir_info())
        print()

    # Listar Pedidos
    elif opcao == "5":
        for pedido in pedidos:
            pedido.exibir_pedido()

    # Sair
    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
