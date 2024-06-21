<h4>Laços de repetição</h4>

Os laços de repetição também conhecidos como loops estão presentes em todas as linguagens de programação, frequentemente em nossas aplicações precisamos repetir determinadas tarefas, e é para isso que os laços de repetição servem. O fluxograma abaixo exemplifica como um laço de repetição funciona, ele entra no loop ele faz um teste para verificar se o laço deve terminar, caso retorne verdadeiro ele termina, caso ele retorne falso ele repete a instrução.

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/La%C3%A7osDeRepeti%C3%A7%C3%A3o/img/fluxograma.jpg">

Agora vamos para um exemplo usando o laço de repetição while:

```
x = 1

while x < 10:
    x = x + 1 # ou x += 1
    print (x)
```

Agora vou explicar como esse código funciona, tem a variavel x que recebe o valor 1, enquanto a variavel x não valer 10 x recebe x + 1, e antes de repetir ele imprime o valor de x na tela. 

Com o laço de repetição for podemos fazer a mesma coisa com menos linhas, como por exemplo:

```
for i in range(10):
    print(i)
```

Exercicio 4: Faça um programa que receba um número e usando laços de repetição calcule e mostre a tabuada desse número.

Exemplo de entrada:

```5```

Exemplo de saída:

```
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
5 x 10 = 50
```
