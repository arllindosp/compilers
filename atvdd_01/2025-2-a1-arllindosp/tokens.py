from enum import Enum

class Token:
    def __init__(self, tokenText, tokenKind):
        self.text = tokenText #lexema, a instância específica encontrada.
        self.kind = tokenKind # o tipo de token (TokenType) classificado

    @staticmethod
    def checkIfKeyword(word):
        for kind in TokenType:
            if kind.name == word.upper() and kind.value > 100 and kind.value < 200:
                return kind
        return None
    
    #não modificar
    def _test_print(self):
        kindStr = str(self.kind)
        if self.kind == TokenType.EOF:
            return f"{kindStr} (EOF)"
        
        return  kindStr + " ("+ self.text +")"

    #se desejar alterar o print(token), modifique apenas __repr__
    def __repr__(self):
       #pode modificar
       return self._test_print()


# não renomear os tipos do enum
class TokenType(Enum):
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