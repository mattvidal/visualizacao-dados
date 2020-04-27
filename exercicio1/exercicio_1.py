import matplotlib.pyplot as plt
import csv

meses = []
casosNovos = []
casosAcumulados = []
obitosNovos = []
obitosAcumulados = []

with open('dadosCovid.txt', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        meses.append(row[0]) #armazenar os meses
        casosNovos.append(int(row[1])) #armazena os casos novos
        casosAcumulados.append(int(row[2])) #armazena os casos acumulados
        obitosNovos.append(int(row[3])) #armazena os óbitos novos
        obitosAcumulados.append(int(row[4])) #armazena os óbitos acumulados

plt.title("Casos COVID-19 na decorrência dos meses")
plt.xlabel("Meses")
plt.ylabel("Número de Casos")

plt.plot(meses, casosNovos, color = 'b', label = "Casos novos")
plt.plot(meses, casosAcumulados, color = 'g', label = "Casos acumulados")
plt.plot(meses, obitosNovos, color = 'r', label = "Óbitos novos")
plt.plot(meses, obitosAcumulados, color = 'c', label = "Óbtos acumulados")
plt.legend()
plt.show()