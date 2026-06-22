#=========================================
# aula 02 - estrutura de dados
# professor: seu guia Python DeepSeek
# ========================================

#-----------------------------------------
# PARTE 1: LISTAS
#-----------------------------------------

print ("="* 50)
print ("LISTAS")
print ("="* 50)

# criando listas
frutas = ["maçã", "banana", "laranja", "uva", "pera"]
print("lista de frutas:", frutas)

print ("="* 50)

# acessando elementos (índice começa em 0)
print("\nPrimeira fruta", frutas[0])
print("última fruta:", frutas[-1])
print("Duas primeiras frutas:", frutas[0:2])

print ("="* 50)

# adcionar elementos
frutas.append ("morango") # adicionar no final
print("\nApos append:", frutas)

frutas.insert(1, "abacaxi") # adcionar na posição 
print("\nApós insert", frutas)

print ("="* 50)

# 1 removendo elementos

print("antes de remover fruta:", frutas)
frutas.remove("banana")
print("após remover banana:", frutas)
frutas.remove("pera")
print("após remover pera:", frutas)
ultima_fruta = frutas.pop() #remove e retorna o ultimo remover o ultimo variavel seguida de pop()
print("Fruta removida:", ultima_fruta)
print("lista atual:", frutas)

print ("="* 50)

# verificar tamanho 
print ("\nTamanho da lista", len(frutas))
print ("="* 50)

# verificando se existe
print("'uva' esta listada?","uva" in frutas)
print("'morango' esta listada?","morango" in frutas)
# --------------------------------------------
# PARTE 2: TUPLAS
# --------------------------------------------

print("\n" + "=" * 50)
print("TUPLAS")
print("=" * 50)

#criando tuplas (imutáveis)
coordenadas = (10, 20)
cores_rgb =(255,128,0)

print("coordenadas:", coordenadas)
print("x =",coordenadas[0])
print("Y =",coordenadas[1])

#Tupla de um elemento (atenção á vírgula!)
unidade = (1,)
print("\nTupla de um elemento:", unidade)

# Tentar modificar uma tupla (vai da erro - comentando)
#coordenadas [0] = 15  # descomentar para ver o erro 

# convertendo lista para tupla
lista_numeros = [1, 2, 3, 4, 5]
tupla_numeros = tuple(lista_numeros)
print("\nLista:", lista_numeros)
print("convertida para tupla:", tupla_numeros)

#---------------------------------------
# parte 3 dicionário
#---------------------------------------

print("\n" + "=" * 50)
print("DICIONÁRIOS")
print("=" * 50)

#criando dicionário

pessoa = {
    "nome": "joão silva",
    "idade": 25,
    "cidade": "são paulo",
    "profissão": "programador"
}

print("Dicionário pessoas:", pessoa)

print("\nNome:", pessoa["nome"])
print("Idade:", pessoa["idade"])
print("Cidade:", pessoa["cidade"])
print("Profissão:", pessoa["profissão"])

# adicionar valores 

print("\nAdicionando valores ao dicionário")
pessoa["email"] = "joao@email.com" #adcionar uma chave
pessoa["idade"] = 26 # alterar valor existente
print("\nApós modificaçoes:", pessoa)

# removendo valores
email = pessoa.pop("email") # remove e retorna 
print("\nEmail removido:", email)
del pessoa["profissão"] # remove sem retornar
print("\nApós remoção da profissão:", pessoa)

# verificando chaves
print("'email' existe?", "email" in pessoa)
print("'nome' existe?", "nome" in pessoa)
print("-" * 50)
#listando chaves e valores
print("\nChaves do dicionário:", pessoa.keys())
print("Valores do dicionário:", pessoa.values())
print("Itens do dicionário:", pessoa.items())
print("-" * 50)
print("\nChaves do dicionário:", list(pessoa.keys()))
print("Valores do dicionário:", list(pessoa.values()))
print("Itens do dicionário:", list(pessoa.items()))

# --------------------------------------------
# PARTE 4: PERCORRENDO ESTRUTURAS
# --------------------------------------------

print("\n" + "=" * 50)
print("PERCORRENDO ESTRUTURAS")
print("=" * 50)

# percorrendo listas
print("\nPercorrendo lista de frutas:")
for fruta in frutas:
    print(f" - {fruta}") 


#percorndo lista de frutas
print("\nLista de frutas :")
for i, fruta in enumerate(frutas):
    print(f" posição {i}: {fruta}")

# TESTES
print("\nfrutas com índice:")
for i, fruta in enumerate(frutas):
    print(f" posição {i}: {frutas[i]}")


# Percorendo dicionário
print("\nDados de pessoas:")
for chave, valor in pessoa.items():
    print(f" {chave}: {valor}")

#--------------------------------------------
# PARTE 5: listas aninhadas
#-------------------------------------------- 

print("\n" + "=" * 50)
print("LISTAS ANINHADAS")
print("=" * 50)

# matriz lista de lista 
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matriz:")
for linha in matriz:
    print(f" {linha}")

print("\nElementos [0][0]:", matriz[0][0])
print("Elementos [1][2]:", matriz[1][2])
print("Elementos [2][1]:", matriz[2][1])

# --------------------------------------------
# PARTE 6: EXERCÍCIO PRÁTICO
# --------------------------------------------

print("\n" + "=" * 50)
print("EXERCÍCIO: CADASTRO DE ALUNOS")
print("=" * 50)

#lista de dicionários (cada aluno é um dicionário)
alunos = [
    {"nome": "Ana", "notas": [8.5, 7.0, 9.5]},
    {"nome": "Bruno", "notas": [6.0, 7.5, 8.0]},
    {"nome": "Carla", "notas": [9.0, 8.5, 7.5]}
    
]

# função para calcular a media
def calcular_media(notas):
    return sum(notas) / len(notas)

# funçã para determinar status

def definir_status(media):
    if media >= 7.0:
        return "Aprovado"
    elif media >= 5.0:
        return "Recuperação"
    else:
        return "Reprovado"

print("\n  boletin escolar:")
print("-" * 50)

for aluno in alunos:
    media = calcular_media(aluno["notas"])
    status = definir_status(media)

    print(f"Aluno: {aluno['nome']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")
    print("-" * 50)


# PARTE 7: DESAFIO 
print("""
Crie um programa que:

1. Armazene contatos em um dicionário
   Exemplo: contatos = {"João": "9999-9999"}

2. Permita:
   - Adicionar contato
   - Remover contato
   - Buscar contato
   - Listar todos os contatos

3. O programa deve ter um menu interativo:
   1 - Adicionar contato
   2 - Remover contato
   3 - Buscar contato
   4 - Listar contatos
   5 - Sair
""")