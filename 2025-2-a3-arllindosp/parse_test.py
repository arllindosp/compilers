from lexer import TokenType, Lexer
from parse import Parser, ParseException
import pytest
import sys


def readFile(file): 
    input = None
    with open(file, 'r') as inputFile:
        input = inputFile.read()
    return input

def test_ok_Simples():
    file = "data/ok_Simples.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_ok_BinarySearch():
    file = "data/ok_BinarySearch.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_ok_BinaryTree(): 
    file = "data/ok_BinaryTree.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_ok_BubbleSort(): 
    file = "data/ok_BubbleSort.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_ok_LinearSearch(): 
    file = "data/ok_LinearSearch.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_ok_LinkedList(): 
    file = "data/ok_LinkedList.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result
    
def test_ok_QuickSort(): 
    file = "data/ok_QuickSort.java"
    parser = Parser(Lexer(readFile(file)))
    result = parser.parse()
    assert True == result

def test_Error_Tokens():
    file = "data/error_Tokens.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()

def test_error_BinarySearch():
    file = "data/error_BinarySearch.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()

def test_error_BinaryTree(): 
    file = "data/error_BinaryTree.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()

def test_error_BubbleSort(): 
    file = "data/error_BubbleSort.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()

def test_error_LinearSearch(): 
    file = "data/error_LinearSearch.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()

def test_error_LinkedList(): 
    file = "data/error_LinkedList.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()
    
def test_error_QuickSort(): 
    file = "data/error_QuickSort.java"
    parser = Parser(Lexer(readFile(file)))
    with pytest.raises(ParseException):
        result = parser.parse()