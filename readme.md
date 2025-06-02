# Função minimax

## Primeira Iteração
Assumindo que o jogo começou com player executando na coordenada [1,1]

- Na primeira iteração é feita é avaliado o estado atual do quadro do jogo da velha
![img.png](img.png)
- Verificando se há algum vencedor ou empate, por se tratar de a primeira jogada nenhum if é entrado
- Depois é verificado se o é o jogador maximizer ou minimizer
- na como é chamado na primeira iteração, o minimizer é o jogador X, então caindo no else como a seguir
![img_1.png](img_1.png)
- é atribuído à variável de melhor jogada um número infinito positivo
- Depois é começado a iteração para ser preenchido as jogadas possíveis no estado atual do tabuleiro.
![img_2.png](img_2.png)
- Se caso a linha e coluna do tabuleiro estiver em branco é colocado na posição o oponente neste caso O
- Após isto como a posição [0,0] está preenchida, é iterado o segundo loop (j)
- É testado se está em branco, neste caso sim, então é colocado o oponente nela para simular uma possível jogada
![img_3.png](img_3.png)
- Após isto é atribuído o menor valor da comparação entre best, e a chamada da função minimax, só que agora simulando como se o maximizer fosse jogar
- Entrando na segunda iteração da função

## Segunda iteração
- é avaliado o estado do tabuleiro atualmente
- neste caso como ainda não há vencedores ou empate, os ifs seguintes não irão entrar
![img_4.png](img_4.png)
- Como está iteração da função é simulando o maximizer é entrado no primeiro if
![img_5.png](img_5.png)
- É atribuído o valor infinito negativo à variável best
- E após isto é iniciado um loop para preencher a jogada do maximizer
![img_6.png](img_6.png)
- Caso a posição esteja em branco, neste caso não, é iterado o segundo loop assim como na 1ª iteração
- Nesta iteração a jogada é feita na coordenada [0, 2]
![img_7.png](img_7.png)
- é colocado o X do player na posição, resultando nesta iteração o tabuleiro desta forma:
![img_8.png](img_8.png)
- Após isto é atribuído ao valor da variável best o maior valor entre o valor atual de best e o valor da próxima chamada da função minimax, simulando a jogada do oponente (O)

## Terceira iteração
- é avaliado o estado atual do tabuleiro novamente
- Como não há ainda um vencedor para esta rodada simulada, nenhum if será executado:
![img_9.png](img_9.png)
![img_10.png](img_10.png)
- Como esta iteração se trata de uma rodada simulada para o oponente(O), ele não é o maximizer e sim o minimizer
- Então caindo no else:
![img_11.png](img_11.png)
- é atribuído como melhor jogada o valor de infinito positivo, por se tratar do minimizer e pegar o menor valor
- Então é começado o loop para preenchimento da suposta próxima jogada de O
![img_12.png](img_12.png)
- Caso a posição esteja em branco é entrado no if para executar as instruções
- Como nesta iteração da função está a próxima posição que está vazia é a [1,0]
- Então loop será executado conforme a imagem a seguir do tabuleiro atualmente:
![img_13.png](img_13.png)
- É atribuído o valor do oponente (O) à posição, ficando da forma a seguir o tabuleiro simulado:
![img_14.png](img_14.png)
- Após isto é atribuído à variável best o menor valor da comparação entre valor atual de best e minimax da próxima possível jogada de X
- Indo então para a próxima iteração

## Quarta iteração