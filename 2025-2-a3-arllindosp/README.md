[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/LdV-wAay)
# IF688 - Teoria e Implementação de Linguagens Computacionais

## Atividade 3 - _Recursive-Descent Parsing em MiniJava_

Este exercício visa trabalhar os conceitos de análise sintática _top-down_ vistos em sala de aula. A ideia é implementar um analisador sintático manualmente para parte da linguagem MiniJava, que consiste em um subconjunto de Java, cuja gramática é descrita mais abaixo. 

Para simplificar o processo de desenvolvimento, é fornecido aqui um esqueleto de código disponível em `parse.py` como ponto de partida para implementar o analisador, bem como alguns testes para verificar a corretude da sua implementação usando a biblioteca `pytest` (se não tiver a biblioteca instalada, rode `pip3 install pytest`). 

**O seu repositório será avaliado automaticamente pelo Github Classroom, rodando os testes por meio de uma Github Action. Esta ferramenta só avalia commits enviados até a data limite, portanto tenha em mente isso.**

O único arquivo que deve ser enviado **também** no Google Classroom é a sua versão de `parse.py`, e o nome do arquivo deve ser o seu login. Então, no meu caso seria `lmt.py`.

## Gramática Simplificada de MiniJava

**Esta gramática não contempla toda a sintaxe de MiniJava, os métodos declarados dentro das classes não tem corpo, por exemplo**

O que está dentro de aspas é ou um token de palavra reservada, ou um separador, delimitador. Por exemplo, `"class"` representa o `TokenType.CLASS`, e `"{"` representa o `TokenType.L_BRACK` (vide `lexer.py`). Além disso, no caso da gramática abaixo, `<IDENTIFIER>` representa o `TokenType.IDENT`. 

```
Program ::= MainClass Classes
MainClass ::= "class" <IDENTIFIER> "{" "public static void main(String[] a) { System.out.println(); } }"
Classes ::= ClassDecl Classes | ϵ
ClassDecl ::= "class" <IDENTIFIER> ClassA
ClassA ::= "extends" <IDENTIFIER> "{" ClassB | "{" ClassB
ClassB ::=  "}"
          | "static" VarDecl ClassB
          | VarDecl ClassB
          | "public" MethodDecl ClassC
ClassC ::=  "}"
          | "public" MethodDecl ClassC
VarDecl ::= Type <IDENTIFIER> ";"
MethodDecl ::= Type <IDENTIFIER> "(" MethodA
MethodA ::= ")" "{" "}"
          | Type <IDENTIFIER> MethodB
MethodB ::= ")" "{" "}"
          | "," Type <IDENTIFIER> MethodB
Type ::= SimpleType ArrayPart
SimpleType ::= "boolean"
          | "float"
          | "int"
          | <IDENTIFIER>
ArrayPart ::= ϵ
          | "[" "]" ArrayPart
```

## ATENÇÃO!

Você _não precisa_, *nem deve*, alterar nada do esqueleto de projeto dado além do arquivo `parse.py` com a sua implementação do analisador. Arquivos modificados

### Testando o Projeto
- Faça o download deste projeto;
- Caso ainda não tenha `pytest` instalada, rode `pip3 install pytest`
- Na linha de comando, rode `pytest` e veja que os testes não estão passando; 
- Implemente o seu analisador léxico em `parse.py`, usando apenas a parte dedicada do arquivo para tanto;
- Para testar enquanto implementa, execute `python3 minijava.py data/NOME_ARQUIVO.java` e observe o output.