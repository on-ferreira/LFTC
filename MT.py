
R = 1
L = -1

class MT():
  def __init__(self, Alfabeto,Transicoes,estadoInicial,estadoFinal):
    self.AL = Alfabeto
    self.TR = Transicoes
    self.EI = estadoInicial
    self.EF = estadoFinal

  def getEI(self):
    return self.EI

  def novoEstado(self,EA,s):
    return self.TR[EA][s][0],self.TR[EA][s][1], self.TR[EA][s][2]

  def getFinal(self):
    return self.EF

  def imprimirAtual(self,EA,i,string):
    for k in range(len(string)):
      if k == i:
        print('q'+str(EA),end='')
      print(string[k],end='')
    print()
    
def Validacao(automato,string):
  EA = automato.getEI()
  string = string + "◊" #Como Python não trabalha reconhecendo o "\n" no final da cadeia, esse caractere vai indicar o nosso final de cadeia
  i = 0
  try:
    while EA != automato.getFinal():
      automato.imprimirAtual(EA,i,string)
      EA,novoChar,Direcao = automato.novoEstado(EA,string[i])
      string = string[:i]+novoChar+string[(i+1):]
      i += Direcao
    automato.imprimirAtual(EA,i,string)
    return True
  except KeyError:    
    return False




#Exemplo de funcionamento para a linguagem L = {a^n b^n / n>0}:
Alfabeto = set(['a','b']) #Ficou sem uso devido ao formato  da validação
Transicoes = { 
  #Transições vão ser  no padrão (q1,a)=(q2,A,R)
  1 : {'a' : [2,'X',R], 'Y' : [4,'Y',R]},
  2 : {'a' : [2,'a',R], 'b' : [3,'Y',L], 'Y' : [2,'Y',R]},
  3 : {'a' : [3,'a',L], 'X' : [1,'X',R], 'Y' : [3,'Y',L]},
  4 : {'Y' : [4,'Y',R], '◊' : [5,'F',R]}}
estadoInicial = 1
estadoFinal = 5  
TURING = MT(Alfabeto,Transicoes,estadoInicial,estadoFinal)




strings = ['aabb','ab','abc','abab','aaabbb','b','aaab','baba']

for s in strings:
  print("Analisando a string "+s)
  print(f'{s}  {Validacao(TURING,s)}') 
  print()
