# Automatos

### Inicio implementação automatos

* Para iniciar o codigo basta abrir o <strong> main.py </strong> e executá-lo
* Ele irá perguntar qual tipo de arquivo quer ler, DFA.TXT ou NFA.TXT, e só basta testar as palavras. 

-----------------------
### Arquivo de leitura DFA.txt 

#### Alfabeto do automato
* alfabeto = 0, 1
#### Seu estado inicial
* estadoInicial = s0
#### Seu estado final
* estadoFinal = s0
#### Suas respectivas transições por exemplo de s0 quando ele recebe 0 ele vai para s0 e quando recebe 1 vai para s1. 
* s0: 0:s0,1:s1
* s1: 0:s2,1:s0 
* s2: 0:s1,1:s2 

------------------------
### Arquivo de leitura NFA.txt

#### Alfabeto do automato
* alfabeto = 0, 1
#### Seu estado inicial
* estadoInicial = s0
#### Seu estado final
* estadoFinal = s0
#### Suas respectivas transições por exemplo de q0 quando ele recebe 0 ele vai para q0 e q1 e quando recebe 1 vai para q0.
##### OBS: nenhumEstado significa que quando receber uma letra do alfabeto não irá para nenhum lugar.
* q0: a:q0,q1/b:q0
* q1: a:nenhumEstado/b:q2 
* q2: a:nenhumEstado/b:nenhumEstado  
