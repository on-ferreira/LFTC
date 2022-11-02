class AFD():
  def __init__(self, AL,TR,EI,EF):
    self.AL = AL
    self.TR = TR
    self.EI = EI
    self.EF = EF

  def getEA(self):
    return self.EI

  def validarAlfabeto(self,string):
    return string not in self.AL

  def novoEstado(self,EA,s):
    return self.TR[EA][s]

  def verificarEF(self,estado):
    return estado in self.EF
    
def Validacao(automato,string):
  EA = automato.getEA()
  for s in string:
    if automato.validarAlfabeto(s):  #Verifica se o caracter pertence ao alfabeto da linguagem
      return False
    EA = automato.novoEstado(EA,s)
    if EA == -1:
      return False   #Verifica se o estado atual é válido ou inválido.

  return automato.verificarEF(EA) #Com isso sabemos se o estado Atual no final da string é equivalente ao estado final

'''Criamos alguns exemplos baseados nos automatos que vimos em sala
'''
#Exemplo 1:
AL = set(['a','b'])
TR = {1 : {'a' : 2, 'b' : -1},
      2 : {'a' :-1, 'b' : 3},
      3 : {'a' :-1, 'b' : 1}}
EI = 1
EF = set([3])
automato = AFD(AL,TR,EI,EF)
strings = ['ab','abbab','abc','abab','a','b','aaab','baba']

for s in strings:
  print(f'{s}  {Validacao(automato,s)}') 
