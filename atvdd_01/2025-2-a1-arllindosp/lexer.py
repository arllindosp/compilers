import enum
import sys
from tokens import Token,TokenType

class Lexer:
    def __init__(self, input):
        self.source = input + '\n' #código-fonte (entrada)
        self.curChar = '' #caractere atual dentro do código-fonte
        self.curPos = -1
        self.nextChar()
        pass

    # Processa o proximo caractere
    def nextChar(self):
        self.curPos = self.curPos + 1
        if self.curPos >= len(self.source):
            self.curChar = '\0' #EOF
        else:
            self.curChar = self.source[self.curPos]

    # Retorna o caractere seguinte (ainda não lido).
    def peek(self):
        if self.curPos+1 >= len(self.source):
            return '\0'
        else: 
            return self.source[self.curPos+1]

    # Token inválido encontrado, método usado para imprimir mensagem de erro e encerrar.
    def abort(self, message):
        sys.exit("Erro léxico! " + message)
		
    # Pular espaço em branco
    def skipWhitespace(self):
        while self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\n' or self.curChar == '\r':
            self.nextChar()
		
    # Pular comentários.
    def skipComment(self):
        if self.curChar == '/' :
            if self.peek() == '/':

                while self.curChar != '\n' and self.curChar != '\0':
                    self.nextChar()

            elif self.peek() == '*':
                # Comentário de bloco /* */
                self.nextChar()  # Pula '/'
                self.nextChar()  # Pula '*'
                stop = False
                while not stop:
                    if self.curChar == '*' and self.peek() == '/':
                        self.nextChar()  # Pula '*'
                        self.nextChar()  # Pula '/'
                        stop = True
                    elif self.curChar == '\0':
                        self.abort("Comentário não fechado")
                    else:
                        self.nextChar()


    # Return o próximo token --> Implementar esta função e as funções de skip acima 
    # Atualmente esta função retorna um token de tipo TEST para cada caractere do programa até alcançar EOF
    # Os tipos de token estão definidos em tokens.py
    def getToken(self):
        self.skipWhitespace()
        # Verificar comentários
        if self.curChar == '/':
            if self.peek() == '/' or self.peek() == '*':
                self.skipComment()
                return self.getToken()  
            else:
                self.abort("Operador de divisão não suportado em MiniJava")
        token = None
        
        if self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        
        elif self.curChar.isalpha() or self.curChar == '_':
            startPos = self.curPos
            
            if (self.curPos + 18 <= len(self.source) and 
                self.source[self.curPos:self.curPos+18] == "System.out.println"):
                # Avançar manualmente para o final de "System.out.println"
                for _ in range(18):
                    self.nextChar()
                token = Token("System.out.println", TokenType.SYSTEM_OUT_PRINTLN)
            else:
            
                #Enquanto for uma letra ou dígito [a-z A-Z 0-9] ou um underscore '_'
                while self.curChar.isalnum() or self.curChar == '_' :
                    self.nextChar()
                
                lexema = self.source[startPos:self.curPos]
                if lexema == 'class':
                    token = Token(lexema, TokenType.CLASS)
                elif lexema == "public":
                    token = Token(lexema, TokenType.PUBLIC)
                elif lexema == "static":
                    token = Token(lexema, TokenType.STATIC)
                elif lexema == "void":
                    token = Token(lexema, TokenType.VOID)
                elif lexema == "main":
                    token = Token(lexema, TokenType.MAIN)
                elif lexema == "String":
                    token = Token(lexema, TokenType.STRING)
                elif lexema == "int":
                    token = Token(lexema, TokenType.INT)
                elif lexema == "new":
                    token = Token(lexema, TokenType.NEW)
                elif lexema== "this":
                    token = Token(lexema, TokenType.THIS)
                elif lexema == "if":
                    token = Token(lexema, TokenType.IF)
                elif lexema == "else":
                    token = Token(lexema, TokenType.ELSE)
                elif lexema == "while":
                    token = Token(lexema, TokenType.WHILE)
                elif lexema == "boolean":
                    token = Token(lexema, TokenType.BOOLEAN)
                elif lexema == "extends":
                    token = Token(lexema, TokenType.EXTENDS)
                elif lexema == "return":
                    token = Token(lexema, TokenType.RETURN)
                elif lexema == "length":
                    token = Token(lexema, TokenType.LENGTH)
                elif lexema == "true":
                    token = Token(lexema, TokenType.TRUE)
                elif lexema == "false":
                    token = Token(lexema, TokenType.FALSE)
                elif lexema == "for":
                    token = Token(lexema, TokenType.FOR)
                elif lexema == "break":
                    token = Token(lexema, TokenType.BREAK)
                else:
                    # Se não é palavra reservada, é um identificador
                    token = Token(lexema, TokenType.IDENT)
        
        #Verificação de strings
        elif self.curChar == '"':
            self.nextChar()
            startPos = self.curPos

            while self.curChar != '"' and self.curChar != '\0':
                self.nextChar()
            
            if self.curChar == '\0':
                self.abort("String não fechada")
            
            stringTexto = self.source[startPos:self.curPos]
            token = Token(stringTexto, TokenType.LITERAL)
            self.nextChar()
            
            
                

        # Verificar se é um número
        elif self.curChar.isdigit():
            startPos = self.curPos
            
            # Ler todos os dígitos
            while self.curChar.isdigit():
                self.nextChar()
            
            # Extrair o número completo
            numeroTexto = self.source[startPos:self.curPos]
            token = Token(numeroTexto, TokenType.NUMBER)
        
        
        #Verifica operador de soma
        elif self.curChar == '+':
            plus = self.curChar
            token = Token(plus, TokenType.PLUS)
            self.nextChar()
        
        #verifica operador de subtração
        elif self.curChar == '-':
            minus = self.curChar
            token = Token(minus, TokenType.MINUS)
            self.nextChar()

        #Verifica operador de multiplicação 
        elif self.curChar == '*':
            mult = self.curChar
            token = Token(mult,TokenType.MULT)
            self.nextChar()
        
        #Verifca operador dos operadores de negação e de desigualdade
        elif self.curChar == '!':
            if self.peek() == '=':
                token = Token('!=', TokenType.NOTEQ)
                self.nextChar()
                self.nextChar()
            else:
                no = self.curChar
                token =Token(no,TokenType.NOT)
                self.nextChar()

        #Verifca operador de menor e menor e igual 
        elif self.curChar == '<':
            if self.peek() == '=':
                token = Token('<=', TokenType.LTEQ)
                self.nextChar()
                self.nextChar()
            else:
                lt = self.curChar
                token = Token(lt,TokenType.LT)
                self.nextChar()
        
        #Verifca operador de maior e maior e igual 
        elif self.curChar == '>':
            if self.peek() == '=':
                token = Token('>=', TokenType.GTEQ)
                self.nextChar()
                self.nextChar()
            else:
                gt = self.curChar
                token = Token(gt,TokenType.GT)
                self.nextChar()
            
        #Verfica operador AND
        elif self.curChar == '&':
            if self.peek() == '&':  # Verifica se o próximo também é &
                token = Token('&&', TokenType.AND)
                self.nextChar()  # Pula o primeiro &
                self.nextChar()  # Pula o segundo &
            else:
                # & sozinho é um erro em MiniJava
                self.abort("Caractere inválido: &")
        
        #verificao do operador de igualdade
        elif self.curChar == '=':
            if self.peek() == '=':
                token = Token('==', TokenType.EQEQ)
                self.nextChar()
                self.nextChar()
            else:
                eq = self.curChar
                token = Token(eq,TokenType.EQ)
                self.nextChar()
        
        #Verificacao de ponto e vírgula, ponto e de vírgula
        elif self.curChar == '.':
            lexema = self.curChar
            token = Token(lexema,TokenType.DOT)
            self.nextChar()
        elif self.curChar == ';':
            lexema = self.curChar
            token = Token(lexema, TokenType.SEMICOLON)
            self.nextChar()
        elif self.curChar == ',':
            lexema = self.curChar
            token = Token(lexema, TokenType.COMMA)
            self.nextChar()
        
         # Verificar delimitadores simples
        elif self.curChar == '{':
            token = Token(self.curChar, TokenType.L_BRACK)
            self.nextChar()
        elif self.curChar == '}':
            token = Token(self.curChar, TokenType.R_BRACK)
            self.nextChar()
        elif self.curChar == '(':
            token = Token(self.curChar, TokenType.L_PAREN)
            self.nextChar()
        elif self.curChar == ')':
            token = Token(self.curChar, TokenType.R_PAREN)
            self.nextChar()
        elif self.curChar == '[':
            token = Token(self.curChar, TokenType.L_SQBRACK)
            self.nextChar()
        elif self.curChar == ']':
            token = Token(self.curChar, TokenType.R_SQBRACK)
            self.nextChar()
        else: 
            self.abort("Caractere inválido: " + self.curChar)
        
        return token
