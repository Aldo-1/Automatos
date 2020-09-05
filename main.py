from modules.DFA import AutomatoFinitiDeterministico
from modules.ler import *

def init(automato, estadoInicial, estadoFinal, dfa):
  while(True):
    escolha = input('1) Ler arquivo de DFA e testar'+'\n'+ '0) Finalizar ' + '\n')
    if(escolha == '1'):
      while(True):
        palavra = input('Digite a palavra para testar:(-1 sai do programa) = ')
        if(palavra == '-1'):
          break
        else:
          print(dfa.checkIsAccepted(automato, estadoInicial, estadoFinal , palavra))
    else:
      break

estadoFinal = lerEstadoFinal('dfa.txt')
estadoInicial = lerEstadoInicial('dfa.txt')
automato = lerAutomatoDFA('dfa.txt')

dfa = AutomatoFinitiDeterministico()

init(automato,estadoInicial, estadoFinal, dfa)

