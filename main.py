# lista de nomes
nomes = []

# loop
while True:
    # menu
    print('1- Inserir novo nome: ')
    print('2- Exibir lista de nomes.')
    print('3- Exibir em ordem alfabética.')
    print('4- Sair do programa.')

    # opção do usuário
    opcao = input('Opção do usuário: ')

    # verifica a opção
    match opcao:
        case '1':
            novo_nome = input('Insira novo nome: ').capitalize()
            nomes.append(novo_nome)
            print(f'{novo_nome} inserido com sucesso')
            continue
        case '2':
            print('\nLISTA DE NOMES\n')
            for nome in nomes:
                print(nome)
            continue    
        case '3': 
            nomes.sort()
            for nome in nomes:
                print(nome)
            print('Lista ordenada com sucesso.')
            continue
        case '4':
            print('Programa encerrado.')
            break