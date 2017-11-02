'''SHORTEST JOB FIRST - SJF'''

#Simulação do escalonador SJF em Python

import time     #Módulo que fará com que haja delay na execução de alguns processos

processos = []      #Lista que conterá os processos
thrash = []         #Lista em que será inserido os números dos processos já carregados

cont = int(input('\nInsira o número de processos: '))     #É solicitado o número de processos para o usuário

for x in range(cont):       #Será realizado n ciclos, cujo n é o número de processos
    processos.append(int(input('Processo[%d]: ' %(x+1))))       #Este ciclo irá adicionar na lista de processos os números solicitados em cada linha processos.sort()

processos_ord = sorted(processos)    #Declarando uma nova variável que terá os processos organizados por tamanho

temp_esp = 0        #Tempo de espera
turn = 0            #Turnaround
temp_esp_med = 0    #Tempo de espera médio
turn_med = 0        #Tempo de turnaround médio

for x in range(cont):       #Será realizado n ciclos, cujo n é o número de processos

    turn += processos_ord[x]    #O turnaround é o tempo de execução de todo o processo, por isso é somado cada processo um com o outro
    turn_med += turn        #O turnaround médio é o seu total dividido pelo número de processos. A divisão será realizada ao imprimir o resultado na tela

    for d in range(cont):       #Este ciclo faz com que seja mostrado na tela o processo correto em execução
        if processos_ord[x] == processos[d]:
            if d not in thrash:
                num = d + 1
                thrash.append(d)
                break

    print('\n\nCarregando %dº' %(x+1))
    for i in range(processos_ord[x]):
        time.sleep(1)
        print('%d...' %(i+1))
    
    print('\nPROCESSO %d\nCiclo de CPU(Burst): %d\nTempo de espera: %d\nTempo de retorno: %d\n\n------------------------------------------' %(num, processos[x], temp_esp, turn))      #É mostrado na tela os resultados
    temp_esp_med += temp_esp        #O tempo de espera é somado depois porque o seu resultado é tratado com o início de chegada de cada processo
    temp_esp += processos_ord[x]

print('\n||Tempo de espera médio:\t%d' %(temp_esp_med/cont))
print('||Turnaround médio:\t\t%d\n' %(turn_med/cont))
