Desenvolvido por:
João Pedro Ferreira do Nascimento Lucas 		nºUSP: 11802291
João Pedro Santos Lourenço 				          nºUSP: 13782522
Julia Souto Leoni 						              nºUSP: 13386270
Marcus Vinicius Novaes Flori				        nºUSP: 13836921
Pedro Ruiz Pereira Lopes 					          nºUSP: 13725611
Raul de Assis Santos 						            nºUSP: 13748892


Disciplina:
Computação Científica em Python (LOM 3260)

Docente:
Luiz Tadeu Fernandes Eleno

Universidade de São Paulo - Escola de Engenharia de Lorena

########################################################################

Este projeto foi desenvolvido para a disciplina de Computação
Científica em Python - ministrada pelo Prof. Dr. Luiz Tadeu
Fernandes Eleno.

Os arquivos em questão buscam simular o sistema solar e o cometa
Halley, a Terra, alguns de seus satélites artificiais e a Lua e,
finalmente, Júpiter e algumas de suas luas.
A proporção exata do tamanho dos planetas não foi respeitada já
que alguns corpos ficariam invisíveis (por exemplo, no sistema
solar, os planetas próximos ao Sol ficariam praticamente invisíveis).
Buscou-se também aplicar texturas aos planetas a partir de imagens.

Para isso, foram usadas as bibliotecas: numpy, VPython, ephem e
datetime.

#######################################################################

O código utiliza uma função que converte as coordenadas espaciais
para coordenadas cartezianas utilizando uma função.
A partir de uma lista os planetas e satélites são ordenados.
Foi criada uma função para aplicar as texturas nos planetas.
A partir disso, a animação foi criada. A taxa de atualização é,
relativamente, alta no caso do sistema solar pois não ele não seria
capaz de contemplar a mudança na órbita de alguns planetas e estrelas.

Ao executar o código, é aberta uma janela 500x500 no navegador (que
pode ser reajustada conforme o interesse do usuário). É possível
aplicar zoom a partir do scroll do mouse. Também é possível mudar a
orientação da visão ao segurar o botão direito do mouse enquanto o
move - assim, o usuário pode perceber a inclinação do cometa Halley,
por exemplo, em relação ao plano dos planetas no sistema solar.

São salvas as órbitas dos últimos 10 anos a fim de não sobrecarregar
o código em questão.

######################################################################
