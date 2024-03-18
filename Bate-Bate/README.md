# Projeto CG

## Bate-Bate

O projeto é dividido em três partes distintas:

1. Mecânica de Movimentos
Nesta parte, é implementada a lógica responsável por simular os movimentos do display, alterando sua cor de forma aleatória conforme é "batido".

2. Game
Aqui, são definidas as características do jogo, como a largura e altura da janela, a configuração do modo gráfico e o controle do tempo de execução. Além disso, são estabelecidos os atributos relacionados aos movimentos do display.

3. Main
O Main é a parte do código responsável por iniciar o objeto do jogo e dar início à sua execução.

Cada uma dessas partes possui seus próprios conjuntos de atributos e métodos, contribuindo para o funcionamento geral do projeto "Bate-Bate".


<h2>Diagarama UML: </h2>
<div align=center>

<img height="250em" src="./Diagrama UML/diagrama.png">

<h3>Classe MecMovimento:</h3>

<h5>1.Atributos: </h5>

<p>
Fonte: Estabelece o tamanho da fonte utilizada para o texto, definindo a legibilidade e o estilo visual das informações apresentadas na tela.

Texto: Define o conteúdo textual que será exibido na tela durante o jogo, permitindo a personalização e a comunicação de mensagens importantes aos jogadores.

Largura: Determina a largura da janela de visualização do jogo, controlando o espaço disponível para a exibição dos elementos gráficos e textuais.

Altura: Define a altura da janela de visualização do jogo, configurando a dimensão vertical disponível para a apresentação dos elementos visuais e textuais.   
</p>
<h5>2.Métodos: </h5>
<p>
Gerar numero não zero = Sorteio entre os número -1 e 1

Move =  o texto na direção X e Y

Cor texto = Sortear a cor do texto

RUN: Inicia a execução do jogo e processa os comandos necessários para o seu funcionamento, garantindo que todas as operações e interações ocorram conforme o esperado durante a jogabilidade.
</p>

<h3>Classe Game: </h3>
<h5>1. Atributos</h5>
<p>
Largura: Define a dimensão horizontal da janela de exibição do jogo, determinando o espaço visual disponível para os elementos gráficos.

Altura: Estabelece a dimensão vertical da janela de exibição do jogo, definindo a altura visual da área de jogo.

Tela: Configura o modo de exibição gráfica da janela do jogo, especificando como os elementos visuais serão renderizados e apresentados aos jogadores.

Clock: Controla o tempo de execução do jogo, sincronizando eventos e atualizações dentro do ambiente de jogo.

Movendo Texto: Define os atributos da classe MecMovimento que serão renderizados na tela, permitindo a representação dinâmica de texto durante a jogabilidade.

</p>
<h5>2.Métodos:</h5>
<p>
RUN: Executa o jogo e seta comandos

</p>
<h3>Classe Main: </h3>
<p>
Inicia o objeto GAME
</p>