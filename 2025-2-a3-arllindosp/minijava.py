from lexer import *
from parse import *
import sys

def main(): 
    if len(sys.argv) != 2:
        sys.exit("Erro: Precisamos de um arquivo como argumento.")
    with open(sys.argv[1], 'r') as inputFile:
        input = inputFile.read()
    lexer = Lexer(input)
    parser = Parser(lexer)
    try:
        parser.parse()
        print('Terminamos.')
    except ParseException as e:
        print(e)
    
main()