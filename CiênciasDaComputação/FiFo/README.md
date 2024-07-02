## FiFo

Fifo ou first in first out é um algoritmo de fila simples. Como diz o nome no FiFo, pense no fifo como uma fila, o primeiro elemento a entrar na fila é obrigatóriamente o primeiro a sair. O "queue" (fila, em inglês) é um conceito bem simples e útil na programação, especialmente quando você precisa organizar coisas na ordem em que elas chegam e garantir que o primeiro item a entrar seja o primeiro a sair. É como estar numa fila de mercado: o primeiro que chega é o primeiro a ser atendido, né?
Como nessa imagem que ilustra completamente o que estou querendo dizer:

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/FiFo/img/firstinfirstout.png" alt="First In First Out"> 

E no python temos uma coisa que chamamos de deque, mas o que é o deque?

O deque (pronuncia-se "deck") é uma estrutura de dados bem bacana e super útil em Python, que vem da biblioteca collections. Basicamente, o deque é uma abreviação de "double-ended queue" (fila de duas pontas). O que isso significa? Simples: ele permite adicionar e remover elementos tanto do início quanto do final da fila, de forma rápida e eficiente. Diferente das listas normais, onde adicionar ou remover elementos no início pode ser meio lento, o deque foi feito justamente para essas operações serem rapidinhas em ambas as extremidades. Então, se você precisa de algo mais flexível que uma lista comum, e que funcione como uma fila ou uma pilha, o deque é a escolha perfeita.

E como podemos representar isso em python? 

``` Python
import collections

def queue():
    d = collections.deque([9,8,7,6,5,4]) # Inicializo a fila com uma lista de 9 a 4
    return d 

d = queue()
print("Deque",d) # Printo o valor da lista da fila

def insertQueue(): # Adiciono o valor 1 2 3 na lista da fila
    d.append(1) 
    d.append(2)
    d.append(3)

def removeQueue(): # Removo o primeiro item na lista da fila
    d.popleft()

insert = insertQueue()
print("Adding 3, 2, 1",d)

remove = removeQueue()
print("Removing 9 from deque", d)
```

Neste exemplo, temos a função queue que cria e retorna uma deque inicializada com os elementos de 9 a 4. Em seguida, temos a função insertQueue que adiciona os elementos 1, 2 e 3 ao final da fila. Por fim, a função removeQueue remove o primeiro elemento da fila.

Quando rodamos esse código, a saída será:

```
Deque deque([9, 8, 7, 6, 5, 4])
Adding 3, 2, 1 deque([9, 8, 7, 6, 5, 4, 1, 2, 3])
Removing 9 from deque deque([8, 7, 6, 5, 4, 1, 2, 3])
```

Como podemos ver, o elemento 9, que foi o primeiro a entrar na fila, é também o primeiro a ser removido, seguindo a lógica FIFO. Essa estrutura de dados é muito útil em diversos cenários onde a ordem dos elementos deve ser preservada.
