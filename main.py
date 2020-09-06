from modules.DFA import AutomatoFinitoDeterministico
from modules.NFA import AutomatoFinitoNãoDeterministico



def init(dfa, nfa):
  while(True):
    escolha = input('1) Ler arquivo de DFA e testar'+'\n'+ '2) Ler arquivo de NFA, transformar para DFA e testar' + '\n' + '0) Finalizar ' + '\n')
    if(escolha == '1'):
      while(True):
        print('Alfabeto da maquina ', dfa.alfabeto, ' divirta-se!')
        palavra = input('Digite a palavra para testar: (-1 voltar ao inicio) = ')
        if(palavra == '-1'):
          break
        else:
          print(dfa.checkIsAcceptedDFA(palavra))
    elif(escolha == '2'):  
      print('--------------------Transformação--------------------')
      automatoNFA = nfa.transform()
      print('-----------------------------------------------------')
      while(True):
        print('Alfabeto da maquina ', nfa.alfabeto, ' divirta-se!')
        palavra = input('Digite a palavra para testar: (-1 voltar ao inicio) = ')
        if(palavra == '-1'):
          break
        else:
          print(nfa.checkIsAcceptedNFA(automatoNFA, palavra))
    else:
      break


dfa = AutomatoFinitoDeterministico()
nfa = AutomatoFinitoNãoDeterministico()



init(dfa,nfa)

