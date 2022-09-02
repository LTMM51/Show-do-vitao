#Importar as bibliotecas nescessarias pra rodar tudo direitinho
from tela_login import tela_login
import time
import random
import os
from gera_pergunta import gera_pergunta
tela_login()

#Definindo algumas variaveis para que possamos usar no futuro
pergunta_respondida = 0
cerebro = False
ja_foi_perg = []
rank = []
quao_longe = 0
conteudo = "oi"
lista = []
dicio = {}
resposta = []
pergunta = []

#Abrir os arquivos de texto tanto dos ranques quanto das perguntas e respostas
ranques = open("rank.txt", "r", encoding="utf-8")
lista_perguntas = open("perguntas.txt", "r", encoding="utf-8")
#Cria a lista de perguntas organizando cada pergunta com suas respectivas alternativas em um dicionario
for niveis in range(16):
    habilidade = ranques.readline()
    habilidade = habilidade.replace("\n","")
    rank.append(habilidade)
    
lista = gera_pergunta()

print(lista)
#Começo do jogo e apresentação
print('OLÁ JOGADOR!!!!! \nBem-Vindo ao show do vitão \nJá conhece o jogo? (S/N)')
while not cerebro:
    conhece = input()
    if conhece == 'N':
      print('Ora, então eu lhe explico \nO jogo é bem simples, irá aparecer na sua tela uma pergunta e quatro opções de resposta \nMas cuidado, apenas uma delas é verdadeira')
      cerebro = True
    elif conhece == 'S':
      print('Beleza então, vai la Einstein')
      cerebro = True 
    else:
      print('por favor eu apenas entendo S ou N, meu criador não pensou nessa opção')
print('\n\n\n\nUM!!!!\nDOIS!!!\nTRÊS!!!\ne que vitão esteja com você')
time.sleep(2.5)
nome = input('\n\n\nPARA PARA PARA, você é rápido mas ainda não me disse seu nome\nPosso saber qual é? ')

#Sitema de impressão e checagem de perguntas
while (len(ja_foi_perg) !=15) and cerebro == True:
    correto =1
    ja_foi_resp = []
    questão = random.randint(1,len(lista)-1)
    if ja_foi_perg.count(questão)==0:
        print(f'\nentão vamos para a proxima pergunta, {nome} ')
        for p in range (len(lista[questão]['pergunta'])):
            print(lista[questão]['pergunta'][p])
        ja_foi_perg.append(questão)
    else:
        continue
    while not len(ja_foi_resp) ==4:
        alternativa = random.randint(0,3)
        if ja_foi_resp.count(alternativa)==0 and alternativa == 0:
            print(f"{correto}- {lista[questão]['resposta'][alternativa]}")
            ja_foi_resp.append(alternativa)
            certo = correto
            correto += 1
        elif ja_foi_resp.count(alternativa)==0 and alternativa != 0:
            print(f"{correto}- {lista[questão]['resposta'][alternativa]}")
            ja_foi_resp.append(alternativa)
            correto += 1
        else:
            continue
    chute = int(input("\nE então? Qual sua resposta?\n"))
    if certo == chute:
        print("PARABENS VOCE ACERTOU")
        time.sleep(2.5)
        os.system('cls')
        quao_longe +=1
    else:
        print(f"Não foi dessa vez\nA resposta certa era:{certo}- {lista[questão]['resposta'][0]}")
        print(f'Seu ranque é {rank[quao_longe]}')
        cerebro = False
