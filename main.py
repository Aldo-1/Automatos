from modules.DFA import AutomatoFinitoDeterministico
from modules.NFA import AutomatoFinitoNãoDeterministico
from modules.ler import *


def init(dfa, nfa):
  while(True):
    escolha = input('1) Ler arquivo de DFA e testar'+'\n'+ '2) Ler arquivo de NFA, transformar para DFA e testar' + '\n' + '0) Finalizar ' + '\n')
    if(escolha == '1'):
      estadoFinal = lerEstadoFinal('dfa.txt')
      estadoInicial = lerEstadoInicial('dfa.txt')
      alfabetoDFA = lerAlfabeto('dfa.txt')
      automatoDFA = lerAutomatoDFA('dfa.txt')
      while(True):
        print('Alfabeto da maquina ', alfabetoDFA, ' divirta-se!')
        palavra = input('Digite a palavra para testar:(-1 sai do programa) = ')
        if(palavra == '-1'):
          break
        else:
          print(dfa.checkIsAcceptedDFA(automatoDFA, estadoInicial, estadoFinal , palavra))
    elif(escolha == '2'):
      estadoFinalNFA = lerEstadoFinal('nfa.txt')
      estadoInicialNFA = lerEstadoInicial('nfa.txt')
      alfabetoNFA = lerAlfabeto('nfa.txt')
      automatoNFA = lerAutomatoNFA('nfa.txt')
      automatoNFA = nfa.transform(automatoNFA, alfabetoNFA, estadoInicialNFA)
      while(True):
        print('Alfabeto da maquina ', alfabetoNFA, ' divirta-se!')
        palavra = input('Digite a palavra para testar:(-1 sai do programa) = ')
        if(palavra == '-1'):
          break
        else:
          print(nfa.checkIsAcceptedNFA(automatoNFA, estadoInicialNFA, estadoFinalNFA , palavra))
    else:
      break


dfa = AutomatoFinitoDeterministico()
nfa = AutomatoFinitoNãoDeterministico()


init(dfa,nfa)

