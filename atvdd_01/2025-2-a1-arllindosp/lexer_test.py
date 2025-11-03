from lexer import *
import sys
import pytest


def readFile(file): 
    input = None
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    return input

def readTokens(input):
    lexer = Lexer(input)
    token = lexer.getToken()
    tokens = []
    tokens.append(token)
    while token.kind != TokenType.EOF:
        token = lexer.getToken()
        tokens.append(token)
    return tokens

def readExpectedTokens(filename):
    with open(filename, 'r') as tokenFile:
        #remover \n do final das tokenStrs 
        return [s.strip() for s in tokenFile.readlines()]
        
def verify_files(sourceFile, expectedTokensFile):
    tokens = readTokens(readFile(sourceFile))
    #gabarito 
    expectedTokens = readExpectedTokens(expectedTokensFile)

    for tokenIdx,(parsedToken,expectedTokenStr) in enumerate(zip(tokens, expectedTokens)):
        assert parsedToken._test_print() == expectedTokenStr,  (
            f"{tokenIdx+1}:{expectedTokenStr} != {parsedToken}"
        )

    assert len(tokens) == len(expectedTokens)

def test_Simples():
    verify_files("data/Simples.java", "data/Simples.tokens")

def test_Tokens():
    verify_files("data/Tokens.java", "data/Tokens.tokens")

def test_BinarySearch():
    verify_files("data/BinarySearch.java", "data/BinarySearch.tokens")

def test_BinaryTree():
    verify_files("data/BinaryTree.java", "data/BinaryTree.tokens")

def test_BubbleSort():
    verify_files("data/BubbleSort.java", "data/BubbleSort.tokens")

def test_LinearSearch():
    verify_files("data/LinearSearch.java", "data/LinearSearch.tokens")

def test_LinkedList():
    verify_files("data/LinkedList.java", "data/LinkedList.tokens")

def test_QuickSort():
    verify_files("data/QuickSort.java", "data/QuickSort.tokens")
