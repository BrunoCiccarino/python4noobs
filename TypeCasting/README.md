<h4>Type Casting</h4>

Type Casting é a conversão de objetos ou tipos primitivos de um tipo para outro tipo. E python é uma das poucas linguagens que permite essa conversão. 

Para explicar o que é o type casting tenho que explicar algumas coisas antes, la no primeiro exemplo, la no hello world eu fiz uma operação de soma ```print(1 + 1)```, mas o que aconteceria se eu tentasse realizar a mesma operação com a e b que não declarei como variaveis, então o interpretador vai interpretar como strings. ```print('x' + 'z')``` o interpretador vai retornar "xz", mas porquê isso, vocês conseguem me explicar? Não? Porquê ele concatenou as strings, por conta que no python temos o polimorfismo, ou seja, podemos usar o mesmo operador para realizar operações diferentes. isso só acontece porquê python é dinamicamente tipada, você pode passar dois tipos para o interpretador que ele vai conseguir se virar. 

Um exemplo onde podemos usar o casting: Imagine que você esta escrevendo um programa e nele você precisa concatenar uma string com um número inteiro, você conseguiria fazer isso sem o casting? A resposta é não pois são de tipos primitivos diferentes, iria retornar uma mensagem de erro assim: 

``` Python
print('i' + 2)
     ~~~~^~~
TypeError: can only concatenate str (not "int") to str
```

Agora vamos para os exemplos de casting's:

De float para inteiro (Integer)

``` Python
valor_float = 3.5
valor_inteiro = int(valor_float)
print(valor_inteiro)  # Saída: 3

```

De inteiro para float

``` Python
valor_inteiro = 3
valor_float = float(valor_inteiro)
print(valor_float)  # Saída: 3.0
```

De inteiro para string(int -> str)

``` Python
valor_inteiro = 42
valor_string = str(valor_inteiro)
print(valor_string)  # Saída: '42'
```

De inteiro para boolean

``` Python
valor_inteiro = 0
valor_booleano = bool(valor_inteiro)
print(valor_booleano)  # Saída: False
```

Exercicio 1: faça um código que tenha 3 variaveis, uma com seu nome, outra com seu sobrenome, outra com sua idade e que imprima todos os valores das variaveis.
