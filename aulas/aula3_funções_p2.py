print ("="* 50)
print ("funções parte 2")
print ("="* 50)

#lambida parametros : expressão

#função normal
def dobrar(x):
    return x * 2

#função lambda equivalente
dobrar_lambda = lambda x: x * 2
print(dobrar(5)) # chamando a função normal
print(dobrar_lambda(5)) # chamando a função lambda

print ("-"* 50)

#multiplos parâmetros
def somar(a, b):
    return a + b

somar_lambda = lambda a, b: a + b
print(somar(5, 3)) # chamando a função normal
print(somar_lambda(5, 3)) # chamando a função lambda

print ("-"* 50)

# usando lambida com listas 
numeros = [1, 2, 3, 4, 5]
#filtrar números pares
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(f"Números pares: {pares}") # [2, 4, ...]

print ("-"* 50)
#multiplicar todos por 2
dobrados = list(map(lambda x: x * 2, numeros))

print(f"Números dobrados: {dobrados}") # [2, 4, 6, 8, 10]
print ("-"* 50)

print ("="* 50)
print ("*args - argumentos variáveis posicionais")
print ("="* 50)

def somar_todos(*args):
    total = 0
    for numero in args:
        total += numero
    return total

print(somar_todos(1, 2, 3)) # 6
print(somar_todos(10, 20, 30, 40)) # 100
print(somar_todos(5))# 5
print(somar_todos()) # 0

print ("★"* 50)

# outro exemplo de função com *args

def listar_itens(*args):
    for item in args:
        print(f"- {item}")

listar_itens("maçã", "banana", "laranja")
#maçã
#banana
#laranja
print ("★"* 50)

#kwargs - argumentos variáveis nomeados
def exibir_dados(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

exibir_dados(nome="Alice", idade=30, cidade="São Paulo")

#nome: Alice
#idade: 30
#cidade: São Paulo
print ("★"* 50)

# usando com outro parametros:

def cadastrar_usuario(nome, **dados):
    print(f"Nome: {nome}")
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

cadastrar_usuario("lee", idade=7, cidade="são paulo", profissao="tegnologo em formação")

#Nome: lee
#idade: 7
#cidade: são paulo
#profissao: tegnologo em formação

print ("-"* 50)

cadastrar_usuario("aline", idade=6, cidade="são paulo", profissao="estudante")

print ("★"* 50)

# misturando tudo!

def super_funcao(obrigadotorio, *args, opcional="padrão", **kwargs):
    print(f"Obrigatório: {obrigadotorio}")
    print(f"Argumentos posicionais: {args}")
    print(f"Argumento opcional: {opcional}")
    print(f"Argumentos nomeados: {kwargs}")

super_funcao("azafie", 1, 2, 3, opcional="alterado", cidade="São Paulo", idade="39")

print ("★"* 50)
print ("funções dentro de funções")
print ("★"* 50)

def calculadora(operacao):
    def somar(a, b):
        return a + b

    def subtrair(a, b):
        return a - b

    if operacao == "+":
        return somar
    elif operacao == "-":
        return subtrair
    else:
        return None
    
# usando a função calculadora para obter a função desejada
funcao_escolida = calculadora("+")
resultado = funcao_escolida(10, 5) # chamando a função retornada
print(f"Resultado: {resultado}")
