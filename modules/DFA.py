from modules.ler import *

class AutomatoFinitoDeterministico:
    def __init__(self):
      self.estadoFinal = lerEstadoFinal('dfa.txt')
      self.estadoInicial = lerEstadoInicial('dfa.txt')
      self.alfabeto = lerAlfabeto('dfa.txt')
      self.automato = lerAutomatoDFA('dfa.txt')
    def checkIsAcceptedDFA(self,palavra):
      #Iniciando o estado inicial
      estado = self.estadoInicial
      #Para cada letra do palavra
      for letra in palavra:
        if(not(letra in self.automato[estado])):
          print('algum caracter da palavra nao existe no alfabeto dessa maquina!')
          break
        else:
          estado = self.automato[estado][letra]
      if(estado in self.estadoFinal):
          return 'accept'
      else:
          return 'reject'

    
      
    
      
      
    

    
    
