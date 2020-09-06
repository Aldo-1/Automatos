from modules.ler import *

class AutomatoFinitoNãoDeterministico:

  def __init__(self):
      self.estadoFinal = lerEstadoFinal('nfa.txt')
      self.estadoInicial = lerEstadoInicial('nfa.txt')
      self.alfabeto = lerAlfabeto('nfa.txt')
      self.automato = lerAutomatoNFA('nfa.txt')
      self.novoAutomato = {}
  ##Transforma de array para string
  def __transformArrayToString__(self,novoAutomato, alfabeto):
    for estado in novoAutomato:
      for letra in alfabeto:
        paraOndeVai = novoAutomato[estado][letra]
        novoAutomato[estado][letra] = ','.join(paraOndeVai)
    return novoAutomato

  ##aqui ele checa se tem espaco vazio e retorna true ou false
  def __checkEmptySpace__(self,resultado):
    for letra in resultado:
      if(letra == ''):
        return True
      else:
        return False

  ##iniciar o estado inicial
  def __initInicialState__(self,automato, palavras, estadoInicial, novoAutomato):
    for palavra in palavras:
      novoEstados =  ','.join(automato[estadoInicial][palavra])
      novoAutomato[estadoInicial][palavra] = {}
      novoAutomato[estadoInicial][palavra] = automato[estadoInicial][palavra]   
      if(novoEstados != estadoInicial):
        novoAutomato[novoEstados] = {}
      else:
        continue
    return novoAutomato

  ##checar se e aceito
  def checkIsAcceptedNFA(self,novoAutomato, palavra):
        #Iniciando o estado inicial
        estado = self.estadoInicial
        #Para cada letra do palavra
        for letra in palavra:
          if(not(letra in novoAutomato[estado])):
            print('algum caracter da palavra nao existe no alfabeto dessa maquina!')
            break
          else:
            estado = novoAutomato[estado][letra]
        ##Para ver se o estado final esta no conjunto do estado final.
        for ultimoEstado in self.estadoFinal:
          if(ultimoEstado in estado):
            return 'accept'
          else:
            return 'reject'  

  ##Transformar ndfa para dfa
  def transform(self):
    try:
      print('Automato Original:' , self.automato)
      self.novoAutomato[self.estadoInicial] = {}
      ##Preencher o estado inicial que a partir dele iremos para os outros.
      self.novoAutomato = self.__initInicialState__(self.automato, self.alfabeto, self.estadoInicial, self.novoAutomato)
      visitados = []
      print(self.novoAutomato)
      ##Enquanto o tamanho do vetor de resultados for diferente do tamanho do novo automato - 1
      ##Coloquei o -1 por conta que ele pula o estado inicial
      while(len(visitados) != (len(self.novoAutomato) - 1)):
        
        ##Aqui é para pegar o estado que vai virar o estado do automato e
        ##Pegar os respectivos resultados do alfabeto de cada um
        for estado in self.novoAutomato:
          ##Aqui eu verfico se ele é diferente do estado e inicial e 
          ##Se nao foi visitado, no array
          
          if(estado != self.estadoInicial and not(estado in visitados)):
            for letra in self.alfabeto:
              ##Crio um array na posicao do estado e da letra 
              self.novoAutomato[estado][letra] = []
              ##Pego cada estado 1 de cada
              arraySplit = estado.split(',')
              ##Exemplo = 0,1
              ##Aqui é para juntar o conjunto por exemplo 0 quando recebe a vai para q0
              ##Quando recebe 1 vai para q1q2
              ##Agora eles juntam q0q1q2
              for unicoEstado in arraySplit:
                resultado = self.automato[unicoEstado][letra]
                
                if(self.__checkEmptySpace__(resultado)):
                  continue
                else:
                  self.novoAutomato[estado][letra].extend(resultado)   
            
            visitados.append(estado)    
      
        ##Aqui é para criar o estado dele no automato  
        for estado in visitados:
          for letra in self.alfabeto:
            novoEstado = ','.join(self.novoAutomato[estado][letra])
            if(novoEstado in self.novoAutomato):
              continue
            else:
              self.novoAutomato[novoEstado] = {}
        
        print(self.novoAutomato)
      
      #aqui faco a transicao de array para como faco o finitio        
      self.novoAutomato = self.__transformArrayToString__(self.novoAutomato, self.alfabeto)
      print('Automato Final:', self.novoAutomato)
      return self.novoAutomato
    except:
      print('Ocorreu algum erro durante a transformação, verifique se o alfabeto esta correto, o estado inicial, ou se o automato é valido')




