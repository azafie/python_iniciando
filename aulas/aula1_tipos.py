# ===========================================
# aula 01 - tipos de dados
# professor: seu guia Python DeepSeek
# ===========================================

# -------------------------------------------
# 1 variaveis e tipos primitivos
# -------------------------------------------

# inteiro (int)
idade = 23
print("idade:", idade)
print("tipos de idade:", type(idade))

# float (ponto flutuante)
altura = 1.75
print("\nAltura:", altura)
print("tipos de altura:", type(altura))

# string
nome = "joão"
mensagem = 'olá, python!'
print("\nNome:", nome)
print("mensagem:", mensagem)
print("Tipos de nome:", type(nome))

# booleano (bool)
verdadeiro = True
falso = False

print("\nVerdadeiro:", verdadeiro)
print("Falso:", falso)
print("Tipos de verdadeiro:", type(verdadeiro))

# -------------------------------------------
# 2 entrada e saída de dados
# -------------------------------------------

# print() - exibir informações
print("\n" + "=" * 50)
print("usando o print")
print("=" * 50)

nome_usuario = "maria"
idade_usuario = 30

print(f"olá {nome_usuario}, você tem {idade_usuario} anos!")

# input() - recebe dados do usuário
nome_input = input("\nDigite seu nome: ")

print(f"Bem-vindo(a), {nome_input}!")

# -------------------------------------------
# 3. operadores basicos
# -------------------------------------------

print("\n" + "=" * 50)
print("operadores")

# aritméticos
a = 10
b = 3

print(f"{a} + {b} =", a + b)     # soma
print(f"{a} - {b} =", a - b)     # subtração
print(f"{a} * {b} =", a * b)     # multiplicação
print(f"{a} / {b} =", a / b)     # divisão (sempre float)
print(f"{a} // {b} =", a // b)   # divisão inteira
print(f"{a} % {b} =", a % b)     # resto da divisão
print(f"{a} ** {b} =", a ** b)   # potência

# comparação
print("\nComparações:")

print(f"{a} == {b}?", a == b)   # igual
print(f"{a} != {b}?", a != b)   # diferente
print(f"{a} > {b}?", a > b)     # maior
print(f"{a} < {b}?", a < b)     # menor

# -------------------------------------------
# 4. conversão de tipos (cast)
# -------------------------------------------

print("\n" + "=" * 50)
print("conversão de tipos")
print("=" * 50)

numero_str = "123"

print(f"'{numero_str}' é do tipo:", type(numero_str))

numero_int = int(numero_str)

print("convertido para int:", numero_int, type(numero_int))

numero_float = float(numero_str)

print("convertido para float:", numero_float, type(numero_float))

# -------------------------------------------
# 5. exercício
# -------------------------------------------

print("\n" + "=" * 50)
print("exercício: calculadora simples")
print("=" * 50)

# solicitar números
num1 = float(input("digite o primeiro número: "))
num2 = float(input("digite o segundo número: "))

# calcular
soma = num1 + num2
subtracao = num1 - num2
multiplicacao = num1 * num2

divisao = num1 / num2 if num2 != 0 else "divisão por zero não permitida"

# exibir resultados
print(f"\n{num1} + {num2} = {soma}")
print(f"\n{num1} - {num2} = {subtracao}")
print(f"\n{num1} * {num2} = {multiplicacao}")
print(f"\n{num1} / {num2} = {divisao}")