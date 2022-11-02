Repositório criado para armazenar os trabalhos de implementação da disciplina Linguagens Formais e Teoria da Computação, sendo eles:

Trabalho 1 - Verificar, via AFD, se uma cadeia é aceita. (Automato Finito Deterministico)

Os automatos devem estar no formato AL,TR,EI,EF onde cada sigla significa, além disso, temos também um índice que será usado na 4-upla na função de validação.
0 - AL = Alfabeto
1 - TR = Transições *** Quando um estado não tem 'caminho' com um dos simbolos do alfabeto ele será representado como -1
2 - EI = Estado Inicial
3 - EF = Estado Final
EA = Estado Atual



Trabalho 2 - Verificar se uma cadeia é aceita por uma MT. (Maquina de Turing)

As maquinas de Turing devem criadas dentro do padrão (Alfabeto, Estados/Transições, EstadoInicial, EstadoFinal)

Como em python, passar um índice que não existe a um dicionário vai dar uma Exception, resolvemos usar isso a nosso favor. Vai cair na expection por 2 motivos: Caractere inválido ao alfabeto e/ou caractere sem transição no estado atual, resultando em "Máquina Parou".

Legenda:
AL = Alfabeto
TR = Transições 
EI = Estado Inicial
EF = Estado Final 
EA = Estado Atual
