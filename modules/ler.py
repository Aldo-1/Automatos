def tirarEspacoVazio(lista):
  for i in range(0,len(lista)):
    lista[i] = lista[i].strip()
    
  return lista

def lerAlfabeto(txt):
  f = open(txt, 'r')
  for line in f:
    if('alfabeto' in line):
      index = line.index('=')
      alfabeto = line[index+1:].split(',')
      alfabeto = tirarEspacoVazio(alfabeto)
      break
  f.close()
  return alfabeto

def lerEstadoInicial(txt):
  f = open(txt, 'r')
  for line in f:
    if('estadoInicial' in line):
      index = line.index('=')
      estadoInicial = line[index+1:].strip()
  f.close()
  return estadoInicial

def lerEstadoFinal(txt):
  f = open(txt, 'r')
  for line in f:
    if('estadoFinal' in line):
      index = line.index('=')
      estadoFinal = set(line[index+1:].strip().split(','))
  f.close()
  
  return estadoFinal

def lerAutomatoDFA(txt):
  automato = {}
  dicionarioLetra = {}
  f = open(txt, 'r')
  for line in f:
    alfabeto = lerAlfabeto(txt)
    if(line.find('=') == -1 and line != '\n'):
      indexDoisPontos = line.index(':')
      estado = line[:indexDoisPontos].strip()
      transicoes = line[indexDoisPontos+1:].split(',')
      transicoes = tirarEspacoVazio(transicoes)
      for transicao in transicoes:
        indexDoisPontosTransicao = transicao.index(':')
        paraOndeVai = transicao[indexDoisPontosTransicao + 1:].strip()
       
        letra = transicao[:indexDoisPontos - 1].strip()
        if(letra in alfabeto):
          
          automato[estado] = {}
          dicionarioLetra[letra] = paraOndeVai
        else:
          print('ocorreu algum erro na execucao')
          break
      automato[estado] = dicionarioLetra
      dicionarioLetra = {}
  f.close()
  return automato

def lerAutomatoNFA(txt):
  automato = {}
  dicionarioLetra = {}
  f = open(txt, 'r')
  for line in f:
    alfabeto = lerAlfabeto(txt)
    if(line.find('=') == -1 and line != '\n'):
      indexDoisPontos = line.index(':')
      estado = line[:indexDoisPontos].strip()
      transicoes = line[indexDoisPontos+1:].split('/')
      transicoes = tirarEspacoVazio(transicoes)
      for transicao in transicoes:
        indexDoisPontosTransicao = transicao.index(':')
        paraOndeVai = transicao[indexDoisPontosTransicao + 1:].strip()
        if(paraOndeVai == 'nenhumEstado'):
          paraOndeVai = ''
        
        letra = transicao[:indexDoisPontos - 1].strip()
        
        paraOndeVai = tirarEspacoVazio(paraOndeVai.split(','))
        
        if(letra in alfabeto):
          automato[estado] = {}
          dicionarioLetra[letra] = paraOndeVai
        else:
          print('ocorreu algum erro na execucao')
          break
      automato[estado] = dicionarioLetra
      dicionarioLetra = {}
  f.close()
  return automato

