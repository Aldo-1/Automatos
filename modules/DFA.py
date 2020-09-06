class AutomatoFinitoDeterministico:
    def checkIsAcceptedDFA(self,automato:dict,estadoInicial, estadoFinal,palavra):
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

    
      
    
      
      
    

    
    
