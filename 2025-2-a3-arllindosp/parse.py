import sys
from lexer import *

class ParseException(Exception):
    pass

class Parser: 
    def __init__(self, lexer):
        self.lexer = lexer
        self.tokenAtual = None
        self.proximoToken = None
        self.nextToken()
        self.nextToken()

    #Retorna true se o Token **atual** casa com tipo de Token esperado
    def checkToken(self, tipo):
        return tipo == self.tokenAtual.kind

    #Retorna true se o próximo Token **(peek)** casa com tipo de Token esperado
    def checkPeek(self, tipo):
        return tipo == self.proximoToken.kind

    #Tenta fazer o casamento do Token atual. Se conseguir, avança para o próximo Token. Do contrário, gera mensagem de erro.
    def match(self, tipo):
        if not self.checkToken(tipo):
            self.abort("Esperava por token do tipo " + tipo.name + ", mas apareceu " + self.tokenAtual.kind.name)
        else:
            self.nextToken()

    # Avançando com os ponteiros dos tokens (atual e peek)
    def nextToken(self):
        self.tokenAtual = self.proximoToken
        self.proximoToken = self.lexer.getToken()

    def abort(self, msg):
        raise ParseException("Erro sintático: "+msg)

    # MINIJAVA GRAMMAR
    # Program ::= MainClass Classes
    # MainClass ::= "class" <IDENTIFIER> "{" "public static void main(String[] a) { System.out.println(); } }"
    # Classes ::= ClassDecl Classes | ϵ
    # ClassDecl ::= "class" <IDENTIFIER> ClassA
    # ClassA ::= "extends" <IDENTIFIER> "{" ClassB | "{" ClassB
    # ClassB ::= "}"
    # | "static" VarDecl ClassB
    # | VarDecl ClassB
    # | "public" MethodDecl ClassC
    # ClassC ::= "}"
    # | "public" MethodDecl ClassC
    # VarDecl ::= Type <IDENTIFIER> ";"
    # MethodDecl ::= Type <IDENTIFIER> "(" MethodA
    # MethodA ::= ")" "{" "}"
    # | Type <IDENTIFIER> MethodB
    # MethodB ::= ")" "{" "}"
    # | "," Type <IDENTIFIER> MethodB
    # Type ::= SimpleType ArrayPart
    # SimpleType ::= "boolean"
    # | "float"
    # | "int"
    # | <IDENTIFIER>
    # ArrayPart ::= ϵ
    # | "[" "]" ArrayPart


    def parse(self):
        self.Program()
        self.match(TokenType.EOF)
        return True
    
    def MainClass(self):
        # MainClass ::= "class" <IDENTIFIER> "{" "public static void main(String[] a) { System.out.println(); } }"
        self.match(TokenType.CLASS)
        self.match(TokenType.IDENT)
        self.match(TokenType.L_BRACK)      # '{'
        self.match(TokenType.PUBLIC)
        self.match(TokenType.STATIC)
        self.match(TokenType.VOID)
        self.match(TokenType.MAIN)         # token MAIN
        self.match(TokenType.L_PAREN)      # '('
        self.match(TokenType.STRING)       # 'String'
        self.match(TokenType.L_SQBRACK)    # '['
        self.match(TokenType.R_SQBRACK)    # ']'
        self.match(TokenType.IDENT)        # nome do parâmetro 
        self.match(TokenType.R_PAREN)      # ')'
        self.match(TokenType.L_BRACK)      # '{' do método
        self.match(TokenType.SYSTEM_OUT_PRINTLN)  # token especial 'System.out.println'
        self.match(TokenType.L_PAREN)
        self.match(TokenType.R_PAREN)
        self.match(TokenType.SEMICOLON)
        self.match(TokenType.R_BRACK)      # '}' fecha método
        self.match(TokenType.R_BRACK)      # '}' fecha classe
        
    def Classes(self):
        # Classes ::= ClassDecl Classes | ϵ
        if self.checkToken(TokenType.CLASS):
            self.ClassDecl()
            self.Classes()
        else:
            # ε
            pass
    def ClassDecl(self):
        # ClassDecl ::= "class" <IDENTIFIER> ClassA
        self.match(TokenType.CLASS)
        self.match(TokenType.IDENT)
        self.ClassA()
        
    def ClassA(self):
        # ClassA ::= "extends" <IDENTIFIER> "{" ClassB | "{" ClassB
        if self.checkToken(TokenType.EXTENDS):
            self.match(TokenType.EXTENDS)
            self.match(TokenType.IDENT)
        self.match(TokenType.L_BRACK)  # '{'
        self.ClassB()

    def ClassB(self):
        # ClassB ::= "}" | "static" VarDecl ClassB | VarDecl ClassB | "public" MethodDecl ClassC
        if self.checkToken(TokenType.R_BRACK):
            self.match(TokenType.R_BRACK)
            return
        elif self.checkToken(TokenType.STATIC):
            self.match(TokenType.STATIC)
            self.VarDecl()
            self.ClassB()
        elif self.checkToken(TokenType.PUBLIC):
            self.match(TokenType.PUBLIC)
            self.MethodDecl()
            self.ClassC()
        else:
            # start of VarDecl: Type begins with BOOLEAN, FLOAT, INT or IDENT
            if (self.checkToken(TokenType.BOOLEAN)
                    or (hasattr(TokenType, 'FLOAT') and self.checkToken(TokenType.FLOAT))
                    or self.checkToken(TokenType.INT)
                    or self.checkToken(TokenType.IDENT)):
                self.VarDecl()
                self.ClassB()
            else:
                self.abort("Esperava membro de classe ou '}'")

    def ClassC(self):
        # ClassC ::= "}" | "public" MethodDecl ClassC
        if self.checkToken(TokenType.R_BRACK):
            self.match(TokenType.R_BRACK)
            return
        elif self.checkToken(TokenType.PUBLIC):
            self.match(TokenType.PUBLIC)
            self.MethodDecl()
            self.ClassC()
        else:
            self.abort("Esperava '}' ou 'public' em ClassC")

    def VarDecl(self):
        # VarDecl ::= Type <IDENTIFIER> ";"
        self.Type()
        self.match(TokenType.IDENT)
        self.match(TokenType.SEMICOLON)

    def MethodDecl(self):
        # MethodDecl ::= Type <IDENTIFIER> "(" MethodA
        self.Type()
        self.match(TokenType.IDENT)
        self.match(TokenType.L_PAREN)
        self.MethodA()

    def MethodA(self):
        # MethodA ::= ")" "{" "}" | Type <IDENTIFIER> MethodB
        if self.checkToken(TokenType.R_PAREN):
            self.match(TokenType.R_PAREN)
            self.match(TokenType.L_BRACK)
            self.match(TokenType.R_BRACK)
            return
        else:
            # at least one parameter: Type IDENT ...
            self.Type()
            self.match(TokenType.IDENT)
            self.MethodB()

    def MethodB(self):
        # MethodB ::= ")" "{" "}" | "," Type <IDENTIFIER> MethodB
        if self.checkToken(TokenType.R_PAREN):
            self.match(TokenType.R_PAREN)
            self.match(TokenType.L_BRACK)
            self.match(TokenType.R_BRACK)
            return
        elif self.checkToken(TokenType.COMMA):
            self.match(TokenType.COMMA)
            self.Type()
            self.match(TokenType.IDENT)
            self.MethodB()
        else:
            self.abort("Esperava ')' ou ',' em MethodB")

    def Type(self):
        # Type ::= SimpleType ArrayPart
        if self.checkToken(TokenType.BOOLEAN):
            self.match(TokenType.BOOLEAN)
        elif hasattr(TokenType, 'FLOAT') and self.checkToken(TokenType.FLOAT):
            self.match(TokenType.FLOAT)
        elif self.checkToken(TokenType.INT):
            self.match(TokenType.INT)
        elif self.checkToken(TokenType.IDENT):
            self.match(TokenType.IDENT)
        else:
            self.abort("Esperava um tipo")
        self.ArrayPart()

    def ArrayPart(self):
        # ArrayPart ::= ϵ | "[" "]" ArrayPart
        if self.checkToken(TokenType.L_SQBRACK):
            self.match(TokenType.L_SQBRACK)
            self.match(TokenType.R_SQBRACK)
            self.ArrayPart()
        else:
            # epsilon
            return
        
        
    # Program ::= MainClass Classes
    def Program(self):
        self.MainClass()
        self.Classes()
