<h4>Estruturas condicionais: </h4>

Agora vamos falar sobre estruturas condicionais, estruturas condicionais nada mais são que expressões booleanas como eu disse no capitulo anterior, essas estruturas verificam se uma condição é verdadeira ou falsa e executa o bloco de código a baixo da condição, vamos começar falando do if.

```
senha = int(input("Digite a senha: "))

if senha == 1312:
    print("Senha correta!")

else:
    print("Senha incorreta!")
```

O input recebe a entrada de dados e o ```if senha == 1312:``` checa se a senha que o usuario digitou é a correta, caso seja correta imprimira na tela "Senha correta"

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/EstruturasCondicionais/img/condicionaisPython.jpg" alt="Estrutura condicional" width="200px" height="200px">

Caso contrário imprimirá "senha incorreta!"

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/EstruturasCondicionais/img/estruturasCondicionaisElse.jpg" alt="Estrutura condicional" width="200px" height="200px">

O elif, mais conhecido como else if, também verifica se a condição é verdadeira, para não termos que adicionar um monte de if's o que deixaria o código mais sujo! Usando o elif podemos verificar se mais condições são verdadeiras. Agora segue um exemplo de código usando o elif:

```
# -*- coding: UTF-8 -*-

i = 47

if i == 2:
    print("i é igual a dois")

elif i == 43:
    print("i é igual a 43")

elif i == 47:
    print("i é igual a 47")

else:
    print("A variavel i não é igual a nenhuma das opções anteriores!")
```

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/EstruturasCondicionais/img/estruturasCondicionaisElif.jpg" alt="Estrutura condicional" width="200px" height="200px">

Exercicio 3: Usando os conhecimentos que você adiquiriu crie um programa que receba duas entradas das notas do aluno, salvando em duas variaveis, a nota1 e nota2 calcule a média aritmética de um aluno, e que caso a nota do aluno seja igual ou maior que 6 imprima na tela que o aluno esta aprovado, caso contrário, o aluno estará reprovado.
