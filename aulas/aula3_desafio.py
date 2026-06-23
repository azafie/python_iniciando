# crie uma função que caulule a média de uma lista de números e retorne o resultado.
# crie uma função receber_salario que recebe o salário e um percentual de 10 % de aumento e retorne o novo salário. 
# crie uma função que recebe uma lista de numeros e retorna o maior e menor valor 

# função calcular midia
def calcular_media(a, b, c, d):
    media = (a + b + c + d) / 4
    return media

media = calcular_media(7, 8, 9, 10) # chamando a função e passando os valores
print(f"A média dos números é: {media}")

# função receber_salario
def receber_salario(salario, percentual_aumento=10):
    novo_salario = salario + (salario * percentual_aumento / 100)
    return novo_salario

salario = receber_salario(1000) # chamando a função e passando os valores
print(f"O novo salário é: {salario}")   

# função maior e menor valor
def maior_menor(lista):
    maior = max(lista)
    menor = min(lista)
    return maior, menor

numeros = [7, 8, 9, 10]
maior, menor = maior_menor(numeros)
print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")