print ("="* 50)
print ("funções data e hora")
print ("="* 50)


import datetime
#data e hora atual
data_completa = datetime.datetime.now()
data = data_completa.date()
hora = data_completa.time()
print("Data completa:", data_completa)
print("Data:", data)
print("Hora:", hora)

print ("-"* 50)
#data e hora formatada
print("dia",data_completa.day)
print("mês",data_completa.month)
print("ano",data_completa.year)
print("hora",data_completa.hour)
print("minuto",data_completa.minute)
print("segundo",data_completa.second)

print ("-"* 50)
data = datetime.date(2000,9,30)
data = datetime.date(day=30, month=9, year=2000)
print("Data:", data)
print(type(data))

print ("-"* 50)
hora = datetime.time(10,20,35)
print("Hora:", hora)

data = datetime.datetime(2000,9,30,10,20,35)
print("Data e hora:", data)
print ("-"* 50)
# y ano
# m mês
# d dia
# H hora
# M minuto
# S segundo

atual = datetime.datetime.now()
corrente = atual.strftime("%Y-%m-%d %H:%M:%S")
print("Data e hora atual formatada:", corrente)
print(type(corrente))
print ("-"* 50)
# y ano
# m mês
# d dia
# H hora formato 00-23
# M minuto
# S segundo

# A dia da semana
# a dia da semana abreviado
# B mês abreviado
# b mês abreviado
# I hora formato 01-12
# p AM/PM

data = datetime.datetime(2024, 6, 15, 14, 30, 45)
print(atual.strftime("%A  -  %a"))
print(atual.strftime("%B  -  %b"))
print(atual.strftime("%H  -  %I"))
print(atual.strftime("%I  -  %p"))


print ("="* 50)
print ("funções data e hora operaçoes aritimeticas")
print ("="* 50)

data1 = datetime.datetime(2024, 6, 15, 14, 30, 45)
data2 = datetime.datetime(2024, 6, 20, 10, 15, 30)
diferenca = data2 - data1
print("Diferença entre datas:", diferenca)
print(type(diferenca))
print ("-"* 50)

from datetime import timedelta, datetime
data_atual = datetime.now()
data_futura1 = data_atual + timedelta(weeks = 4)
data_futura2 = data_atual + timedelta(days = 30)
data_futura3 = data_atual + timedelta(hours = 12)
data_futura4 = data_atual + timedelta(weeks = 60)
print("Data atual:", data_atual)
print("Data futura 1 (+ 4 semanas):", data_futura1)
print("Data futura 2 (+ 30 dias):", data_futura2)
print("Data futura 3 (+ 12 horas):", data_futura3)
print("Data futura 4 (+ 60 semanas):", data_futura4)

print ("-"* 50)
import datetime


data_2000 = datetime.datetime(2000, 1, 1, 0, 0, 0)
data_agora = datetime.datetime.now()

diferenca = data_agora - data_2000

print("Desde o ano 2000 passaram", diferenca.days, "dias")
print("Segundos restantes:", diferenca.seconds)
print("Microsegundos restantes:", diferenca.microseconds)



