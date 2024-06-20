<h4>Operadores e uma introdução as estruturas de Condição</h4>

No python existem 6 tipos de operadores, os Operadores Aritméticos, os Operadores Lógicos, os Operadores de Associação, os Operadores de Comparação, os Operadores de Identidade e os Operadores de Atribuição. Como não tem como falar de Operadores de comparação sem falar de estruturas de condição vou dar só uma introdução a as estruturas de condição, mas vou abordar mais profundamente eles em outra sessão que vou deixar somente para falar de estruturas de condição. Vamos começar pelos operadores mais fáceis, os Operadores Aritméticos. No python temos 7 operadores aritméticos ```+``` *Adição*	Realiza a soma de ambos operandos. ```-``` *Subtração*	Realiza a subtração de ambos operandos. ```*``` *Multiplicação*	Realiza a multiplicação de ambos operandos. ```/``` *Divisão*	Realiza a Divisão de ambos operandos. ```//``` *Divisão inteira*	Realiza a divisão entre operandos e a parte decimal de ambos operandos. ```%``` *Módulo*	Retorna o resto da divisão de ambos operandos. ```**``` 	*Exponenciação*	Retorna o resultado da elevação da potência pelo outro.

Agora eu vou fazer um exemplo de calculo com todos esses operadores que eu citei.

Soma

```
a = 4
b = 2
soma = a + b
print(soma)
```

Subtração

```
a = 8
b = 3
subtracao = a - b
print(subtracao)
```

Multiplicação

```
a = 5
b = 3
multiplicacao = a * b
print(multiplicacao)
```

divisão

```
a = 9
b = 3
divisao = a / b
print(divisao)
```

Divisão inteira

```
a = 5
b = 2
divisao_inteira = a // b
print(divisao_inteira)
```

Exponenciação

```
a = 4
b = 2
exponenciacao = a ** b
print(exponenciacao)
```

Operadores de comparação, são usados para comparar dois valores, e esses são os operadores de comparação: ```==```	Igual a	Verifica se um valor é igual ao outro. ```!=```	Diferente de	Verifica se um valor é diferente ao outro. ```>```	Maior que	Verifica se um valor é maior que outro. ```>=```	Maior ou igual	Verifica se um valor é maior ou igual ao outro. ```<```	Menor que	Verifica se um valor é menor que outro. ```<=```	Menor ou igual	Verifica se um valor é menor ou igual ao outro.

Agora um exemplo utilizando esses operadores:

```
# -*- coding: UTF-8 -*-
a = int(input("Insira um valor para fazermos a comparação"))

if a == 5:
    print('O valor inserido é igual a 5')

elif a != 7:
    print('O valor inserido não é igual a 7')

elif a > 2:
    print('O valor inserido é maior de 2')

elif a >= 5:
    print('O valor inserido é maior ou igual a 5')

elif a < 7:
    print('O valor inserido é menor que 7')

elif a <= 5:
    print('O valor inserido inserido é menor ou igual a 5')

else:
    print("Insira um valor valido")

```

Lembram que no capitulo sobre tipos primitivos eu falei que o tipo booleano era utilizado em laços de repetição? Então, esse é o exemplo perfeito para explicar isso, vamos la. 

```
if a == 5:
    print('O valor inserido é igual a 5')
```

Explicação do código: Se a for igual a 5 ele executa o trecho de código a baixo ou seja, imprime(O valor inserido é igual a 5), nesse caso seria se a for igual a 5 ele retorna True. Caso o valor de a não fosse igual a 5 ele retornaria False, então executaria a operação de baixo que é o: 

```
elif a != 7:
    print('O valor inserido não é igual a 7')
```

Caso o valor de a não fosse igual a 7 ele retornaria True, e nesse caso ele imprimiria na tela (O valor inserido não é igual a 7) e finalizaria a execução por ali. Vamos executar esse código no vscode e vamos ver o output (a saída) dele:

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Operadores/img/operadorespython.jpg" alt="Exercicios dos operadores do python" width="200" height="200">

E se nós tirassemos esse trecho do código? Vamos executar para ver o que acontece...

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Operadores/img/operadorespython2.jpg" alt="Exercicios dos operadores do python 2" width="200" height="200">

E se nós não inseríssimos um valor válido? Vamos executar e para ver o que acontece

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Operadores/img/valueError.jpg" alt="Value Error" width="200" height="200">

Retornaria esse value error, o value error é uma exceção comum em Python que ocorre quando uma função recebe um argumento com o tipo correto, mas com um valor inválido. ja que usamos int(input()) e passamos um argumento do tipo string quando o interpretador estava esperando um número inteiro como argumento. 

Operadores de atribuição, usados para atribuições de valores à variaveis, podendo controlar como a atribuição será realizada. 

Operador                Equivalente a

```
=	                        x = 1
+=	                     x = x + 1
-=	                     x = x - 1
*=	                     x = x * 1
/=	                     x = x / 1
%=	                     x = x % 1
```
