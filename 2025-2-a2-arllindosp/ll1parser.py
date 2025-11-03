import enum
import sys

class SymbolType(enum.Enum):
    TERMINAL = 0
    NONTERMINAL = 1
    EPSILON = 2
    EOF = 3

class Symbol:
    def __init__(self,name,type):
        self.name = name
        self.type = type
    def __repr__(self):
        return self.__str__()
    def __str__(self):
        return self.name

class Nonterminal(Symbol):
    def __init__(self, name):
        super().__init__(name, SymbolType.NONTERMINAL)

class Terminal(Symbol):
    def __init__(self, name):
        super().__init__(name, SymbolType.TERMINAL)

class SpecialSymbol(Symbol):
    def __init__(self, name, type):
        if type == SymbolType.EPSILON or type == SymbolType.EOF: 
            super().__init__(name, type)
        else: 
            sys.exit('Tipo inválido')

EPSILON = SpecialSymbol('ε', SymbolType.EPSILON)
EOF = SpecialSymbol('$', SymbolType.EOF)

class Rule: 
    def __init__(self, nt, production):
        self.nonterminal = nt
        self.production = production
    def __str__(self):
        return str(self.nonterminal) + " -> " + ' '.join([str(e) for e in self.production])

class Grammar:
    def __init__(self, productions, startSymbol):
        self.productions = productions
        self.startSymbol = startSymbol
        self.nonTerminals = set()
        self.terminals = set()
        for p in productions:
            self.nonTerminals.add(p.nonterminal)
            for s in p.production:
                if isinstance(s,Terminal):
                    self.terminals.add(s)

        self.firstSet = {}
        self.followSet = {}
        self.parsingTable = {}
        self.buildFirstSets()
        self.buildFollowSets()
        self.generateParsingTable()
    
    #TODO implementar construção dos conjuntos FIRST da gramática
    def buildFirstSets(self):
        #Condição inicial dos conjuntos FIRST (incluindo definição de FIRST(t)=t onde t é um terminal, EOF, ou EPSILON)
        self.firstSet[EOF] = {EOF}
        self.firstSet[EPSILON] = {EPSILON}
        for t in self.terminals:
            self.firstSet[t] = {t}
        for nt in self.nonTerminals:
            self.firstSet[nt] = set()
        
    #Completar a implementação construindo conjuntos FIRST para cada um dos não-terminais
    

        #Montando os conjuntos que possuem simbolos termianis de imediato em suas productions
        for production in self.productions:
            
            old_size = len(self.firstSet[production.nonterminal])
            element  = production.production[0]
            
            if element in self.terminals or element == EPSILON:
                self.firstSet[production.nonterminal].add(element)
            else:
                continue

            new_size = len(self.firstSet[production.nonterminal])
            if new_size > old_size:
                changed = True
        
        # Algoritmo iterativo para calcular FIRST corretamente
        changed = True
        while changed:
            changed = False
            
            for production in self.productions:
                old_size = len(self.firstSet[production.nonterminal])
                
                # Calcula FIRST para esta produção: A → X₁X₂...Xₙ
                production_symbols = production.production
                
                # Percorre todos os símbolos da produção
                for i, symbol in enumerate(production_symbols):
                    
                    if symbol in self.terminals:
                        # Se é terminal, adiciona ao FIRST e para
                        self.firstSet[production.nonterminal].add(symbol)
                        break
                    elif symbol == EPSILON:
                        # Se é epsilon, adiciona ao FIRST e para
                        self.firstSet[production.nonterminal].add(EPSILON)
                        break
                    else:
                        # Se é não-terminal, adiciona FIRST(symbol) - {ε}
                        first_without_epsilon = self.firstSet[symbol] - {EPSILON}
                        self.firstSet[production.nonterminal].update(first_without_epsilon)
                        
                        # Se FIRST(symbol) não contém ε, para aqui
                        if EPSILON not in self.firstSet[symbol]:
                            break
                        
                        # Se chegou ao último símbolo e todos podem produzir ε
                        if i == len(production_symbols) - 1:
                            self.firstSet[production.nonterminal].add(EPSILON)
                
                new_size = len(self.firstSet[production.nonterminal])
                if new_size > old_size:
                    changed = True            


    #TODO implementar construção dos conjuntos FOLLOW da gramática
    def buildFollowSets(self):
        #Condição inicial dos conjuntos FOLLOW
        for nt in self.nonTerminals:
            self.followSet[nt] = set()
        self.followSet[self.startSymbol].add(EOF)
        #Completar a implementação construindo conjuntos FOLLOW para cada um dos não-terminais

        # Algoritmo iterativo para calcular conjuntos FOLLOW
        changed = True
        while changed:
            changed = False
            
            # Para cada produção A → α
            for production in self.productions:
                # Para cada símbolo na produção
                for i, symbol in enumerate(production.production):
                    # Só processa não-terminais
                    if symbol in self.nonTerminals:
                        old_size = len(self.followSet[symbol])
                        
                        # Verifica se há símbolos após este não-terminal
                        if i + 1 < len(production.production):
                            # Caso: A → αBβ (há símbolos depois de B)
                            beta = production.production[i + 1:]  # β = símbolos restantes
                            
                            # Calcula FIRST(β)
                            first_beta = set()
                            all_have_epsilon = True
                            
                            for beta_symbol in beta:
                                if beta_symbol in self.terminals:
                                    first_beta.add(beta_symbol)
                                    all_have_epsilon = False
                                    break
                                elif beta_symbol == EPSILON:
                                    first_beta.add(EPSILON)
                                    break
                                else:  # é não-terminal
                                    first_beta.update(self.firstSet[beta_symbol] - {EPSILON})
                                    if EPSILON not in self.firstSet[beta_symbol]:
                                        all_have_epsilon = False
                                        break
                            
                            # Se todos os símbolos em β podem derivar ε
                            if all_have_epsilon:
                                first_beta.add(EPSILON)
                            
                            # Adiciona FIRST(β) - {ε} ao FOLLOW(B)
                            self.followSet[symbol].update(first_beta - {EPSILON})
                            
                            # Se ε ∈ FIRST(β), adiciona FOLLOW(A) ao FOLLOW(B)
                            if EPSILON in first_beta:
                                self.followSet[symbol].update(self.followSet[production.nonterminal])
                        
                        else:
                            # Caso: A → αB (B está no final)
                            # FOLLOW(B) inclui FOLLOW(A)
                            self.followSet[symbol].update(self.followSet[production.nonterminal])
                        
                        new_size = len(self.followSet[symbol])
                        if new_size > old_size:
                            changed = True

    def calculateFirstOfProduction(self, production_symbols):
        """Calcula FIRST de uma sequência de símbolos (lado direito de uma produção)"""
        first_set = set()
        
        # Percorre todos os símbolos da produção
        for i, symbol in enumerate(production_symbols):
            if symbol in self.terminals:
                # Se é terminal, adiciona ao FIRST e para
                first_set.add(symbol)
                break
            elif symbol == EPSILON:
                # Se é epsilon, adiciona ao FIRST e para
                first_set.add(EPSILON)
                break
            else:
                # Se é não-terminal, adiciona FIRST(symbol) - {ε}
                first_without_epsilon = self.firstSet[symbol] - {EPSILON}
                first_set.update(first_without_epsilon)
                
                # Se FIRST(symbol) não contém ε, para aqui
                if EPSILON not in self.firstSet[symbol]:
                    break
                
                # Se chegou ao último símbolo e todos podem produzir ε
                if i == len(production_symbols) - 1:
                    first_set.add(EPSILON)
        
        return first_set

    #TODO implementar geração da tabela de parsing da gramática
    def generateParsingTable(self):
        #Estrutura da tabela
        for nt in self.nonTerminals:
            self.parsingTable[nt] = {}
            for t in self.terminals:
                self.parsingTable[nt][t.name] = []
            #Adicionando EOF como coluna
            self.parsingTable[nt]['$'] = []

        # Preenche a tabela de parsing
        for production in self.productions:
            # Calcula FIRST da produção (lado direito da regra)
            first_production = self.calculateFirstOfProduction(production.production)
            
            # Para cada terminal no FIRST da produção
            for t in first_production:
                if t in self.terminals:
                    # Se é terminal, adiciona produção na célula [A, t]
                    self.parsingTable[production.nonterminal][t.name].append(production.production)
                elif t == EPSILON:
                    # Se é epsilon, adiciona produção nas células [A, b] onde b ∈ FOLLOW(A)
                    for column in self.followSet[production.nonterminal]:
                        if column in self.terminals:
                            self.parsingTable[production.nonterminal][column.name].append(production.production)
                        elif column == EOF:
                            self.parsingTable[production.nonterminal]['$'].append(production.production)

    #TODO implementar checagem da gramática. Retorna True se a gramática é LL(1), False do contrário.
    def checkIfLL1(self):
        # Uma gramática é LL(1) se não há conflitos na tabela de parsing
        # Ou seja, cada célula tem no máximo uma produção
        for nonterminal in self.nonTerminals:
            for terminal_name in self.parsingTable[nonterminal]:
                if len(self.parsingTable[nonterminal][terminal_name]) > 1:
                    return False
        return True

    #Algoritmo de parsing, assume que cada caractere é um token 
    #NÃO É NECESSÁRIO MUDAR ESTE ALGORITMO
    def parse(self, sentence): 
        if not self.checkIfLL1():
            return 'Erro, gramática não é LL(1)!'
        else:
            size = len(sentence)
            i = 0
            stack = [EOF, self.startSymbol]
            a = sentence[i] if size > 0 else '$'            
            X = stack[len(stack)-1]
            while X != EOF:
                if type(X) == Terminal: 
                    if X.name == a: 
                        stack.pop()
                        i = i+1
                        if i < size:
                            a = sentence[i]
                        else: 
                            a = '$'
                    else:
                        return 'Erro sintático, esperava por '+X.name+' e apareceu '+a+'!'
                elif type(X) == Nonterminal:  
                    if len(self.parsingTable[X][a]) == 0:
                        return 'Erro sintático, caractere inesperado para resolver não-terminal '+X.name+': ' + a
                    elif len(self.parsingTable[X][a]) == 1:
                        stack.pop()
                        for s in reversed(self.parsingTable[X][a][0]):
                            if s != EPSILON:
                                stack.append(s)
                else:
                    return 'Tem algo errado com a tabela de parsing.'
                X = stack[len(stack)-1]
            if a == '$':
                return 'Palavra válida'
            else: 
                return 'Erro sintático, esperava por $ e apareceu: '+a
