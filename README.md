# Schelling Segregation Disease

## Apresentação do novo modelo, em sua relação ao modelo original

O modelo Schelling Segregation presente na pasta de exemplos do framework MESA consiste em um grupo de agentes de 2 tipos diferentes. Um agente estará feliz quando tiver pelo menos uma quantidade X de vizinhos que possuem o mesmo tipo que ele. Caso o agente não esteja feliz, ele se moverá para um espaço vazio. A simulação acaba quando todos os agentes estiverem felizes.
O modelo aqui apresentado é bastante semelhante ao modelo presente na pasta de exemplos do framework MESA. A diferença é a variável indepednente "Disease probability". Essa variável representa a probabilidade de um agente ser portador de uma doença possivelmente contagiosa, cujo efeito na simulação é que nenhum de seus vizinhos estará feliz enquanto for seu vizinho.

## Descrição da hipótese causal que você deseja comprovar

A inspiração para essa modificação no modelo surgiu em decorrência das várias menções a covid encontradas na pequisa bibliogŕafica. A simulação tem como objetivo observar como a presença de pessoas contaminadas com uma doença contagiosa afeta o bem estar geral de uma comunidade de um ponto de vista social e como isso pode modificar a tendência que indivíduos têm de formarem grupos conforme o modelo de Schelling.

Podemos formular a hipótese da seguinte maneira: A presença de uma doença contagiosa em uma comunidade, de modo que tal doença é capaz de afetar a percepção social que os indivíduos possuem de seus portadores, afetará a tendência presente no modelo para a formação de grupos?

## Justificativa para as mudanças que você fez, em relação ao código original

As modificações de código foram a adição da variável "Disease probability", que diz respeito à probabilidade de um agente ser portador da doença e a lógica para que nenhum agente da simmulação esteja feliz caso um de seus vizinhos seja portador da doença.
A adição da variável se deu pela necessidade do usuário ser capaz de estipular uma quantidade de agentes portadores da doença e a lógica para que nenhum indivíduo fique satisfeito em ter um de seus vizinhos como potador da doença se deu para simular um comportamento de histeria e medo que seria plausível diante de uma doença contagiosa desconhecida, como vimos durante o início da pandemia em 2020. Vale dizer que o modelo presume algumas coisas, como os agentes conseguem saber de forma imediata e correta se um de seus vizinhos está infectado, a doença nunca se espalha e nenhum indivíduo melhora ou morre por causa da doença. Essas funcionalidades podem ser implementadas em versões futuras do modelo.

## Orientação sobre como usar o simulador

O modelo não exige nenhuma atenção especial em comparação com o modelo presente na pasta de exemplos do framework MESA. Pode-se executá-lo normalmente pela linha de comando e pausar, reiniciar e ajustar os valores das variáveis conforme desejar.

## Descrição das variáveis do modelo usadas na simulação

O modelo de Schelling no framework MESA originalmente possui as seguitnes variáveis:
- Agent density: representa a quantidade de agentes na simulação. Varia de 0.1 a 1, porém note que nunca preenche a simulação completamente pois espaços vazios são necessários para que a simulação funcione, assim como nunca deixa a simulação sem agentes, pois agentes são necessários para o funcionamento da simulação.
- Fraction minority: representa o percentual de agentes que vai fazer parte do grupo azul, variando de 0 a 1 (0 a 100%).
- Homophility: representa a quantidade mínima de vizinhos do mesmo tipo de si mesmo que um agente precisa para ser feliz.
- Disease probability: Representa a probabilidade de que um agente seja portador de uma doença possivelmente contagiosa.
