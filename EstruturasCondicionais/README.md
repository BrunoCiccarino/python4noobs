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

Caso contrário imprimirá "senha incorreta!"
