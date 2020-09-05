class AutomatoFinitiDeterministico:
    #{'q0':{'0':'q1'}}
    def __namingStates__(self, automato:dict):
        _quantidade = 0
        _qtdStates = int(input('Digite quantos estados ira ter o seu automato: '))
        
        while _qtdStates != _quantidade:
          nomeEstado = input('Digite o nome do seu estado ')            
          automato[nomeEstado] = {}
          _quantidade += 1
        return automato
    
    def __setAlphabetic__(self):
        while True:
          alfabeto = input('Digite o alfabeto com virgula ')
          if(alfabeto.find(',') == -1 ):
            print('Digite o alfabeto com virgula !')
            continue
          else:
            break
        return alfabeto.split(',')
    
    def __setStartState__(self,automato:dict):
      while True:
        estadoInicial = input('Digite o estado inicial ')
        if(not(estadoInicial in automato)):
          print('------Digite um estado inicial que exista !-------')
          continue
        else:
          break
      return estadoInicial
        
    def __setEndingState__(self, automato:dict):
      while True:
        estadoFinal = input('Digite o estado final ')
        if(not(estadoFinal in automato)):
          print('------Digite um estado final que exista !-------')
          continue
        else:
          break
      return estadoFinal
    
    def __createAction__(self, automato:dict, alfabetoArray:list):
        dictAcoes = {}
        for estado in automato:
            for letra in alfabetoArray:
              while True:
                acao = input('Quando receber ' + letra + ' em ' + estado + ' ele ira pra onde ?')
                if(not(acao in automato)):
                  print('-----------Digite um estado para ir que exista!-------------')
                  continue
                else:
                  break
              dictAcoes[letra] = acao
            automato[estado] = dictAcoes
            dictAcoes = {}
        return automato

    def __chooseWord__(self, automato:dict, estadoInicial, estadoFinal):
      while(True):
        palavra = input('Escolha a palavra para testar na maquina que voce criou ! (Ou digite -1 para parar!)')
        if(palavra == '-1'):
          return False
        else:
          print(self.__checkIsAccepted__(automato, estadoInicial, estadoFinal, palavra))
    
    def __checkIsAccepted__(self,automato:dict,estadoInicial, estadoFinal,palavra):
      #Iniciando o estado inicial
      estado = estadoInicial
      #Para cada letra do palavra
      for letra in palavra:
        if(not(letra in automato[estado])):
          print('algum caracter da palavra nao existe no alfabeto dessa maquina!')
          break
        else:
          estado = automato[estado][letra]
      if(estado in estadoFinal):
          return 'accept'
      else:
          return 'reject'

    def initProgram(self): 
      automato = {}
      while True:
        automato = self.__namingStates__(automato)
        
        if(len(automato) == 0):
          return False
        
        alfabetoArray = self.__setAlphabetic__()
        automato = self.__createAction__(automato, alfabetoArray)
        estadoInicial = self.__setStartState__(automato)
        estadoFinal = self.__setEndingState__(automato)
        self.__chooseWord__(automato, estadoInicial, estadoFinal)
        return False
      
    
      
      
    

    
    
