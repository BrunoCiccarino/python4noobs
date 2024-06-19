<h4>Tipos primitivos</h4>

No python, diferente de muitas linguagens, não precisamos declarar os tipos primitivos nas variaveis, o proprio python detecta automaticamente isso, como por exemplo:

Em python

``` a = "Uma string qualquer"```

Ja em outras linguagens, fazemos assim: 

Em Java 

```
public class StringExample {
    public static void main(String[] args) {
        // Inicialização direta
        String saudacao = "Olá, Mundo!";
    }
}
```

Em C

```
#include <stdio.h>

int main() {
    char saudacao[] = "Olá, Mundo!";
}
```

Em python temos esses tipos primitivos: ```int, string, float e boolean```

O tipo int representa os números inteiros, números positivos e negativos sem casas decimais.

Para declarar em python variaveis do tipo inteiro é a mesma forma de declarar variaveis do tipo string, só que não precisa das aspas, por exemplo:

```i = 10``` ou ```i = "-10"```

Ja o tipo Float é um tipo primitivo de ponto flutuante e é usado para representar números com decimais menores. Pode ser qualquer numero basta ter esse ponto '.'

para declarar variaveis em python do tipo float é a mesma coisa que do tipo inteiro

```f = 10.5```

Tipo booleano -> True or False. Expressões booleanas necessariamente retornam true ou false. 

Para declarar uma variavel do tipo boolean, é a mesma coisa de todos os outros exemplos

```b = True``` Observe que o python é case sensitive, ou seja, ele é sensivel a letras maiusculas e minusculas, então ```Print``` é diferente de ```print``` no primeiro caso retornaria um erro pois no python, não existe ```print``` com a letra maiuscula.

E pode ser utilizado dentro de laços de repetição

```
 i = 748
 if i == 890:
     print("O número escolhido é igual o numero especificado")
 else:
     print("O numero especificado é diferente")
```

Para verificar o tipo da variavel que esta sendo usado usamos a classe type, como nesse exemplo:

```
i = 12345
print(type(i))
```
