print ("="* 50)
print ("funçoes basicas")
print ("="* 50)

def nome_dafuncao():
    print("olá!")

nome_dafuncao() #executando a função

print ("="* 50)
print ("funçoes com parametros")
print ("="* 50)

def soma(a, b):
    resultado = a + b
    print(f"A soma de {a} + {b} é: {resultado}")

soma(5, 3) #executando a função com dois parâmetros


def nome_dafuncao_com_parametros(parametro):
    print(f"olá, {parametro}!")

nome_dafuncao_com_parametros("Alice") #executando a função com um parâmetro

print ("="* 50)
print ("retorno de valores com return")
print ("="* 50)

def soma(a, b):
    return a + b

resultado = soma(5, 3)
print(f"O resultado da soma é: {resultado}")    

# print() → mostra no console
#return → devolve o valor para ser usado em outro lugar do código

# com o print ( só mostra )
def doblo_print(x):
    print(x * 2)

# com o return ( devolve o valor )
def dobro_return(x):
    return x * 2

valor1 = doblo_print(5) # não retorna nada, apenas mostra no console
valor2 = dobro_return(5) # retorna o valor, que pode ser usado em outro lugar do código
valor = (valor2 + 3) # aqui podemos usar o valor retornado para fazer outra operação


print ("="* 50)
print ("variaveis globais e locais")
print ("="* 50)

def teste():
    mensagem = "Olá, mundo!" # variável local
    print(mensagem)

teste() # chamando a função, que imprime a variável local
print ("-"* 50)

nome = "pedro" # variável global

def saudacao():
    print(f"Olá, {nome}!") # acessando a variável global


saudacao() # chamando a função, que acessa a variável global    
print ("-"* 50)
# modificando uma variável global dentro de uma função

contador = 0 # variável global

def incrementar():
    global contador # aviso que vou modificar a variável global
    contador += 1

incrementar() # chamando a função, que modifica a variável global em +1
incrementar() # chamando a função, que modifica a variável global em +1
print(f"O valor do contador é: {contador}")

print ("="* 50)
print ("parametros opcionais (valores e padrão)")
print ("="* 50)

def saudaçoes (nome, saudacao="Olá"):
    print(f"{saudacao}, {nome}!")

saudaçoes("Alice") # usando o valor padrão para saudacao
saudaçoes("Bob", "bom dia") # sobrescrevendo o valor padrão para saudaçoes

print ("-"* 50)

# outro exempo 
def calcular_preco(valor, desconto=0):
    return valor - (valor * desconto / 100)

preco1 = calcular_preco(100) # usando o valor padrão para desconto
preco2 = calcular_preco(100, 10) # sobrescrevendo o valor padrão para desconto
print(f"Preço sem desconto: {preco1}")
print(f"Preço com desconto: {preco2}")

print ("-"* 50)

#multiplos retornos (como uma tuplas)

def operacoes(a, b):
    soma = a + b
    subtracao = a - b
    multiplicacao = a * b
    divisao = a / b if b != 0 else None # evitando divisão por zero
    return soma, subtracao, multiplicacao, divisao

resultados = operacoes(10, 5)
print(f"Soma: {resultados[0]}")
print(f"Subtração: {resultados[1]}")
print(f"Multiplicação: {resultados[2]}")
print(f"Divisão: {resultados[3]}")

print ("-"* 50)

s, sub, milt, div = operacoes(20, 4) # desempacotando os valores retornados
print(f"Soma: {s}")
print(f"Subtração: {sub}")
print(f"Multiplicação: {milt}") 
print(f"Divisão: {div}")

print ("-"* 50)

print ("="* 50)
print ("exercicios")
print ("="* 50)

# crie uma função que caulule a média de uma lista de números e retorne o resultado.
# crie uma função receber_salario que recebe o salário e um percentual de 10 % de aumento e retorne o novo salário. 
# crie uma função que recebe uma lista de numeros e retorna o maior e menor valor 
