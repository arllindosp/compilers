import enum
import sys

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
		
    # Pular espaço em branco, exceto novas linhas, que são usadas como separadores.
    def skipWhitespace(self):
        while self.curChar == '\n' or self.curChar == ' ' or self.curChar == '\t' or self.curChar == '\r':
            self.nextChar()
		
    # Pular comentários.
    def skipComment(self):
        if self.curChar=='/' and self.peek()=='/':
            while self.curChar != '\n':
                self.nextChar()
            self.nextChar()
        if self.curChar=='/' and self.peek()=='*':
            while not (self.curChar=='*' and self.peek()=='/'):
                self.nextChar()
            self.nextChar()

    def shouldIgnore(self, c):
        return c == '\n' or c == ' ' or c == '\t' or c == '\r' or c == '/'

    def ignore(self): 
        while self.shouldIgnore(self.curChar):
            self.skipWhitespace()
            self.skipComment()

    # Return o próximo token.
    def getToken(self):
        self.ignore()
        token = None
        if self.curChar == '+':
            token = Token(self.curChar, TokenType.PLUS)
        elif self.curChar == '-':
            token = Token(self.curChar, TokenType.MINUS)
        elif self.curChar == '*':
            token = Token(self.curChar, TokenType.MULT)
        elif self.curChar == '.':
            token = Token(self.curChar, TokenType.DOT)
        elif self.curChar == ',':
            token = Token(self.curChar, TokenType.COMMA)
        elif self.curChar == ';':
            token = Token(self.curChar, TokenType.SEMICOLON)
        elif self.curChar == '(':
            token = Token(self.curChar, TokenType.L_PAREN)
        elif self.curChar == ')':
            token = Token(self.curChar, TokenType.R_PAREN)
        elif self.curChar == '{':
            token = Token(self.curChar, TokenType.L_BRACK)
        elif self.curChar == '}':
            token = Token(self.curChar, TokenType.R_BRACK)
        elif self.curChar == '[':
            token = Token(self.curChar, TokenType.L_SQBRACK)
        elif self.curChar == ']':
            token = Token(self.curChar, TokenType.R_SQBRACK)
        elif self.curChar == '\0':
            token = Token(self.curChar, TokenType.EOF)
        elif self.curChar == '<':
            if self.peek() == '=':
                c = self.curChar
                self.nextChar()
                token = Token(c + self.curChar, TokenType.LTEQ)
            else: 
                token = Token(self.curChar, TokenType.LT)    
        elif self.curChar == '>':
            if self.peek() == '=':
                c = self.curChar
                self.nextChar()
                token = Token(c + self.curChar, TokenType.GTEQ)
            else: 
                token = Token(self.curChar, TokenType.GT)
        #se for = EQ, se for == EQEQ
        elif self.curChar == '=':
            if self.peek() == '=':
                c = self.curChar
                self.nextChar()
                token = Token(c + self.curChar, TokenType.EQEQ)
            else: 
                token = Token(self.curChar, TokenType.EQ)
        elif self.curChar == '!':
            if self.peek() == '=':
                c = self.curChar
                self.nextChar()
                token = Token(c + self.curChar, TokenType.NOTEQ)
            else: 
                token = Token(self.curChar, TokenType.NOT)
        elif self.curChar == '&':
            if self.peek() == '&':
                c = self.curChar
                self.nextChar()
                token = Token(c + self.curChar, TokenType.AND)
            else: 
                self.abort("Esperava o símbolo de & e recebeu "+self.peek())
        elif self.curChar.isdigit():
            startPos = self.curPos
            while self.peek().isdigit():
                self.nextChar()
            if self.peek() == '.': #decimais
                self.nextChar()
                if not self.peek().isdigit():
                    self.abort("Caractere ilegal dentro de um número: "+ self.peek())
                while self.peek().isdigit():
                    self.nextChar()
            number = self.source[startPos : self.curPos + 1]
            token = Token(number, TokenType.NUMBER)
        elif self.curChar.isalpha() or self.curChar == '_':
            startPos = self.curPos
            while self.peek().isalnum() or self.peek() == '_':
                self.nextChar()
            word = self.source[startPos : self.curPos + 1]
            if word == "System":#System.out.println
                self.nextChar()
                rest_system = self.source[self.curPos : self.curPos + 12]
                if rest_system == ".out.println":
                    token = Token("System.out.println", TokenType.SYSTEM_OUT_PRINTLN)
                    self.curPos = self.curPos + 11
                else:
                   self.abort("Esperava um System.out.println") 
            else: 
                keyword = Token.checkIfKeyword(word)
                if keyword == None:
                    token = Token(word, TokenType.IDENT)
                else: 
                    token = Token(word, keyword)
        else: 
            #Token desconhecido
            self.abort("Token desconhecido: "+self.curChar)
        
        self.nextChar()
        return token

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText #lexema, a instância específica encontrada
        self.kind = tokenKind # o tipo de token (TokenType) classificado
    
    def __str__(self):
        return self.kind + " (" + self.text + ")"

    @staticmethod
    def checkIfKeyword(word):
        for kind in TokenType:
            if kind.name == word.upper() and kind.value > 100 and kind.value < 200:
                return kind
        return None

class TokenType(enum.Enum):
    EOF = -1
    NUMBER = 1 #NUMERO
    IDENT = 2 #IDENTIFICADOR
    LITERAL = 3 #STRING "alasdlasdal"
    #PALAVRAS RESERVADAS
    BOOLEAN = 101
    CLASS = 102
    PUBLIC = 103
    EXTENDS = 104
    STATIC = 105
    VOID = 106
    MAIN = 107
    STRING = 108
    INT = 109
    WHILE = 110
    IF = 111
    ELSE = 112
    RETURN = 113
    LENGTH = 114
    TRUE = 115
    FALSE = 116
    THIS = 117
    NEW = 118
    SYSTEM_OUT_PRINTLN = 119
    FOR = 120
    BREAK = 121
    #OPERADORES
    AND = 201   # &&
    LT = 202    # <
    EQEQ = 203  # ==
    NOTEQ = 204 # !=
    PLUS = 205  # +
    MINUS = 206 # -
    MULT = 207  # *
    NOT = 208   # !
    GT = 209    # >
    GTEQ = 210  # >=
    LTEQ = 211  # <=
    #DELIMITADORES
    SEMICOLON = 251   # ;
    DOT = 252    # .
    COMMA = 253  # ,
    EQ = 254 # =
    L_PAREN = 255  # (
    R_PAREN = 256  # )
    L_BRACK = 257  # {
    R_BRACK = 258  # }
    L_SQBRACK = 259  # [
    R_SQBRACK = 260  # ]