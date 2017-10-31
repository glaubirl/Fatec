'''FIRST COME FIRST SERVER'''
#Simulando o funcionamento do escalonador FCFS em Python

processos = []      #Lista que conterá os processos

cont = int(input('\nInsira o número de processos: '))     #É solicitado o número de processos para o usuário

for x in range(cont):       #Será realizado n ciclos, cujo n é o número de processos
    processos.append(int(input('Processo[%d]: ' %(x+1))))       #Este ciclo irá adicionar na lista de processos os números solicitados em cada linha

temp_esp = 0        #Tempo de espera
turn = 0            #Turnaround
temp_esp_med = 0    #Tempo de espera médio
turn_med = 0        #Tempo de turnaround médio

print('\n----------------------------------------------------------------------------\nProcesso\tCiclo de CPU\tTempo de espera\t\tTempo de retorno\n----------------------------------------------------------------------------')
for x in range(cont):       #Será realizado n ciclos, cujo n é o número de processos
    turn += processos[x]    #O turnaround é o tempo de execução de todo o processo, por isso é somado cada processo um com o outro
    turn_med += turn        #O turnaround médio é o seu total dividido pelo número de processos. A divisão será realizada ao imprimir o resultado na tela
    print('[%d]\t\t%d\t\t%d\t\t\t%d' %(x+1, processos[x], temp_esp, turn))      #É mostrado na tela os resultados
    temp_esp_med += temp_esp        #O tempo de espera é somado depois porque o seu resultado é tratado com o início de chegada de cada processo
    temp_esp += processos[x]

print('\nTempo de espera médio: %d' %(temp_esp_med/cont))
print('Turnaround médio: %d' %(turn_med/cont))
