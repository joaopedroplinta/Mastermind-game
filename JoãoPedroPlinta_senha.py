import tkinter as tk # Importa o módulo tkinter que será utilizado para criar uma janela.
import random # Importa o módulo random que será utilizado para gerar valores aleatórios.

root = tk.Tk() # Criamos uma instância do objeto Tk() do módulo tkinter e armazenamos em uma variável chamada "root". Essa instância representa a janela principal do jogo.

import time # Importamos o módulo time, que será utilizado para realizar pausas na execução do programa.

frame = tk.Frame(root)  # Criamos uma instância do objeto Frame() do tkinter, que será utilizada para agrupar outros elementos da janela, como o canvas.
canvas = tk.Canvas(frame, width=400,height=600, highlightthickness=0,highlightbackground="black", relief=tk.FLAT,bg='#aaaaff',bd=0) # Criamos uma instância do objeto Canvas() do tkinter, que será utilizado para desenhar os elementos do jogo, como os círculos coloridos e as linhas que representam as tentativas. Essa instância é adicionada ao frame criado anteriormente. O canvas possui algumas configurações, como a largura e altura, a cor de fundo, a espessura da borda e a cor da borda.

coresbase = ['red','orange','yellow','green','blue','purple','cyan','white']   # Criamos uma lista com as cores possíveis para serem selecionadas no jogo.

# Definimos algumas variáveis que serão utilizadas no jogo. "posição" e "velocidade" serão utilizadas para controlar a posição dos círculos coloridos na tela. "numTentativas" e "tamanhoCodigo" são o número de tentativas e o tamanho do código que o jogador terá que acertar. "tamanhoCor" e "paddingCor" são o tamanho e o espaço entre os círculos coloridos na tela.
posição = 0
velocidade = 2

numTentativas = 12
tamanhoCodigo = 4
tamanhoCor = 40
paddingCor = 50

# Definimos duas variáveis, "linha" e "cpos", que serão utilizadas para controlar a posição dos elementos na tela.
linha = 0
cpos = 0

selecionarCores = [] # Criamos uma lista vazia que será utilizada para armazenar as cores selecionadas pelo jogador.

escolhaCores = [[-1 for i in range (tamanhoCodigo)] for j in range (numTentativas)] # Criamos uma matriz que representa as tentativas do jogador. Cada linha representa uma tentativa e cada coluna representa uma posição no código. Cada elemento da matriz é inicializado com -1, que significa que ainda não foi escolhida uma cor para aquela posição.

def açãoUsuario(): # Define uma função chamada açãoUsuario
    canvas.unbind('<space>') # Desvincula a tecla espaço do canvas
    canvas.bind('<Left>', lambda _: selecionar_posicao(-1)) # Vincula a tecla esquerda do teclado à função selecionar_posicao com o argumento -1
    canvas.bind('<Right>', lambda _: selecionar_posicao(1)) # Vincula a tecla direita do teclado à função selecionar_posicao com o argumento 1
    canvas.bind('<Up>', lambda _: mudar_cor(1)) # Vincula a tecla para cima do teclado à função mudar_cor com o argumento 1
    canvas.bind('<Down>', lambda _: mudar_cor(-1)) # Vincula a tecla para baixo do teclado à função mudar_cor com o argumento -1
    canvas.bind('<Return>', lambda _: mudar_linha()) # Vincula a tecla Enter do teclado à função mudar_linha

def açãoUsuarioInativa(): # Define uma função chamada açãoUsuarioInativa
    canvas.unbind("<Left>") # Desvincula a tecla esquerda do teclado do canvas
    canvas.unbind("<Right>") # Desvincula a tecla direita do teclado do canvas
    canvas.unbind("<Up>") # Desvincula a tecla para cima do teclado do canvas
    canvas.unbind("<Down>") # Desvincula a tecla para baixo do teclado do canvas
    canvas.unbind("<Return>") # Desvincula a tecla Enter do teclado do canvas

def criarCodigo(): # Define uma função chamada criarCodigo
    seleção = [x for x in range(len(coresbase))] # Cria uma lista com números inteiros de 0 a len(coresbase)-1
    codigo = []
    for i in range(tamanhoCodigo):
        codigoIndex = random.randint(0,len(seleção)-1) # Seleciona um índice aleatório na lista seleção
        codigo.append(seleção[codigoIndex]) # Adiciona o elemento da selecao no índice selecionado à lista codigo
        seleção.pop(codigoIndex) # Remove o elemento da selecao no índice selecionado
    return codigo

corCoded = criarCodigo() # Chama a função criarCodigo e atribui o resultado à variável corCoded

def iniciarLinha(): # Define uma função chamada iniciarLinha.
    global selecionarCores, tops, bots # Define três variáveis globais selecionarCores, tops e bots, que podem ser acessadas em qualquer lugar do programa.
    selecionarCores = [x for x in range(len(coresbase))] # Cria uma lista selecionarCores contendo números de 0 a len(coresbase) - 1. Ela usa uma sintaxe de compreensão de lista para fazer isso.
    tops = 0 # Define a variável tops como 0.
    bots = 0 # Define a variável bots como 0.

def iniciarJogo(): # Define uma função chamada "iniciarJogo".
    global linha, cpos, escolhaCores, corCoded # Indica que as variáveis "linha", "cpos", "escolhaCores" e "corCoded" serão usadas globalmente dentro da função.
    canvas.itemconfig(board[linha][cpos],width=0) # Atualiza a aparência de um item do "canvas" (uma tela para desenho). O item é um círculo na posição [linha][cpos] em "board" e a largura é definida como 0.
    for i in range(numTentativas): # Inicia um loop "for" que será executado "numTentativas" vezes.
        for j in range(tamanhoCodigo): # Inicia outro loop "for" que será executado "tamanhoCodigo" vezes.
            canvas.itemconfig(board[i][j], fill='#8888dd') # Atualiza a cor de um item do "canvas". O item é um círculo na posição [i][j] em "board" e é preenchido com a cor "#8888dd".
            if i < numTentativas - 1: # Atualiza a cor de outro item do "canvas", apenas se o valor de "i" for menor que "numTentativas - 1". O item é um círculo na posição [i][j] em "response" e é preenchido com a cor "#8888dd".
                canvas.itemconfig(response[i][j], fill='#8888dd')
    escolhaCores = [[-1 for i in range(tamanhoCodigo)] for j in range(numTentativas)] # Cria uma matriz "escolhaCores" com "numTentativas" linhas e "tamanhoCodigo" colunas, preenchida com o valor -1.
    # Define as variáveis "linha" e "cpos" como 0 e atualiza a largura do item em "board" na posição [linha][cpos] como 1.
    linha = 0
    cpos = 0
    canvas.itemconfig(board[linha][cpos],width=1)
    açãoUsuario() # Chama uma função "açãoUsuario()" que não está definida neste código.
    corCoded = criarCodigo() # Define a variável "corCoded" como o resultado da função "criarCodigo()".
    iniciarLinha() # Chama uma função "iniciarLinha()" que não está definida neste código.

# Estas linhas criam uma matriz chamada "board" que contém as tentativas do usuário e uma matriz chamada "response" que contém as respostas para cada tentativa. A matriz "board" é criada preenchendo uma lista vazia "novaLinha" com uma série de objetos ovais criados pelo método "canvas.create_oval()" do módulo "canvas" (não mostrado no código). A posição e o tamanho desses objetos ovais são determinados pelos valores das variáveis "x", "y", "tamanhoCor" e "paddingCor". A matriz "response" é criada de forma semelhante, mas é preenchida apenas se a tentativa atual não for a última.
board = []
response = []
for i in range(numTentativas):
    novaLinha = []
    novaResposta = []
    for j in range(tamanhoCodigo):
        x = paddingCor*j+5
        y = 600 - paddingCor*i - tamanhoCor - 5
        novaLinha.append(canvas.create_oval(x,y,x+tamanhoCor,y+tamanhoCor,fill='#8888dd',outline='black',width=0))
        if i < numTentativas-1:
            x = paddingCor /2*j+255
            y += tamanhoCor /8
            novaResposta.append(canvas.create_oval(x+ tamanhoCor/4, y+ tamanhoCor/4, x + tamanhoCor/2, y + tamanhoCor/2, fill='#8888dd', outline='black', width=0))
    board.append(novaLinha)
    if i < numTentativas - 1:
        response.append(novaResposta)
iniciarJogo() # Chama uma função chamada "iniciarJogo()". Não há informações suficientes para entender o que essa função faz.
canvas.itemconfig(board[linha][cpos],width=1) # Altera a largura do objeto oval localizado na linha "linha" e coluna "cpos" da matriz "board" criada anteriormente. A largura é alterada para 1, o que provavelmente torna o objeto oval mais visível. O objeto oval é modificado pelo método "canvas.itemconfig()" do módulo "canvas" (não mostrado no código).

def selecionar(cor_posição): # Define uma função chamada selecionar que recebe um parâmetro cor_posição.
    canvas.itemconfig(cor_posição, width=5) # Altera a largura da configuração do item no canvas para 5

def desmarcar(cor_posição): # Define uma função chamada desmarcar que recebe um parâmetro cor_posição.
    canvas.itemconfig(cor_posição, width=0) # Altera a largura da configuração do item no canvas para 0

def definir_cor(cor_posição, cor): # Define uma função chamada definir_cor que recebe um cor_posição, cor.
    canvas.itemconfig(cor_posição, fill=cor) # Altera a cor de preenchimento da configuração do item no canvas para cor

def selecionar_posicao(incremento): # Define uma função chamada selecionar_posição que recebe um parâmetro incremento.
    global cpos # Define a variável cpos como uma variável global
    canvas.itemconfig(board[linha][cpos],width=0) # Altera a largura da configuração do item no canvas para 0
    cpos += incremento # Adiciona o valor de incremento à variável cpos
    if cpos < 0: cpos = tamanhoCodigo-1 # Se cpos for menor que 0, atribui o valor de tamanhoCodigo-1 a cpos
    if cpos >= tamanhoCodigo: cpos = 0 # Se cpos for maior ou igual a tamanhoCodigo, atribui 0 a cpos
    canvas.itemconfig(board[linha][cpos],width=1) # Altera a largura da configuração do item no canvas para 1 na nova posição de cpos no board[linha]

def mudar_cor(incremento): # Define uma função chamada mudar_cor que recebe um parâmetro incremento.
    escolhaCores[linha][cpos] += incremento # Adiciona o valor de incremento ao elemento da lista escolhaCores que está na linha linha e na coluna cpos.
    if escolhaCores[linha][cpos] > len(coresbase)-1: escolhaCores[linha][cpos] = 0 # Se o valor resultante da operação anterior for maior que o tamanho da lista coresbase menos 1, define o elemento da lista escolhaCores que está na linha linha e na coluna cpos como 0.
    if escolhaCores[linha][cpos] < 0: escolhaCores[linha][cpos] = len(coresbase)-1 # Se o valor resultante da operação da primeira linha for menor que 0, define o elemento da lista escolhaCores que está na linha linha e na coluna cpos como o tamanho de coresbase menos 1.
    canvas.itemconfig(board[linha][cpos], fill=coresbase[escolhaCores[linha][cpos]]) # Atualiza a cor de um objeto na tela (canvas) que está na posição [linha][cpos] do tabuleiro (board), com a cor da lista coresbase que está na posição escolhaCores[linha][cpos].

def mudar_linha(): # Define uma função chamada mudar_linha
    global linha, tops, bots, escolhaCores # Declaração de que as variáveis linha, tops, bots e escolhaCores são globais e podem ser usadas dentro da função.
    for i in range(tamanhoCodigo): # Loop que itera sobre todos os índices de 0 a tamanhoCodigo - 1 (tamanhoCodigo é uma variável global).
        if escolhaCores[linha][i] == -1: # Verifica se a cor na posição [linha][i] da matriz escolhaCores é igual a -1. Se for, imprime uma mensagem de erro e retorna False. Caso contrário, continua a execução da função.
            print("Cores não definidas {},{}:".format(linha,i))
            return False
        for j in range(tamanhoCodigo): # Loop que itera sobre todos os índices de 0 a tamanhoCodigo - 1 novamente e conta quantas cores na posição i são iguais a corCoded[i]. Armazena o número de cores que estão na mesma posição que a cor verificada na variável tops e as que estão em outras posições na variável bots.
            if (j==i and corCoded[j]==escolhaCores[linha][i]): tops += 1
            if (j!=i and corCoded[j]==escolhaCores[linha][i]): bots += 1
    if tops < tamanhoCodigo and linha < numTentativas-2: # Verifica se o número de cores na posição correta é menor que tamanhoCodigo e se a linha atual (linha) é menor que numTentativas-2. Se essa condição for verdadeira, mostra o número de tops e bots na tela, muda as cores das respostas correspondentes (preto para tops e branco para bots), limpa a cor da célula atual do tabuleiro, avança para a próxima linha, destaca a célula atual do novo tabuleiro, executa a função iniciarLinha() e retorna False.
        print("tops:{}, bots:{}".format(tops,bots))
        for i in range(tops):
            canvas.itemconfig(response[linha][i], fill="black")
        for i in range(bots):
            canvas.itemconfig(response[linha][i+tops], fill="white")
        canvas.itemconfig(board[linha][cpos],width=0)
        linha += 1
        canvas.itemconfig(board[linha][cpos],width=1)
        iniciarLinha()
        return False
    else:
        print("Linha{} tops{} e bots{}".format(linha,tops,bots)) # Se não houve uma combinação exata, imprime a linha com os tops e bots
        output = True # Define a variável output como True
        if linha == numTentativas-2:  # Se for a penúltima linha, define output como False
            output = False
        for i in range(tops):
            canvas.itemconfig(response[linha][i], fill="black") # Para cada valor de tops, muda a cor do círculo para preto
        for i in range(bots):
            canvas.itemconfig(response[linha][i+tops], fill="white") # Para cada valor de bots, muda a cor do círculo para branco
        for i in range(tamanhoCodigo):
            canvas.itemconfig(board[numTentativas-1][i], fill=coresbase[corCoded[i]]) # Muda a cor do círculo correspondente na última linha para a cor do código
        açãoUsuario() # Aguarda a ação do usuário
        canvas.bind("<space>", lambda _: iniciarJogo()) # Liga a tecla espaço com a função iniciarJogo
        return output   # Retorna a variável output para a função principal 

frame.pack()    # Coloca o frame na janela principal usando o gerenciador de layout padrão
canvas.pack()   # Coloca o canvas dentro do frame usando o gerenciador de layout padrão

root.title("Mastermind") # Define o título da janela principal como "Mastermind"

canvas.focus_set() # Define o foco para o canvas, permitindo que ele receba eventos de teclado
açãoUsuario() # Chama a função açãoUsuario() para atualizar a interface do usuário
canvas.bind("<space>", lambda _: iniciarJogo()) # Liga a tecla espaço para a função iniciarJogo() quando pressionada

root.mainloop() # Inicia o loop principal do tkinter, mantendo a janela aberta até que seja fechada.