## Grafos

Como esse assunto é bem extenso, vou fazer em mais de uma parte, pra ficar mais facil de entender. Nessa primeira parte vai ficar toda a teoria e na parte 2 grafos em python vai ser toda a pratica.

<a href="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/GrafosEmPython.md">Grafos em python</a>

Vamos começar com o que são grafos! Grafos são exatamente estruturas matemáticas que permitem codificar relacionamentos entre pares de objetos (Resumindo, são conjunto de vértices conectados por arestas). E para um grafo ficar bem definido temos que ter dois conjuntos: O conjunto V dos vértices e o conjunto A das arestas. Para ficar mais fácil de entender, vamos ilustrar com alguns exemplos. Obs: Todas as referências de onde peguei essas imagens e me baseei para escrever esse tutórial estão nessa sessão aqui: <a href="https://github.com/BrunoCiccarino/python4noobs/blob/main/REFERENCIAS.md">Referencias</a> inclusive recomendo muito que vocês vão atrás das minhas referencias para se basear em mais de um conteúdo, não levem tudo o que estou escrevendo como uma verdade absoluta (até porquê sou um estudante também, não tenho autoridade em nada. Só estou passando o que eu aprendi para frente. Achei importante dizer isso logo no começo da sessão para relembrar vocês sobre isso, inclusive sem querer fugir muito do assunto, o fabio akita fez um video chamado "Não terceirize suas decisões" vou deixar o link na sessão de referencias que eu coloquei um pouco acima.

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/grafos.png" alt="Grafos">

Aqui na imagem, podemos ver claramente o conjunto A das arestas e o conjunto V que na imagem é representado com números. E onde que usamos isso? Nós usamos grafos para quase tudo nessa vida, literalmente tudo na natureza da para representar com grafos, na técnologia então, nem se fala... Um bom exemplo é o algoritmo de recomendação do twitter deixei essa imagem abaixo que foi tirada do video do fabio akita sobre o algoritmo do twitter que foi liberado aqui no github, depois vão la dar uma olhada se quiserem se aprofundar no assunto, aqui vou explicar superficialmente pois esse repositório é para facilitar o entendimento de quem quer aprender a programar em python, então o público alvo é desde quem esta começando na programação agora até o público mais experiente.

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/GrafosTwitter.jpg" alt="Twitter Grafos">

Nesse grafo do twitter os vertices são as pessoas e as arestas são os relacionamentos (Quem seguimos, damos like, reetwitamos até mesmo quem bloqueamos). Provavelmente vocês devem estar pensando que isso é coisa de outro mundo, vou deixar outro exemplo para vocês... As rotas dos transportes públicos, cada estação é um vertice, e as arestas estão onde são as linhas. 

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/GrafosTransporteP%C3%BAblico.jpg" alt="Grafos transporte público">

O Dna Humano, pode ser representado por um grafo suas bases hidrogenadas são seus vertices (adenina (A), guanina (G), citosina (C) e timina (T).)

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/grafodna.jpg" alt="Dna Grafos">

Até mesmo as sinapses cerebrais do ser humano pode ser representado por um grafo. As sinapses cerebrais são junções entre a terminação de um neurônio e a membrana de outro neurônio. São elas que fazem a conexão entre células vizinhas, dando continuidade à propagação do impulso nervoso por toda a rede neuronal.

<img src="https://github.com/BrunoCiccarino/python4noobs/blob/main/Ci%C3%AAnciasDaComputa%C3%A7%C3%A3o/Grafos/img/cerebrografo.jpg" alt="Cerebro Grafo">
