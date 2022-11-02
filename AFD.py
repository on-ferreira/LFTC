def Validacao(automato,string):
  EA = automato[2]
  for s in string:
    if s not in automato[0]: #Verifica se o caracter pertence ao alfabeto da linguagem
      return False
    EA = automato[1][EA][s]
    if EA == -1:
      return False   #Verifica se o estado atual é válido ou inválido.

  return (EA in automato[3]) #Com isso sabemos se o estado Atual no final da string é equivalente ao estado final

'''Criamos alguns exemplos baseados nos automatos que vimos em sala
'''
#Exemplo 1:
AL = set(['a','b'])
TR = {1 : {'a' : 2, 'b' : -1},
      2 : {'a' :-1, 'b' : 3},
      3 : {'a' :-1, 'b' : 1}}
EI = 1
EF = set([3])
automato = (AL,TR,EI,EF)
strings = ['ab','abbab','abc','abab','a','b','aaab','baba']

for s in strings:
  print(f'{s}  {Validacao(automato,s)}') 
