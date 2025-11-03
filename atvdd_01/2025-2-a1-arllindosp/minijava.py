from pathlib import Path
from lexer import *
import sys

def print_to_file(tok:Token, out_file):
    if out_file:
        print(tok._test_print(), file=out_file)



def main():
    out_file = None

    if len(sys.argv) < 2:
        sys.exit("Erro: Precisamos de um arquivo como argumento.\n" +
                "Uso: python minijava.py arquivo_minijava.java\n" +
                "Uso: python minijava.py arquivo_minijava.java arquivo_de_saida")
    elif len(sys.argv) == 3:
        filename = sys.argv[2]
        print(f"OUTPUT FILE: {out_file}. Overwriting.", file=sys.stderr)
        out_file = open(filename, "w")


    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    token = lexer.getToken()
    while token.kind != TokenType.EOF:
        print(token)
        print_to_file(token, out_file)
        token = lexer.getToken()

    print(token)
    print_to_file(token,out_file)

main()