'''
• efetuar o CRUD de Clientes
• efetuar o CRUD de Motocicletas
• efetuar a venda de Motocicletas
• fornecer listagem de Vendas
• permitir a consulta de uma venda específica, incluindo o cliente e motocicleta
relacionada a mesma'''


def pularLinha():
    print('')


def mostraLinha():
    print('-' * 40)


def titulo(msg):
    mostraLinha()
    print(msg.center(40))
    mostraLinha()


def exibirMenu():
    pularLinha()
    print('1. Cadastrar cliente\n2. Buscar cliente\n3. Listar clientes\n4. Cadastrar veículo\n5. Listar veículos\n6. Sair ')
    pularLinha()


def cadastrarClientes(clientes):

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    pularLinha()
    titulo('CADASTRO DE CLIENTES:')
    identif = int(input('Informe o CPF: '))
    nome = input('Nome completo: ')
    email = input('Email: ')
    #clientes.append((identif, nome, idade))
    #print('Cadastrado realizado com sucesso!')
    #pularLinha()

    # inserindo dados na tabela
    cursor.execute("""
    INSERT INTO Clientes (CPF, nome, email)
    VALUES (?,?,?)
    """, (identif, nome, email))

    conn.commit()

    print('Dados inseridos com sucesso.')

    conn.close()


def listarClientes(clientes):
    pularLinha()
    titulo('LISTA DE CLIENTES CADASTRADOS:')
    #for cliente in clientes: #PARA CADA CLIENTE NA LISTA CLIENTES
    #    identif, nome, idade = cliente
    #    print(f'Nome:{nome} | Idade: {idade} | Id: {identif}')

    import sqlite3

    conn = sqlite3.connect('Loja.db')
    cursor = conn.cursor()

    # lendo os dados
    cursor.execute("""
    SELECT * FROM Clientes;
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()

    pularLinha()


def buscarClientes(clientes):
    pularLinha()
    titulo('BUSCAR CLIENTE')
    identif_desejado = int(input('Informe o Id do cliente: '))
    for cliente in clientes:
        identif, nome, idade = cliente
        if identif == identif_desejado:
            pularLinha()
            titulo('RESULTADO DA CONSULTA:')
            print(f'Nome: {nome}\nIdade: {idade}\nId: {identif}')
            break
    else:
        print(f'Pessoa com ID {identif_desejado} nao encontrada.')
    pularLinha()


def cadastrarMotos(motos):
    pularLinha()
    titulo('CADASTRO DE MOTOCICLETA:')
    identifMoto = int(input('Id: '))
    marca = input('Marca: ')
    modelo = (input('Modelo: '))
    motos.append((identifMoto, marca, modelo))
    print('Cadastrado realizado com sucesso!')
    pularLinha()


def listarMotos(motos):
    pularLinha()
    titulo('LISTA DE MOTOCICLETAS CADASTRADAS:')
    for moto in motos:
        identif, marca, modelo = moto
        print(f'Id: {identif} | Marca: {marca} | Modelo: {modelo}')
    pularLinha()


def iniciarPrograma():
    clientes = []
    motos = []
    while True:
        exibirMenu()
        opcao = int(input('Escolha a opçao: '))
        if opcao == 1:
            cadastrarClientes(clientes)
        elif opcao == 2:
            buscarClientes(clientes)
        elif opcao == 3:
            listarClientes(clientes)
        elif opcao == 4:
            cadastrarMotos(motos)
        elif opcao == 5:
            listarMotos(motos)
        elif opcao == 6:
            print('Programa finalizado!')
            break
        else:
            print('Opção inválida. Tente novamente.')


# Fazer sistema de vendas
# Fazer uma validaçao da entrada de 'opçao'
# Fazer um 'voltar para menu' ou 'finalizar programa' para nao ficar retornando sempre o menu de opçoes completo.


#INÍCIO DO PROGRAMA

titulo('SISTEMA CONCESSIONÁRIA')
iniciarPrograma()





