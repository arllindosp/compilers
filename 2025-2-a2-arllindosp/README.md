[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/YGAzT_Iv)
# IF688 - Teoria e Implementação de Linguagens Computacionais

## Atividade 2 - LL(1) parsing

Este exercício visa trabalhar os conceitos de análise sintática *top-down* vistos em sala de aula. A ideia é implementar um gerador de parsers LL(1) para gramáticas livres de contexto, usando as funções `FIRST` e `FOLLOW`.

Para simplificar o processo de desenvolvimento, é fornecido aqui um esqueleto de código disponível em `ll1parser.py` como ponto de partida para implementar o analisador, bem como alguns testes para verificar a corretude da sua implementação usando a biblioteca `pytest` (se não tiver a biblioteca instalada, rode `pip3 install pytest`). 

**O seu repositório será avaliado automaticamente pelo Github Classroom, rodando os testes por meio de uma Github Action. Esta ferramenta só avalia commits enviados até a data limite, portanto tenha em mente isso.**

## Representação da Grámatica no Código

Para implementar as funções, é fundamental entender como a gramática é definida no projeto:
* **Símbolos**: Terminais e não-terminais são objetos das classes `Terminal` e `Nonterminal`. Por exemplo: `S = Nonterminal('S')` e `a = Terminal('a')`. O símbolo para a cadeia vazia (épsilon) é a constante `EPSILON`.
  
* **Regras de Produção**: Cada regra é um objeto da classe `Rule`, que recebe o não-terminal do lado esquerdo e uma lista de símbolos do lado direito. Exemplo: `Rule(S, [a, S, b])` representa a regra `S → a S b`.
  
* **Gramática**: O objeto principal é da classe `Grammar`. Ele é inicializado com um conjunto de objetos `Rule` e o `Nonterminal` inicial. Exemplo: `g = Grammar({r1, r2, r3}, S)`.

## Instruções

A sua resolução precisa implementar as funções a seguir. O código já existente em cada uma destas funções **não precisa, nem deve** ser modificado.

- `buildFirstSets`
  - A versão inicial da função já inicializa os conjuntos `FIRST` de cada um dos terminais da gramática e dos símbolos especiais (ε e $) como sendo o próprio símbolo, além de definir um conjunto vazio para cada um dos não-terminais. 
  - Como resultado da execução da função, os conjuntos `FIRST` de cada um dos não-terminais devem ser corretamente populados com os seus respectivos símbolos terminais ou ε.
- `buildFollowSets`
  - A versão inicial da função já inicializa os conjuntos `FOLLOW` de cada um dos não-terminais da gramática com o conjunto vazio, com exceção do símbolo inicial, que já recebe $ (EOF) como parte do conjunto. 
  - Como resultado da execução da função, os conjuntos `FOLLOW` de cada um dos não-terminais devem ser corretamente populados com os seus respectivos símbolos terminais ou $.
- `generateParsingTable`
  - A versão inicial da função já fornece uma estrutura para a tabela de parsing, onde cada índice de `parsingTable` é um símbolo (objeto) não-terminal, que aponta para um dicionário onde as chaves são as strings dos terminais + EOF ($).
  - Como resultado da execução da função, a tabela de parsing deve ser populada com o lado direito da produção associada com a combinação Não-terminal + Terminal.
- `checkIfLL1`
  - A versão inicial da função sempre retorna `True`, o que nem sempre está correto.
  - Sua implementação deve usar a tabela de parsing (parsingTable) para verificar se a gramática é LL(1).

## ATENÇÃO!

Você _não precisa_, *nem deve*, alterar nada do esqueleto de projeto dado além do arquivo `ll1parser.py` com a sua implementação.

### Testando o Projeto
- Faça o download deste projeto;
- Caso ainda não tenha `pytest` instalada, rode `pip3 install pytest`
- Na linha de comando, rode `pytest` e veja que a maioria dos testes não estão passando; 
- Implemente as funções descritas acima em `ll1parser.py`, usando apenas a parte dedicada do arquivo para tanto;
- Use o arquivo `main.py` se quiser rodar algo no console e observar o *output*.