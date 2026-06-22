# ============================================
# DESAFIO: AGENDA DE CONTATOS
# ============================================

print("\n" + "=" * 50)
print("AGENDA DE CONTATOS - DESAFIO")
print("=" * 50)

# Dicionário para armazenar os contatos
contatos = {}

def exibir_menu():
    """Exibe o menu principal"""
    print("\n" + "=" * 40)
    print(" AGENDA DE CONTATOS")
    print("=" * 40)
    print("1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Listar todos os contatos")
    print("5 - Sair")
    print("=" * 40)

def adicionar_contato():
    """Adiciona um novo contato"""
    nome = input("\nNome do contato: ").strip()
    if nome in contatos:
        print(f" Contato '{nome}' já existe!")
        return
    
    telefone = input("Telefone: ")
    contatos[nome] = telefone
    print(f" Contato '{nome}' adicionado com sucesso!")

def remover_contato():
    """Remove um contato existente"""
    nome = input("\nNome do contato a remover: ").strip()
    if nome in contatos:
        confirmar = input(f"Tem certeza que quer remover '{nome}'? (s/n): ")
        if confirmar.lower() == 's':
            contatos.pop(nome)
            print(f"✅ Contato '{nome}' removido!")
    else:
        print(f" Contato '{nome}' não encontrado!")

def buscar_contato():
    """Busca um contato pelo nome"""
    nome = input("\nNome do contato a buscar: ").strip()
    if nome in contatos:
        print(f" {nome}: {contatos[nome]}")
    else:
        print(f" Contato '{nome}' não encontrado!")

def listar_contatos():
    """Lista todos os contatos"""
    if not contatos:
        print("\n Nenhum contato cadastrado!")
        return
    
    print("\n LISTA DE CONTATOS:")
    print("-" * 30)
    for nome, telefone in contatos.items():
        print(f"   {nome}: {telefone}")
    print("-" * 30)
    print(f"Total: {len(contatos)} contatos")

# Programa principal
def agenda_principal():
    """Função principal da agenda"""
    while True:
        exibir_menu()
        opcao = input("\nEscolha uma opção (1-5): ")
        
        if opcao == '1':
            adicionar_contato()
        elif opcao == '2':
            remover_contato()
        elif opcao == '3':
            buscar_contato()
        elif opcao == '4':
            listar_contatos()
        elif opcao == '5':
            print("\n Saindo da agenda... Até logo!")
            break
        else:
            print("\n Opção inválida! Tente novamente.")

# Executar a agenda
agenda_principal()