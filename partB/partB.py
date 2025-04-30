#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lexer para LSI-2025-1 usando PLY
Tokens terminais: id, num, if, else, def, print, return, int,
                   < > <= >= != == + - * / = ( ) { } , ;
"""
import sys
import ply.lex as lex

tokens = [
    "ID", "NUM",
    "RELOP_EQ", "RELOP_NE", "RELOP_LT", "RELOP_LE", "RELOP_GT", "RELOP_GE",
    "PLUS","MINUS","TIMES","DIVIDE","ASSIGN",
    "LPAREN","RPAREN","LBRACE","RBRACE","COMMA","SEMI"
]

reserved = {
    "if": "IF",
    "else": "ELSE",
    "def": "DEF",
    "print": "PRINT",
    "return": "RETURN",
    "int": "INT"
}
tokens += list(reserved.values())

t_RELOP_LE = r"<="
t_RELOP_GE = r">="
t_RELOP_EQ = r"=="
t_RELOP_NE = r"!="
t_RELOP_LT = r"<"
t_RELOP_GT = r"> "
t_PLUS    = r"\+"
t_MINUS   = r"-"
t_TIMES   = r"\*"
t_DIVIDE  = r"/"
t_ASSIGN  = r"="
t_LPAREN  = r"\("
t_RPAREN  = r"\)"
t_LBRACE  = r"\{"
t_RBRACE  = r"\}"
t_COMMA   = r","
t_SEMI    = r";"

def t_NUM(t):
    r"\d+"
    t.value = int(t.value)
    return t

def t_ID(t):
    r"[A-Za-z][A-Za-z0-9]*"
    t.type = reserved.get(t.value, "ID")
    return t

t_ignore = " \t\n"

def t_error(t):
    print(f"Erro léxico em {t.lineno}:{t.lexpos+1}: '{t.value[0]}'")
    t.lexer.skip(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python3 partB.py <arquivo.lsi>")
        sys.exit(1)
    data = open(sys.argv[1], encoding="utf-8").read()
    lexer = lex.lex()
    lexer.input(data)
    for tok in lexer:
        print(tok)
