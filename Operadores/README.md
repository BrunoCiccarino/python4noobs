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

<h4>Operadores de comparação:</h4>

são usados para comparar dois valores, e esses são os operadores de comparação: ```==```	Igual a	Verifica se um valor é igual ao outro. ```!=```	Diferente de	Verifica se um valor é diferente ao outro. ```>```	Maior que	Verifica se um valor é maior que outro. ```>=```	Maior ou igual	Verifica se um valor é maior ou igual ao outro. ```<```	Menor que	Verifica se um valor é menor que outro. ```<=```	Menor ou igual	Verifica se um valor é menor ou igual ao outro.

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

<h4>Operadores de atribuição: </h4> 

usados para atribuições de valores à variaveis, podendo controlar como a atribuição será realizada. 

Operador,                        Equivalente a:

```
=	                        x = 1
+=	                     x = x + 1
-=	                     x = x - 1
*=	                     x = x * 1
/=	                     x = x / 1
%=	                     x = x % 1
```

Agora vou fazer exemplos de como usar esses operadores em um código:

Operador +=:

```
num = 5

num += 7
print(num)
```

Operador -=:

```
num = 8

num -= 3
print(num)  
```

Operador *=:

```
num = 3

num *= 2
print(num)
```

Operador /=:

```
num = 7

num /= 4
print(num)
```

Operador %=:

```
num = 13

num %= 2
print(num)
```

O operador % é chamado de modulo, que é o resto da divisão, no exemplo acima é 13 / 2, o resto da divisão da 1 e o quociente é 6.5.

<h4>Operadores lógicos: </h4>

O operador ```and``` retorna True se ambas as condições forem verdadeiras. O operador ```or``` retorna True se uma das condições for verdadeira. O operador not	retorna Falso se o resultado for verdadeiro.

```
num1 = int(input("Insira um valor:"))
num2 = int(input("Insira outro valor:"))

# Exemplo and
if num1 > 3 and num2 < 8:
    print("As Duas condições são verdadeiras")

# Exemplo or
elif num1 > 4 or num2 <= 8:
    print("Uma ou duas das condições são verdadeiras")

# Exemplo not
elif not (num1 < 30 and num2 < 8):
    print("Inverte o resultado da condição entre os parânteses")

else:
    print("Insira um valor valido")
```

<h4>Operadores de identidade:</h4> 

Os operadores de identidade vocês não vão precisar saber agora, mas vale a pena eu explicar. Os operadores de identidade são muito utilizados para comparar objetos (Tudo em python são objetos, mas vamos ver isso mais para frente), verificando se os objetos testados referenciam o mesmo objeto ```(is)``` ou não ```(is not)```. 

```
l = [1, 2, 3, 4, 5, 6, 7]
ol = [1, 2, "tres", 4]

print(f"São o mesmo objeto? {l is ol}") # Retorna false
```

```
t = (1, 2, 3)
ot = (3, 2, 1)

print(f"Os objetos são diferentes? {ot is t}")
```

Uma dica, operador == checa os valores testados e o operador is testa a referência dos valores testados!

<h4>Operadores de Associação: </h4>

Os operadores de associação verificam se determinados objetos pertencem uma determinada estrutura de dados.

```
l_stacks = ['web development', 'low level development', 'desktop development', 'mobile development']

print('desktop development' in l_stacks)
print('Front End'not in l_stacks)
```

Exercicio 2: A fórmula para calcular a área de uma circunferência é: area = π . raio2. Considerando para este problema que π = 3.14159: - Efetue o cálculo da área, elevando o valor de raio ao quadrado e multiplicando por π. A entrada contém um valor de ponto flutuante (dupla precisão), no caso, a variável raio. A saída deve apresentar a mensagem "A=" seguido pelo valor da variável area, conforme exemplo abaixo, com 4 casas após o ponto decimal. Caso queira comparar os códigos a resolução desse exercicio estará na pasta Exercicios no diretório principal.
