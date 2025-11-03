from ll1parser import *

def main(): 
    S = Nonterminal('S')
    A = Nonterminal('A')
    K = Nonterminal('K')
    B = Nonterminal('B')
    a = Terminal('a')
    b = Terminal('b')
    c = Terminal('c')
    d = Terminal('d')
    e = Terminal('e')
    
    # S → aABe
    # A → bK
    # K → bcK
    # K → ε
    # B → d 
    r1 = Rule(S, [a, A, B, e])
    r2 = Rule(A, [b, K])
    r3 = Rule(K, [b, c, K])
    r4 = Rule(K, [EPSILON])
    r5 = Rule(B, [d])

    rules = {r1,r2,r3,r4,r5}
    g = Grammar(rules, S)
    for nt in g.nonTerminals:
        print('FIRST(' + str(nt) + ') = ' + str(g.firstSet[nt]))
        print('FOLLOW(' + str(nt) + ') = ' + str(g.followSet[nt]))
    
    print()

    print(g.parsingTable)
    print()
    print(g.checkIfLL1())
    print()
    print(g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcde'))
    print(g.parse('abbcbcbbcbcbcbcbcbcbcbcbcbcbcde'))
    print(g.parse('abcbcbcbcbcbcbcbcbcbcbcbcbcbcde'))
    print(g.parse('bcbcbcbcbcbcbcbcbcbcbcbcbcbcde'))
    print(g.parse('abbcbcbcbcbcbcbcbcbcbcbcbcbcbcda'))
    print('----------')
    print()

main()