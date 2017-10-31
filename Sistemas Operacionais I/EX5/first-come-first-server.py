'''FIRST COME FIRST SERVER'''
#Simulando o funcionamento do escalonador FCFS em Python

import time     #Módulo para haver controle de tempo

processos = []      #Lista que conterá os processos

cont = 1

cont = int(input('\nInsira o número de processos: '))     #É solicitado o número de
#processos para o usuário

for x in range(cont):
    processos.append(int(input('Processo[%d]: ' %(x+1))))

temp_esp = 0
turn = 0
temp_esp_med = 0
turn_med = 0

print('\n----------------------------------------------------------------------------\nProcesso\tCiclo de CPU\tTempo de espera\t\tTempo de retorno\n----------------------------------------------------------------------------')
for x in range(cont):
    turn += processos[x]
    turn_med += turn
    print('[%d]\t\t%d\t\t%d\t\t\t%d' %(x+1, processos[x], temp_esp, turn))
    temp_esp_med += temp_esp
    temp_esp += processos[x]

print('\nTempo de espera médio: %d' %(temp_esp_med/cont))
print('Turnaround médio: %d' %(turn_med/cont))
