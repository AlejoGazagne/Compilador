# Generated from /home/alejo/Escritorio/Compilador/src/main/python/compiladores.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,31,176,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,6,1,6,1,7,1,
        7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,1,14,1,
        14,1,15,1,15,1,16,1,16,1,16,1,17,1,17,1,17,1,18,1,18,1,18,1,19,1,
        19,1,19,1,20,1,20,1,20,1,21,1,21,1,21,1,22,4,22,119,8,22,11,22,12,
        22,120,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,
        25,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,
        27,1,28,1,28,1,28,1,28,1,29,1,29,1,29,1,29,1,29,1,29,1,29,1,30,1,
        30,3,30,161,8,30,1,30,1,30,1,30,5,30,166,8,30,10,30,12,30,169,9,
        30,1,31,1,31,1,31,1,31,1,32,1,32,0,0,33,1,0,3,0,5,1,7,2,9,3,11,4,
        13,5,15,6,17,7,19,8,21,9,23,10,25,11,27,12,29,13,31,14,33,15,35,
        16,37,17,39,18,41,19,43,20,45,21,47,22,49,23,51,24,53,25,55,26,57,
        27,59,28,61,29,63,30,65,31,1,0,3,2,0,65,90,97,122,1,0,48,57,3,0,
        9,10,13,13,32,32,178,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,
        0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,
        0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,
        0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,
        0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,
        0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,
        0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,1,67,1,0,0,0,3,69,1,0,0,0,5,71,1,
        0,0,0,7,73,1,0,0,0,9,75,1,0,0,0,11,77,1,0,0,0,13,79,1,0,0,0,15,81,
        1,0,0,0,17,83,1,0,0,0,19,85,1,0,0,0,21,87,1,0,0,0,23,89,1,0,0,0,
        25,91,1,0,0,0,27,93,1,0,0,0,29,95,1,0,0,0,31,97,1,0,0,0,33,99,1,
        0,0,0,35,102,1,0,0,0,37,105,1,0,0,0,39,108,1,0,0,0,41,111,1,0,0,
        0,43,114,1,0,0,0,45,118,1,0,0,0,47,122,1,0,0,0,49,126,1,0,0,0,51,
        133,1,0,0,0,53,139,1,0,0,0,55,142,1,0,0,0,57,147,1,0,0,0,59,151,
        1,0,0,0,61,160,1,0,0,0,63,170,1,0,0,0,65,174,1,0,0,0,67,68,7,0,0,
        0,68,2,1,0,0,0,69,70,7,1,0,0,70,4,1,0,0,0,71,72,5,61,0,0,72,6,1,
        0,0,0,73,74,5,40,0,0,74,8,1,0,0,0,75,76,5,41,0,0,76,10,1,0,0,0,77,
        78,5,123,0,0,78,12,1,0,0,0,79,80,5,125,0,0,80,14,1,0,0,0,81,82,5,
        59,0,0,82,16,1,0,0,0,83,84,5,44,0,0,84,18,1,0,0,0,85,86,5,43,0,0,
        86,20,1,0,0,0,87,88,5,45,0,0,88,22,1,0,0,0,89,90,5,37,0,0,90,24,
        1,0,0,0,91,92,5,42,0,0,92,26,1,0,0,0,93,94,5,47,0,0,94,28,1,0,0,
        0,95,96,5,60,0,0,96,30,1,0,0,0,97,98,5,62,0,0,98,32,1,0,0,0,99,100,
        5,60,0,0,100,101,5,61,0,0,101,34,1,0,0,0,102,103,5,62,0,0,103,104,
        5,61,0,0,104,36,1,0,0,0,105,106,5,61,0,0,106,107,5,61,0,0,107,38,
        1,0,0,0,108,109,5,33,0,0,109,110,5,61,0,0,110,40,1,0,0,0,111,112,
        5,38,0,0,112,113,5,38,0,0,113,42,1,0,0,0,114,115,5,124,0,0,115,116,
        5,124,0,0,116,44,1,0,0,0,117,119,3,3,1,0,118,117,1,0,0,0,119,120,
        1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,46,1,0,0,0,122,123,5,
        105,0,0,123,124,5,110,0,0,124,125,5,116,0,0,125,48,1,0,0,0,126,127,
        5,100,0,0,127,128,5,111,0,0,128,129,5,117,0,0,129,130,5,98,0,0,130,
        131,5,108,0,0,131,132,5,101,0,0,132,50,1,0,0,0,133,134,5,119,0,0,
        134,135,5,104,0,0,135,136,5,105,0,0,136,137,5,108,0,0,137,138,5,
        101,0,0,138,52,1,0,0,0,139,140,5,105,0,0,140,141,5,102,0,0,141,54,
        1,0,0,0,142,143,5,101,0,0,143,144,5,108,0,0,144,145,5,115,0,0,145,
        146,5,101,0,0,146,56,1,0,0,0,147,148,5,102,0,0,148,149,5,111,0,0,
        149,150,5,114,0,0,150,58,1,0,0,0,151,152,5,114,0,0,152,153,5,101,
        0,0,153,154,5,116,0,0,154,155,5,117,0,0,155,156,5,114,0,0,156,157,
        5,110,0,0,157,60,1,0,0,0,158,161,3,1,0,0,159,161,5,95,0,0,160,158,
        1,0,0,0,160,159,1,0,0,0,161,167,1,0,0,0,162,166,3,1,0,0,163,166,
        3,3,1,0,164,166,5,95,0,0,165,162,1,0,0,0,165,163,1,0,0,0,165,164,
        1,0,0,0,166,169,1,0,0,0,167,165,1,0,0,0,167,168,1,0,0,0,168,62,1,
        0,0,0,169,167,1,0,0,0,170,171,7,2,0,0,171,172,1,0,0,0,172,173,6,
        31,0,0,173,64,1,0,0,0,174,175,9,0,0,0,175,66,1,0,0,0,5,0,120,160,
        165,167,1,6,0,0
    ]

class compiladoresLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    EQ = 1
    PA = 2
    PC = 3
    LLA = 4
    LLC = 5
    PYC = 6
    COMA = 7
    MAS = 8
    MENOS = 9
    MOD = 10
    MUL = 11
    DIV = 12
    LT = 13
    GT = 14
    LE = 15
    GE = 16
    EQQ = 17
    NEQ = 18
    AND = 19
    ORR = 20
    NUMERO = 21
    INT = 22
    DOUBLE = 23
    WHILE = 24
    IF = 25
    ELSE = 26
    FOR = 27
    RETURN = 28
    ID = 29
    WS = 30
    OTRO = 31

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "'{'", "'}'", "';'", "','", "'+'", "'-'", 
            "'%'", "'*'", "'/'", "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", 
            "'&&'", "'||'", "'int'", "'double'", "'while'", "'if'", "'else'", 
            "'for'", "'return'" ]

    symbolicNames = [ "<INVALID>",
            "EQ", "PA", "PC", "LLA", "LLC", "PYC", "COMA", "MAS", "MENOS", 
            "MOD", "MUL", "DIV", "LT", "GT", "LE", "GE", "EQQ", "NEQ", "AND", 
            "ORR", "NUMERO", "INT", "DOUBLE", "WHILE", "IF", "ELSE", "FOR", 
            "RETURN", "ID", "WS", "OTRO" ]

    ruleNames = [ "LETRA", "DIGITO", "EQ", "PA", "PC", "LLA", "LLC", "PYC", 
                  "COMA", "MAS", "MENOS", "MOD", "MUL", "DIV", "LT", "GT", 
                  "LE", "GE", "EQQ", "NEQ", "AND", "ORR", "NUMERO", "INT", 
                  "DOUBLE", "WHILE", "IF", "ELSE", "FOR", "RETURN", "ID", 
                  "WS", "OTRO" ]

    grammarFileName = "compiladores.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


