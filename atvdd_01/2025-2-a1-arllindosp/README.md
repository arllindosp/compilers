[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/xG7wXD0l)
# IF688 - Teoria e Implementação de Linguagens Computacionais

## Atividade 1 - Análise Léxica

Este exercício visa trabalhar os conceitos de análise léxica vistos em sala de aula. A ideia é implementar um analisador léxico para a linguagem MiniJava, que consiste em um subconjunto de Java, cujos elementos léxicos são descritos mais abaixo. 

Para simplificar o processo de desenvolvimento, é fornecido aqui um esqueleto de código disponível em `lexer.py` como ponto de partida para implementar o analisador, bem como alguns testes para verificar a corretude da sua implementação usando a biblioteca `pytest` (se não tiver a biblioteca instalada, rode `pip3 install pytest`).

No arquivo `tokens.py` estão definidos a classe Token e o enum TokenType.

**O seu repositório será avaliado automaticamente pelo Github Classroom, rodando os testes por meio de uma Github Action. Esta ferramenta só avalia commits enviados até a data limite, portanto tenha em mente isso.**

## Elementos Léxicos de MiniJava

- *Whitespace:* espaços em branco, quebra de linha, tabulação e carriage return (`\n` `\t` `\r` `\f`);
- *Comentários:* os dois tipos de comentário são possíveis, comentários de linha, iniciando com `//` e indo até o final da linha, e comentários de múltiplas linhas, que consistem de qualquer texto entre `/*` e `*/`, sem considerar aninhamento;
- *Palavras reservadas:* `boolean`, `class`, `public`, `extends`, `static`, `void`, `main`, `String`, `int`, `while`, `for`, `if`, `else`, `return`, `length`, `true`, `false`, `this`, `new`, `System.out.println`, `break`; 
  - (_Por simplicidade e para facilitar a implementação do compilador, MiniJava trata `System.out.println` como uma palavra reservada, não como uma expressão que representa a chamada do método `println`._)
- *Operadores:* `&&`, `<`, `<=`, `>`, `>=`, `==`, `!=`, `+`, `-`, `*`, `!`; 
  - (_não há operador de divisão, por enquanto_)
- *Delimitadores e pontuação:*  `;` `.` `,` `=` `(` `)` `{` `}` `[` `]`
- *Identificadores:* um identificador começa com uma letra ou _underline_ e é seguido por qualquer quantidade de letras, _underline_ e dígitos. Apenas letras entre A/a e Z/z são permitidos, há diferença entre maiúscula e minúscula. Palavras-chave não são identificadores;
- *Literais Inteiros:* uma sequência de dígitos iniciada com qualquer um dos dígitos entre 1 e 9 e seguida por qualquer número de dígitos entre 0 e 9. O dígito 0 também é um inteiro. 
- Comentários e whitespace não tem significado algum, exceto para separar os tokens.
 
## ATENÇÃO!

Você _não precisa_, *nem deve*, alterar nada do esqueleto de projeto dado além do arquivo `lexer.py` com a sua implementação do analisador.

### Testando o Projeto
- Faça o download deste projeto;
- Caso ainda não tenha `pytest` instalada, rode `pip3 install pytest`
- Na linha de comando, rode `pytest` e veja que os testes não estão passando; 
- Implemente o seu analisador léxico em `lexer.py`, usando apenas a parte dedicada do arquivo para tanto;
- Para testar enquanto implementa, execute `python3 minijava.py data/NOME_ARQUIVO.java` e observe o output.
- Caso deseje ver a saída de minijava.py como arquivo, execute `python3 minijava.py data/NOME_ARQUIVO.java ARQUIVO_SAIDA`

Para cada `data/ARQUIVO.java`, existe um `data/ARQUIVO.tokens` contendo os tokens que devem ser obtidos após o lexing de `data/ARQUIVO.java`. Você pode usar um editor, como o *vscode*, para comparar um arquivo de saída do `minijava.py` com o arquivo esperado, de terminação `.tokens`. Em sistemas unix, eles também podem ser comparados no terminal: `python minijava.py ARQUIVO.java | diff ARQUIVO.tokens -`.