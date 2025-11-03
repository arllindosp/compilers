from ll1parser import *
import sys

def test_Grammar1_ll1(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    K = Nonterminal('K')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [b, K])
    r3 = Rule(K, [b, c, K])
    r4 = Rule(K, [EPSILON])
    r5 = Rule(B, [d])

    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert True == g.checkIfLL1()
 

def test_Grammar1_first(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    K = Nonterminal('K')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [b, K])
    r3 = Rule(K, [b, c, K])
    r4 = Rule(K, [EPSILON])
    r5 = Rule(B, [d])

    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {a} == g.firstSet[S]
    assert {b} == g.firstSet[A]
    assert {d} == g.firstSet[B]
    assert {b,EPSILON} == g.firstSet[K]

def test_Grammar1_follow(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    K = Nonterminal('K')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [b, K])
    r3 = Rule(K, [b, c, K])
    r4 = Rule(K, [EPSILON])
    r5 = Rule(B, [d])

    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {EOF} == g.followSet[S]
    assert {d} == g.followSet[A]
    assert {e} == g.followSet[B]
    assert {d} == g.followSet[K]

def test_Grammar1_parsingTable(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    K = Nonterminal('K')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [b, K])
    r3 = Rule(K, [b, c, K])
    r4 = Rule(K, [EPSILON])
    r5 = Rule(B, [d])

    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['b']
    assert [] == g.parsingTable[S]['e']
    assert [] == g.parsingTable[B]['b']
    assert [] == g.parsingTable[B]['a']
    assert [] == g.parsingTable[A]['a']
    assert [] == g.parsingTable[A]['$']
    assert [] == g.parsingTable[K]['a']
    assert [] == g.parsingTable[K]['c']
    assert r5.production in g.parsingTable[B]['d']
    assert r4.production in g.parsingTable[K]['d']
    assert r3.production in g.parsingTable[K]['b']
    assert r2.production in g.parsingTable[A]['b']
    assert r1.production in g.parsingTable[S]['a']

    assert 'Palavra válida' == g.parse('abde')
    assert 'Palavra válida' == g.parse('abbcde')
    assert 'Palavra válida' == g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro sintático, esperava por c e apareceu b!' == g.parse('abbcbcbbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal K: c' == g.parse('abcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal S: b' == g.parse('bcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro sintático, esperava por e e apareceu a!' == g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcda')    

def test_Grammar2_ll1(): 
    S = Nonterminal('S')
    B = Nonterminal('B')
    D = Nonterminal('D')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')

    r1 = Rule(S, [B, c])
    r2 = Rule(S, [D, B])
    r3 = Rule(B, [a, b])
    r4 = Rule(B, [c, S])
    r5 = Rule(D, [EPSILON])
    r6 = Rule(D, [d])
    rules = {r1,r2,r3,r4,r5,r6}
    g = Grammar(rules, S)

    assert False == g.checkIfLL1()

def test_Grammar2_first(): 
    S = Nonterminal('S')
    B = Nonterminal('B')
    D = Nonterminal('D')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')

    r1 = Rule(S, [B, c])
    r2 = Rule(S, [D, B])
    r3 = Rule(B, [a, b])
    r4 = Rule(B, [c, S])
    r5 = Rule(D, [EPSILON])
    r6 = Rule(D, [d])
    rules = {r1,r2,r3,r4,r5,r6}
    g = Grammar(rules, S)

    assert {c,a,d} == g.firstSet[S]
    assert {c,a} == g.firstSet[B]
    assert {d,EPSILON} == g.firstSet[D]

def test_Grammar2_follow(): 
    S = Nonterminal('S')
    B = Nonterminal('B')
    D = Nonterminal('D')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')

    r1 = Rule(S, [B, c])
    r2 = Rule(S, [D, B])
    r3 = Rule(B, [a, b])
    r4 = Rule(B, [c, S])
    r5 = Rule(D, [EPSILON])
    r6 = Rule(D, [d])
    rules = {r1,r2,r3,r4,r5,r6}
    g = Grammar(rules, S)

    assert {c,EOF} == g.followSet[S]
    assert {c,EOF} == g.followSet[B]
    assert {c,a} == g.followSet[D]

def test_Grammar2_parsingTable(): 
    S = Nonterminal('S')
    B = Nonterminal('B')
    D = Nonterminal('D')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')

    r1 = Rule(S, [B, c])
    r2 = Rule(S, [D, B])
    r3 = Rule(B, [a, b])
    r4 = Rule(B, [c, S])
    r5 = Rule(D, [EPSILON])
    r6 = Rule(D, [d])
    rules = {r1,r2,r3,r4,r5,r6}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['b']
    assert [] == g.parsingTable[S]['$']
    assert [] == g.parsingTable[B]['b']
    assert [] == g.parsingTable[B]['d']
    assert [] == g.parsingTable[D]['b']
    assert [] == g.parsingTable[D]['$']
    
    assert r1.production in g.parsingTable[S]['a']
    assert r2.production in g.parsingTable[S]['a']
    assert r1.production in g.parsingTable[S]['c']
    assert r2.production in g.parsingTable[S]['c']
    assert r2.production in g.parsingTable[S]['d']
    
    assert r3.production in g.parsingTable[B]['a']
    assert r4.production in g.parsingTable[B]['c']

    assert r5.production in g.parsingTable[D]['a']
    assert r5.production in g.parsingTable[D]['c']
    assert r6.production in g.parsingTable[D]['d']

    assert 'Erro, gramática não é LL(1)!' == g.parse('abc')
    assert 'Erro, gramática não é LL(1)!' == g.parse('cdab')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ab')

def test_Grammar3_ll1(): 
    S = Nonterminal('S')
    S_prime = Nonterminal('S\'')
    E = Nonterminal('E')
    a = Terminal('a')
    b = Terminal('b')
    e = Terminal('e')
    i = Terminal('i')
    t = Terminal('t')

    r1 = Rule(S, [i, E, t, S, S_prime])
    r2 = Rule(S, [a])
    r3 = Rule(S_prime, [e, S])
    r4 = Rule(S_prime, [EPSILON])
    r5 = Rule(E, [b])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert False == g.checkIfLL1()

def test_Grammar3_first(): 
    S = Nonterminal('S')
    S_prime = Nonterminal('S\'')
    E = Nonterminal('E')
    a = Terminal('a')
    b = Terminal('b')
    e = Terminal('e')
    i = Terminal('i')
    t = Terminal('t')

    r1 = Rule(S, [i, E, t, S, S_prime])
    r2 = Rule(S, [a])
    r3 = Rule(S_prime, [e, S])
    r4 = Rule(S_prime, [EPSILON])
    r5 = Rule(E, [b])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {a,i} == g.firstSet[S]
    assert {e,EPSILON} == g.firstSet[S_prime]
    assert {b} == g.firstSet[E]

def test_Grammar3_follow(): 
    S = Nonterminal('S')
    S_prime = Nonterminal('S\'')
    E = Nonterminal('E')
    a = Terminal('a')
    b = Terminal('b')
    e = Terminal('e')
    i = Terminal('i')
    t = Terminal('t')

    r1 = Rule(S, [i, E, t, S, S_prime])
    r2 = Rule(S, [a])
    r3 = Rule(S_prime, [e, S])
    r4 = Rule(S_prime, [EPSILON])
    r5 = Rule(E, [b])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {e,EOF} == g.followSet[S]
    assert {e,EOF} == g.followSet[S_prime]
    assert {t} == g.followSet[E]

def test_Grammar3_parsingTable(): 
    S = Nonterminal('S')
    S_prime = Nonterminal('S\'')
    E = Nonterminal('E')
    a = Terminal('a')
    b = Terminal('b')
    e = Terminal('e')
    i = Terminal('i')
    t = Terminal('t')

    r1 = Rule(S, [i, E, t, S, S_prime])
    r2 = Rule(S, [a])
    r3 = Rule(S_prime, [e, S])
    r4 = Rule(S_prime, [EPSILON])
    r5 = Rule(E, [b])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['b']
    assert [] == g.parsingTable[S]['$']
    assert [] == g.parsingTable[S_prime]['b']
    assert [] == g.parsingTable[S_prime]['t']
    assert [] == g.parsingTable[E]['t']
    assert [] == g.parsingTable[E]['$']
    
    assert r1.production in g.parsingTable[S]['i']
    assert r2.production in g.parsingTable[S]['a']
    
    assert r3.production in g.parsingTable[S_prime]['e']
    assert r4.production in g.parsingTable[S_prime]['e']
    assert r4.production in g.parsingTable[S_prime]['$']

    assert r5.production in g.parsingTable[E]['b']
    
    assert 'Erro, gramática não é LL(1)!' == g.parse('ibta')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ibtaea')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ibtaibtaea')

def test_Grammar4_ll1(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [A,b,c])
    r3 = Rule(A, [b])
    r4 = Rule(B, [d])
    rules = {r1,r2,r3,r4}
    g = Grammar(rules, S)

    assert False == g.checkIfLL1()

def test_Grammar4_first(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [A,b,c])
    r3 = Rule(A, [b])
    r4 = Rule(B, [d])
    rules = {r1,r2,r3,r4}
    g = Grammar(rules, S)

    assert {a} == g.firstSet[S]
    assert {b} == g.firstSet[A]
    assert {d} == g.firstSet[B]

def test_Grammar4_follow(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [A,b,c])
    r3 = Rule(A, [b])
    r4 = Rule(B, [d])
    rules = {r1,r2,r3,r4}
    g = Grammar(rules, S)

    assert {EOF} == g.followSet[S]
    assert {b,d} == g.followSet[A]
    assert {e} == g.followSet[B]

def test_Grammar4_parsingTable(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')

    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [A,b,c])
    r3 = Rule(A, [b])
    r4 = Rule(B, [d])
    rules = {r1,r2,r3,r4}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['b']
    assert [] == g.parsingTable[S]['c']
    assert [] == g.parsingTable[S]['d']
    assert [] == g.parsingTable[S]['e']
    assert [] == g.parsingTable[S]['$']
    assert [] == g.parsingTable[A]['c']
    assert [] == g.parsingTable[A]['a']
    assert [] == g.parsingTable[A]['e']
    assert [] == g.parsingTable[A]['d']
    assert [] == g.parsingTable[A]['$']
    assert [] == g.parsingTable[B]['a']
    assert [] == g.parsingTable[B]['b']
    assert [] == g.parsingTable[B]['c']
    assert [] == g.parsingTable[B]['e']
    assert [] == g.parsingTable[B]['$']
    
    assert r1.production in g.parsingTable[S]['a']

    assert r2.production in g.parsingTable[A]['b']
    assert r3.production in g.parsingTable[A]['b']
    
    assert r4.production in g.parsingTable[B]['d']
    
    assert 'Erro, gramática não é LL(1)!' == g.parse('abde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('abbcde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('abbcbcbbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('abcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('bcbcbcbcbcbcbcbcbcbcbcbcbcbcde')
    assert 'Erro, gramática não é LL(1)!' == g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcda')

def test_Grammar5_ll1(): 
    E = Nonterminal('E')
    E_prime = Nonterminal('E\'')
    T = Nonterminal('T')
    T_prime = Nonterminal('T\'')
    F = Nonterminal('F')
    i = Terminal('i')
    plus = Terminal('+')
    times = Terminal('*')
    lpar = Terminal('(')
    rpar = Terminal(')')

    r1 = Rule(E, [T, E_prime])
    r2 = Rule(E_prime, [plus, T, E_prime])
    r3 = Rule(E_prime, [EPSILON])
    r4 = Rule(T, [F, T_prime])
    r5 = Rule(T_prime, [times, F, T_prime])
    r6 = Rule(T_prime, [EPSILON])
    r7 = Rule(F, [lpar, E, rpar])
    r8 = Rule(F, [i])
    rules = {r1,r2,r3,r4,r5,r6,r7,r8}
    g = Grammar(rules, E)

    assert True == g.checkIfLL1()

def test_Grammar5_first(): 
    E = Nonterminal('E')
    E_prime = Nonterminal('E\'')
    T = Nonterminal('T')
    T_prime = Nonterminal('T\'')
    F = Nonterminal('F')
    i = Terminal('i')
    plus = Terminal('+')
    times = Terminal('*')
    lpar = Terminal('(')
    rpar = Terminal(')')

    r1 = Rule(E, [T, E_prime])
    r2 = Rule(E_prime, [plus, T, E_prime])
    r3 = Rule(E_prime, [EPSILON])
    r4 = Rule(T, [F, T_prime])
    r5 = Rule(T_prime, [times, F, T_prime])
    r6 = Rule(T_prime, [EPSILON])
    r7 = Rule(F, [lpar, E, rpar])
    r8 = Rule(F, [i])
    rules = {r1,r2,r3,r4,r5,r6,r7,r8}
    g = Grammar(rules, E)

    assert {lpar,i} == g.firstSet[E]
    assert {plus,EPSILON} == g.firstSet[E_prime]
    assert {lpar,i} == g.firstSet[T]
    assert {times,EPSILON} == g.firstSet[T_prime]
    assert {lpar,i} == g.firstSet[F]

def test_Grammar5_follow(): 
    E = Nonterminal('E')
    E_prime = Nonterminal('E\'')
    T = Nonterminal('T')
    T_prime = Nonterminal('T\'')
    F = Nonterminal('F')
    i = Terminal('i')
    plus = Terminal('+')
    times = Terminal('*')
    lpar = Terminal('(')
    rpar = Terminal(')')

    r1 = Rule(E, [T, E_prime])
    r2 = Rule(E_prime, [plus, T, E_prime])
    r3 = Rule(E_prime, [EPSILON])
    r4 = Rule(T, [F, T_prime])
    r5 = Rule(T_prime, [times, F, T_prime])
    r6 = Rule(T_prime, [EPSILON])
    r7 = Rule(F, [lpar, E, rpar])
    r8 = Rule(F, [i])
    rules = {r1,r2,r3,r4,r5,r6,r7,r8}
    g = Grammar(rules, E)

    assert {EOF,rpar} == g.followSet[E]
    assert {EOF,rpar} == g.followSet[E_prime]
    assert {plus, EOF,rpar} == g.followSet[T]
    assert {plus, EOF,rpar} == g.followSet[T_prime]
    assert {times, plus, EOF,rpar} == g.followSet[F]

def test_Grammar5_parsingTable(): 
    E = Nonterminal('E')
    E_prime = Nonterminal('E\'')
    T = Nonterminal('T')
    T_prime = Nonterminal('T\'')
    F = Nonterminal('F')
    i = Terminal('i')
    plus = Terminal('+')
    times = Terminal('*')
    lpar = Terminal('(')
    rpar = Terminal(')')

    r1 = Rule(E, [T, E_prime])
    r2 = Rule(E_prime, [plus, T, E_prime])
    r3 = Rule(E_prime, [EPSILON])
    r4 = Rule(T, [F, T_prime])
    r5 = Rule(T_prime, [times, F, T_prime])
    r6 = Rule(T_prime, [EPSILON])
    r7 = Rule(F, [lpar, E, rpar])
    r8 = Rule(F, [i])
    rules = {r1,r2,r3,r4,r5,r6,r7,r8}
    g = Grammar(rules, E)

    assert [] == g.parsingTable[E]['+']
    assert [] == g.parsingTable[E]['*']
    assert [] == g.parsingTable[E][')']
    assert [] == g.parsingTable[E]['$']

    assert [] == g.parsingTable[E_prime]['i']
    assert [] == g.parsingTable[E_prime]['*']
    assert [] == g.parsingTable[E_prime]['(']

    assert [] == g.parsingTable[T]['+']
    assert [] == g.parsingTable[T]['*']
    assert [] == g.parsingTable[T][')']
    assert [] == g.parsingTable[T]['$']

    assert [] == g.parsingTable[T_prime]['i']
    assert [] == g.parsingTable[T_prime]['(']

    assert [] == g.parsingTable[F]['+']
    assert [] == g.parsingTable[F]['*']
    assert [] == g.parsingTable[F][')']
    assert [] == g.parsingTable[F]['$']
    
    assert r1.production in g.parsingTable[E]['i']
    assert r1.production in g.parsingTable[E]['(']

    assert r2.production in g.parsingTable[E_prime]['+']
    assert r3.production in g.parsingTable[E_prime][')']
    assert r3.production in g.parsingTable[E_prime]['$']
    
    assert r4.production in g.parsingTable[T]['i']
    assert r4.production in g.parsingTable[T]['(']

    assert r6.production in g.parsingTable[T_prime]['+']
    assert r5.production in g.parsingTable[T_prime]['*']
    assert r6.production in g.parsingTable[T_prime][')']
    assert r6.production in g.parsingTable[T_prime]['$']
    
    assert r8.production in g.parsingTable[F]['i']
    assert r7.production in g.parsingTable[F]['(']
    
    assert 'Palavra válida' == g.parse('i')
    assert 'Palavra válida' == g.parse('(i)')
    assert 'Palavra válida' == g.parse('i+i')
    assert 'Palavra válida' == g.parse('i*i')
    assert 'Palavra válida' == g.parse('i+i*i')
    assert 'Palavra válida' == g.parse('i*i+i')
    assert 'Palavra válida' == g.parse('(i+i)*i')
    assert 'Palavra válida' == g.parse('i*(i+i)')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal T: $' == g.parse('i+')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal F: $' == g.parse('i*')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal T: +' == g.parse('i*i++')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal T: *' == g.parse('i+*i')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal T\': i' == g.parse('ii')
    assert 'Erro sintático, esperava por ) e apareceu $!' == g.parse('(i')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal T: )' == g.parse('(i+)')
    assert 'Erro sintático, esperava por ) e apareceu $!' == g.parse('(i+i')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal F: )' == g.parse('(i+i*)')

def test_Grammar6_ll1():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    Z = Nonterminal('Z')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')
    f = Terminal('f')

    r1 = Rule(S, [X, Y, Z])
    r2 = Rule(X, [a, X, b])
    r3 = Rule(X, [EPSILON])
    r4 = Rule(Y, [c,Y,Z,c,X])
    r5 = Rule(Y, [d])
    r6 = Rule(Z, [e,Z,Y,e])
    r7 = Rule(Z, [f])
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, S)

    assert True == g.checkIfLL1()
    
def test_Grammar6_first():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    Z = Nonterminal('Z')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')
    f = Terminal('f')

    r1 = Rule(S, [X, Y, Z])
    r2 = Rule(X, [a, X, b])
    r3 = Rule(X, [EPSILON])
    r4 = Rule(Y, [c,Y,Z,c,X])
    r5 = Rule(Y, [d])
    r6 = Rule(Z, [e,Z,Y,e])
    r7 = Rule(Z, [f])
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, S)
    
    assert {a, c, d} == g.firstSet[S]
    assert {e, f} == g.firstSet[Z]
    assert {c, d} == g.firstSet[Y]
    assert {a, EPSILON} == g.firstSet[X]

def test_Grammar6_follow():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    Z = Nonterminal('Z')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')
    f = Terminal('f')

    r1 = Rule(S, [X, Y, Z])
    r2 = Rule(X, [a, X, b])
    r3 = Rule(X, [EPSILON])
    r4 = Rule(Y, [c,Y,Z,c,X])
    r5 = Rule(Y, [d])
    r6 = Rule(Z, [e,Z,Y,e])
    r7 = Rule(Z, [f])
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, S)

    assert {EOF} == g.followSet[S]
    assert {EOF, c, d} == g.followSet[Z]
    assert {e, f} == g.followSet[Y]
    assert {c, d ,b, e, f} == g.followSet[X]

def test_Grammar6_parsingTable():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    Z = Nonterminal('Z')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')
    f = Terminal('f')

    r1 = Rule(S, [X, Y, Z])
    r2 = Rule(X, [a, X, b])
    r3 = Rule(X, [EPSILON])
    r4 = Rule(Y, [c,Y,Z,c,X])
    r5 = Rule(Y, [d])
    r6 = Rule(Z, [e,Z,Y,e])
    r7 = Rule(Z, [f])
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['b']
    assert [] == g.parsingTable[S]['e']
    assert [] == g.parsingTable[S]['f']
    assert [] == g.parsingTable[S]['$']

    assert [] == g.parsingTable[X]['$']

    assert [] == g.parsingTable[Z]['d']
    assert [] == g.parsingTable[Z]['a']
    assert [] == g.parsingTable[Z]['b']
    assert [] == g.parsingTable[Z]['c']
    assert [] == g.parsingTable[Z]['$']

    assert [] == g.parsingTable[Y]['a']
    assert [] == g.parsingTable[Y]['b']
    assert [] == g.parsingTable[Y]['e']
    assert [] == g.parsingTable[Y]['f']
    assert [] == g.parsingTable[Y]['$']

    assert r1.production in g.parsingTable[S]['d']
    assert r1.production in g.parsingTable[S]['a']
    assert r1.production in g.parsingTable[S]['c']

    assert r3.production in g.parsingTable[X]['d']
    assert r2.production in g.parsingTable[X]['a']
    assert r3.production in g.parsingTable[X]['b']
    assert r3.production in g.parsingTable[X]['e']
    assert r3.production in g.parsingTable[X]['f']
    assert r3.production in g.parsingTable[X]['c']

    assert r6.production in g.parsingTable[Z]['e']
    assert r7.production in g.parsingTable[Z]['f']

    assert r5.production in g.parsingTable[Y]['d']
    assert r4.production in g.parsingTable[Y]['c']

    assert 'Palavra válida' == g.parse('abcdfcf')
    assert 'Palavra válida' == g.parse('ccdfcfcefde')
    assert 'Palavra válida' == g.parse('aabbcdfcf')
    assert 'Palavra válida' == g.parse('ccdfcfcf')
    assert 'Palavra válida' == g.parse('df')
    assert 'Palavra válida' == g.parse('defde')
    assert 'Palavra válida' == g.parse('abcdfcefcdfce')
    assert 'Palavra válida' == g.parse('abcdfcabefde')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal Y: $' == g.parse('aaaabbbb')
    assert 'Erro sintático, esperava por c e apareceu f!' == g.parse('ccccdffffcccc')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal Z: d' == g.parse('abcdfcde')
    assert 'Erro sintático, esperava por e e apareceu $!' == g.parse('defd')

def test_Grammar7_ll1():
    S = Nonterminal('S')
    F = Nonterminal('F')
    lpar = Terminal('(')
    rpar = Terminal(')')
    plus = Terminal('+')
    a = Terminal('a')
    r1 = Rule(S, [F])
    r2 = Rule(S, [lpar, S, plus, F, rpar])
    r3 = Rule(F, [a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert True == g.checkIfLL1()

def test_Grammar7_first():
    S = Nonterminal('S')
    F = Nonterminal('F')
    lpar = Terminal('(')
    rpar = Terminal(')')
    plus = Terminal('+')
    a = Terminal('a')
    r1 = Rule(S, [F])
    r2 = Rule(S, [lpar, S, plus, F, rpar])
    r3 = Rule(F, [a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert {a, lpar} == g.firstSet[S]  
    assert {a} == g.firstSet[F]

def test_Grammar7_follow():
    S = Nonterminal('S')
    F = Nonterminal('F')
    lpar = Terminal('(')
    rpar = Terminal(')')
    plus = Terminal('+')
    a = Terminal('a')
    r1 = Rule(S, [F])
    r2 = Rule(S, [lpar, S, plus, F, rpar])
    r3 = Rule(F, [a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert {plus, EOF} == g.followSet[S]
    assert {plus, rpar, EOF} == g.followSet[F]

def test_Grammar7_parsingTable():
    S = Nonterminal('S')
    F = Nonterminal('F')
    lpar = Terminal('(')
    rpar = Terminal(')')
    plus = Terminal('+')
    a = Terminal('a')
    r1 = Rule(S, [F])
    r2 = Rule(S, [lpar, S, plus, F, rpar])
    r3 = Rule(F, [a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['+']
    assert [] == g.parsingTable[S][')']
    assert [] == g.parsingTable[S]['$']

    assert [] == g.parsingTable[F]['+']
    assert [] == g.parsingTable[F][')']
    assert [] == g.parsingTable[F]['(']
    assert [] == g.parsingTable[F]['$']

    assert r1.production in g.parsingTable[S]['a']
    assert r2.production in g.parsingTable[S]['(']
    
    assert r3.production in g.parsingTable[F]['a']

    assert 'Palavra válida' == g.parse('a')
    assert 'Palavra válida' == g.parse('(a+a)')
    assert 'Palavra válida' == g.parse('((a+a)+a)')
    assert 'Erro sintático, esperava por + e apareceu )!' == g.parse('(a)')
    assert 'Erro sintático, esperava por + e apareceu )!' == g.parse('((a)')
    assert 'Erro sintático, esperava por $ e apareceu: )' == g.parse('(a+a))')
    assert 'Erro sintático, esperava por $ e apareceu: +' == g.parse('((a+a)+a)+a)')

def test_Grammar8_ll1():
    S = Nonterminal('S')
    a = Terminal('a')
    b = Terminal('b')
    r1 = Rule(S, [b,S,a])
    r2 = Rule(S, [a,S,b])
    r3 = Rule(S, [b,a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert False == g.checkIfLL1()

def test_Grammar8_first():
    S = Nonterminal('S')
    a = Terminal('a')
    b = Terminal('b')
    r1 = Rule(S, [b,S,a])
    r2 = Rule(S, [a,S,b])
    r3 = Rule(S, [b,a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert {a, b} == g.firstSet[S]

def test_Grammar8_follow():
    S = Nonterminal('S')
    a = Terminal('a')
    b = Terminal('b')
    r1 = Rule(S, [b,S,a])
    r2 = Rule(S, [a,S,b])
    r3 = Rule(S, [b,a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert {a, b, EOF} == g.followSet[S]

def test_Grammar8_parsingTable():
    S = Nonterminal('S')
    a = Terminal('a')
    b = Terminal('b')
    r1 = Rule(S, [b,S,a])
    r2 = Rule(S, [a,S,b])
    r3 = Rule(S, [b,a])
    rules = {r1,r2,r3}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['$']

    assert r2.production in g.parsingTable[S]['a']
    assert r3.production in g.parsingTable[S]['b']
    assert r1.production in g.parsingTable[S]['b']

    assert 'Erro, gramática não é LL(1)!' == g.parse('baababba')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ba')
    assert 'Erro, gramática não é LL(1)!' == g.parse('aaa')
    assert 'Erro, gramática não é LL(1)!' == g.parse('babaababbaba') 

def test_Grammar9_ll1():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(S, [X,Y,a])
    r2 = Rule(X, [a])
    r3 = Rule(X, [Y,b])
    r4 = Rule(Y, [c])
    r5 = Rule(Y, [EPSILON])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert True == g.checkIfLL1()


def test_Grammar9_first():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(S, [X,Y,a])
    r2 = Rule(X, [a])
    r3 = Rule(X, [Y,b])
    r4 = Rule(Y, [c])
    r5 = Rule(Y, [EPSILON])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {b, c, a} == g.firstSet[S]
    assert {EPSILON, c} == g.firstSet[Y]
    assert {b, c, a} == g.firstSet[X]

def test_Grammar9_follow():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(S, [X,Y,a])
    r2 = Rule(X, [a])
    r3 = Rule(X, [Y,b])
    r4 = Rule(Y, [c])
    r5 = Rule(Y, [EPSILON])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert {EOF} == g.followSet[S]
    assert {b, a} == g.followSet[Y]
    assert {c, a} == g.followSet[X]

def test_Grammar9_parsingTable():
    S = Nonterminal('S')
    X = Nonterminal('X')
    Y = Nonterminal('Y')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(S, [X,Y,a])
    r2 = Rule(X, [a])
    r3 = Rule(X, [Y,b])
    r4 = Rule(Y, [c])
    r5 = Rule(Y, [EPSILON])
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)

    assert [] == g.parsingTable[S]['$']

    assert [] == g.parsingTable[Y]['$']
    
    assert [] == g.parsingTable[X]['$']

    assert r1.production in g.parsingTable[S]['b']
    assert r1.production in g.parsingTable[S]['c']
    assert r1.production in g.parsingTable[S]['a']

    assert r5.production in g.parsingTable[Y]['b']
    assert r4.production in g.parsingTable[Y]['c']
    assert r5.production in g.parsingTable[Y]['a']
    
    assert r3.production in g.parsingTable[X]['b']
    assert r3.production in g.parsingTable[X]['c']
    assert r2.production in g.parsingTable[X]['a']

    assert 'Palavra válida' == g.parse('aca')
    assert 'Palavra válida' == g.parse('bca')
    assert 'Palavra válida' == g.parse('aa')
    assert 'Palavra válida' == g.parse('cbca')
    assert 'Palavra válida' == g.parse('cba')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal Y: $' == g.parse('a')
    assert 'Erro sintático, esperava por $ e apareceu: a' == g.parse('aaa')
    assert 'Erro sintático, esperava por b e apareceu a!' == g.parse('ca')
    assert 'Erro sintático, esperava por a e apareceu $!' == g.parse('ac')

def test_Grammar10_ll1():
    L = Nonterminal('L')
    R = Nonterminal('R')
    Q = Nonterminal('Q')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(L, [R,a])
    r2 = Rule(L, [Q,b,a])
    r3 = Rule(R, [a,b,a])
    r4 = Rule(R, [c,a,b,a])
    r5 = Rule(R, [R,b,c])
    r6 = Rule(Q, [b,b,c])
    r7 = Rule(Q, [b,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, L)

    assert False == g.checkIfLL1()

def test_Grammar10_first():
    L = Nonterminal('L')
    R = Nonterminal('R')
    Q = Nonterminal('Q')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(L, [R,a])
    r2 = Rule(L, [Q,b,a])
    r3 = Rule(R, [a,b,a])
    r4 = Rule(R, [c,a,b,a])
    r5 = Rule(R, [R,b,c])
    r6 = Rule(Q, [b,b,c])
    r7 = Rule(Q, [b,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, L)
    
    assert {b} == g.firstSet[Q]
    assert {a, c} == g.firstSet[R]
    assert {a, c, b} == g.firstSet[L]

def test_Grammar10_follow():
    L = Nonterminal('L')
    R = Nonterminal('R')
    Q = Nonterminal('Q')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(L, [R,a])
    r2 = Rule(L, [Q,b,a])
    r3 = Rule(R, [a,b,a])
    r4 = Rule(R, [c,a,b,a])
    r5 = Rule(R, [R,b,c])
    r6 = Rule(Q, [b,b,c])
    r7 = Rule(Q, [b,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, L)

    assert {b} == g.followSet[Q]
    assert {a, b} == g.followSet[R]
    assert {EOF} == g.followSet[L]

def test_Grammar10_parsingTable():
    L = Nonterminal('L')
    R = Nonterminal('R')
    Q = Nonterminal('Q')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    r1 = Rule(L, [R,a])
    r2 = Rule(L, [Q,b,a])
    r3 = Rule(R, [a,b,a])
    r4 = Rule(R, [c,a,b,a])
    r5 = Rule(R, [R,b,c])
    r6 = Rule(Q, [b,b,c])
    r7 = Rule(Q, [b,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, L)

    assert [] == g.parsingTable[Q]['a']
    assert [] == g.parsingTable[Q]['c']
    assert [] == g.parsingTable[Q]['$']

    assert [] == g.parsingTable[R]['b']
    assert [] == g.parsingTable[R]['$']
    
    assert [] == g.parsingTable[L]['$']

    assert r6.production in g.parsingTable[Q]['b']
    assert r7.production in g.parsingTable[Q]['b']

    assert r5.production in g.parsingTable[R]['a']
    assert r3.production in g.parsingTable[R]['a']
    assert r5.production in g.parsingTable[R]['c']
    assert r4.production in g.parsingTable[R]['c']
    
    assert r1.production in g.parsingTable[L]['a']
    assert r1.production in g.parsingTable[L]['c']
    assert r2.production in g.parsingTable[L]['b']

    assert 'Erro, gramática não é LL(1)!' == g.parse('bbcba')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ababca')
    assert 'Erro, gramática não é LL(1)!' == g.parse('bbcb')
    assert 'Erro, gramática não é LL(1)!' == g.parse('ababbca')

def test_Grammar11_ll1():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    r1 = Rule(A, [B,a])
    r2 = Rule(B, [d,a,b])
    r3 = Rule(B, [C,b])
    r4 = Rule(C, [c,B])
    r5 = Rule(C, [A,c])
    
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, A)

    assert False == g.checkIfLL1()

def test_Grammar11_first():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    r1 = Rule(A, [B,a])
    r2 = Rule(B, [d,a,b])
    r3 = Rule(B, [C,b])
    r4 = Rule(C, [c,B])
    r5 = Rule(C, [A,c])
    
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, A)

    assert {c, d} == g.firstSet[B]
    assert {c, d} == g.firstSet[A]
    assert {c, d} == g.firstSet[C]

def test_Grammar11_follow():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    r1 = Rule(A, [B,a])
    r2 = Rule(B, [d,a,b])
    r3 = Rule(B, [C,b])
    r4 = Rule(C, [c,B])
    r5 = Rule(C, [A,c])
    
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, A)

    assert {a, b} == g.followSet[B]
    assert {c, EOF} == g.followSet[A]
    assert {b} == g.followSet[C]

def test_Grammar11_parsingTable():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    r1 = Rule(A, [B,a])
    r2 = Rule(B, [d,a,b])
    r3 = Rule(B, [C,b])
    r4 = Rule(C, [c,B])
    r5 = Rule(C, [A,c])
    
    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, A)

    assert [] == g.parsingTable[B]['a']
    assert [] == g.parsingTable[B]['b']
    assert [] == g.parsingTable[B]['$']

    assert [] == g.parsingTable[A]['a']
    assert [] == g.parsingTable[A]['b']
    assert [] == g.parsingTable[A]['$']

    assert [] == g.parsingTable[C]['a']
    assert [] == g.parsingTable[C]['b']
    assert [] == g.parsingTable[C]['$']

    assert r3.production in g.parsingTable[B]['c']
    assert r2.production in g.parsingTable[B]['d']
    assert r3.production in g.parsingTable[B]['d']
    
    assert r1.production in g.parsingTable[A]['c']
    assert r1.production in g.parsingTable[A]['d']

    assert r5.production in g.parsingTable[C]['c']
    assert r4.production in g.parsingTable[C]['c']
    assert r5.production in g.parsingTable[C]['d']
    
    assert 'Erro, gramática não é LL(1)!' == g.parse('dabacba')
    assert 'Erro, gramática não é LL(1)!' == g.parse('cdabba')
    assert 'Erro, gramática não é LL(1)!' == g.parse('daa')
    assert 'Erro, gramática não é LL(1)!' == g.parse('cdabbaccba')

def test_Grammar12_ll1():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    p = Terminal('p')
    m = Terminal('m')
    l = Terminal('l')
    r = Terminal('r')
    r1 = Rule(A, [l,A,B,r])
    r2 = Rule(A, [a])
    r3 = Rule(B, [p,A,C])
    r4 = Rule(B, [C,b])
    r5 = Rule(B, [EPSILON])
    r6 = Rule(C, [EPSILON])
    r7 = Rule(C, [m,A,B,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, A)

    assert True == g.checkIfLL1()


def test_Grammar12_first():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    p = Terminal('p')
    m = Terminal('m')
    l = Terminal('l')
    r = Terminal('r')
    r1 = Rule(A, [l,A,B,r])
    r2 = Rule(A, [a])
    r3 = Rule(B, [p,A,C])
    r4 = Rule(B, [C,b])
    r5 = Rule(B, [EPSILON])
    r6 = Rule(C, [EPSILON])
    r7 = Rule(C, [m,A,B,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, A)

    assert {m, EPSILON} == g.firstSet[C]
    assert {l, a} == g.firstSet[A]
    assert {m, b, EPSILON, p} == g.firstSet[B]

def test_Grammar12_follow():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    p = Terminal('p')
    m = Terminal('m')
    l = Terminal('l')
    r = Terminal('r')
    r1 = Rule(A, [l,A,B,r])
    r2 = Rule(A, [a])
    r3 = Rule(B, [p,A,C])
    r4 = Rule(B, [C,b])
    r5 = Rule(B, [EPSILON])
    r6 = Rule(C, [EPSILON])
    r7 = Rule(C, [m,A,B,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, A)

    assert {r, b, c} == g.followSet[C]
    assert {c, m, EOF, b, r, p} == g.followSet[A]
    assert {r, c} == g.followSet[B]

def test_Grammar12_parsingTable():
    A = Nonterminal('A')
    B = Nonterminal('B')
    C = Nonterminal('C')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    p = Terminal('p')
    m = Terminal('m')
    l = Terminal('l')
    r = Terminal('r')
    r1 = Rule(A, [l,A,B,r])
    r2 = Rule(A, [a])
    r3 = Rule(B, [p,A,C])
    r4 = Rule(B, [C,b])
    r5 = Rule(B, [EPSILON])
    r6 = Rule(C, [EPSILON])
    r7 = Rule(C, [m,A,B,c])
    
    rules = {r1,r2,r3,r4,r5,r6,r7}
    g = Grammar(rules, A)

    assert [] == g.parsingTable[C]['l']
    assert [EPSILON] in g.parsingTable[C]['c']
    assert [m, A, B, c] in g.parsingTable[C]['m']
    assert [EPSILON] in g.parsingTable[C]['b']
    assert [] == g.parsingTable[C]['a']
    assert [EPSILON] in g.parsingTable[C]['r']
    assert [] == g.parsingTable[C]['p']
    assert [] == g.parsingTable[C]['$']
    assert [l, A, B, r] in g.parsingTable[A]['l']
    assert [] == g.parsingTable[A]['c']
    assert [] == g.parsingTable[A]['m']
    assert [] == g.parsingTable[A]['b']
    assert [a] in g.parsingTable[A]['a']
    assert [] == g.parsingTable[A]['r']
    assert [] == g.parsingTable[A]['p']
    assert [] == g.parsingTable[A]['$']
    assert [] == g.parsingTable[B]['l']
    assert [EPSILON] in g.parsingTable[B]['c']
    assert [C, b] in g.parsingTable[B]['m']
    assert [C, b] in g.parsingTable[B]['b']
    assert [] == g.parsingTable[B]['a']
    assert [EPSILON] in g.parsingTable[B]['r']
    assert [p, A, C] in g.parsingTable[B]['p']
    assert [] == g.parsingTable[B]['$']

    assert 'Palavra válida' == g.parse('lar')
    assert 'Palavra válida' == g.parse('llarplarr')
    assert 'Palavra válida' == g.parse('llarplarmlarcr')
    assert 'Palavra válida' == g.parse('llamlarcbrplarmlarcr')
    assert 'Palavra válida' == g.parse('labr')
    assert 'Palavra válida' == g.parse('llabrplarr')
    assert 'Palavra válida' == g.parse('llabrplabrmlabrcr')
    assert 'Palavra válida' == g.parse('llamlabrcbrplabrmlabrcr')
    assert 'Erro sintático, esperava por r e apareceu c!' == g.parse('labcr')
    assert 'Erro sintático, caractere inesperado para resolver não-terminal B: l' == g.parse('llabrlplarr')
    assert 'Erro sintático, esperava por r e apareceu p!' == g.parse('llarbplabrcmlabrcr')
    assert 'Erro sintático, esperava por $ e apareceu: a' == g.parse('llamlabrcbrplabrmlabrbcra')

def test_Grammar13_emptyString():
    S = Nonterminal('S')
    a = Terminal('a')
    r1 = Rule(S, [a, S])
    r2 = Rule(S, [EPSILON])
    g = Grammar({r1, r2}, S)
    
    assert 'Palavra válida' == g.parse('')
    assert 'Palavra válida' == g.parse('a')
    assert 'Palavra válida' == g.parse('aaaa')

def test_Grammar14_cyclicGrammar():
    S = Nonterminal('S')
    A = Nonterminal('A')
    a = Terminal('a')
    b = Terminal('b')
    r1 = Rule(S, [A, a])
    r2 = Rule(A, [A])
    r3 = Rule(A, [b])
    g = Grammar({r1, r2, r3}, S)

    assert {b} == g.firstSet[A]
    assert {b} == g.firstSet[S]
    assert {a} == g.followSet[A]
    assert False == g.checkIfLL1()
