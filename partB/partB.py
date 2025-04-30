#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lexer para LSI-2025-1 usando PLY, com comentários em Português.
"""
import sys
import ply.lex as lex

# ------------------------------------------------------------------------------
# 1) Definir os nomes de tokens e seus padrões regex
# ------------------------------------------------------------------------------

# Operadores relacionais e seus padrões
REL_OPS = {
    "LE": r"<=",    # menor ou igual
    "GE": r">=",    # maior ou igual
    "EQ": r"==",    # igual
    "NE": r"!=",    # diferente
    "LT": r"<",     # menor
    "GT": r">"      # maior
}

# Operadores aritméticos e de atribuição
ARITH_OPS = {
    "PLUS":   r"\+",   # soma
    "MINUS":  r"-",    # subtração
    "TIMES":  r"\*",   # multiplicação
    "DIVIDE": r"/",    # divisão
    "ASSIGN": r"="     # atribuição
}

# Pontuação: parênteses, chaves, vírgula e ponto-e-vírgula
PUNCTUATION = {
    "LPAREN": r"\(",  # abre parêntese
    "RPAREN": r"\)",  # fecha parêntese
    "LBRACE": r"\{",  # abre chave
    "RBRACE": r"\}",  # fecha chave
    "COMMA":  r",",   # vírgula
    "SEMI":   r";"    # ponto-e-vírgula
}

# Palavras-chave reservadas
palavras_reservadas = {
    "if":     "IF",
    "else":   "ELSE",
    "def":    "DEF",
    "print":  "PRINT",
    "return": "RETURN",
    "int":    "INT"
}

# Lista inicial de tokens
tokens = [
    "ID",   # identificador
    "NUM"   # literal inteiro
]
# Adiciona tokens para operadores relacionais
for nome in REL_OPS:
    tokens.append(f"RELOP_{nome}")
# Adiciona tokens para operadores aritméticos
for nome in ARITH_OPS:
    tokens.append(nome)
# Adiciona tokens de pontuação
for nome in PUNCTUATION:
    tokens.append(nome)
# Adiciona tokens para palavras-chave
tokens += list(palavras_reservadas.values())

# ------------------------------------------------------------------------------
# 2) Associar cada nome de token ao seu padrão regex
# ------------------------------------------------------------------------------

# Relational operators
t_RELOP_LE = REL_OPS["LE"]
t_RELOP_GE = REL_OPS["GE"]
t_RELOP_EQ = REL_OPS["EQ"]
t_RELOP_NE = REL_OPS["NE"]
t_RELOP_LT = REL_OPS["LT"]
t_RELOP_GT = REL_OPS["GT"]

# Arithmetic and assignment
t_PLUS   = ARITH_OPS["PLUS"]
t_MINUS  = ARITH_OPS["MINUS"]
t_TIMES  = ARITH_OPS["TIMES"]
t_DIVIDE = ARITH_OPS["DIVIDE"]
t_ASSIGN = ARITH_OPS["ASSIGN"]

# Pontuação
t_LPAREN = PUNCTUATION["LPAREN"]
t_RPAREN = PUNCTUATION["RPAREN"]
t_LBRACE = PUNCTUATION["LBRACE"]
t_RBRACE = PUNCTUATION["RBRACE"]
t_COMMA  = PUNCTUATION["COMMA"]
t_SEMI   = PUNCTUATION["SEMI"]

# ------------------------------------------------------------------------------
# 3) Definir funções de ação para tokens mais complexos
# ------------------------------------------------------------------------------

def t_NUM(t):
    r"\d+"
    # Converte a sequência de dígitos em inteiro
    t.value = int(t.value)
    return t

def t_ID(t):
    r"[A-Za-z][A-Za-z0-9]*"
    # Se for palavra-chave, ajusta o tipo de token
    t.type = palavras_reservadas.get(t.value, "ID")
    return t

# ------------------------------------------------------------------------------
# 4) Especificar caracteres a serem ignorados
# ------------------------------------------------------------------------------
t_ignore = " \t\n"    # ignora espaços, tabs e quebras de linha

# ------------------------------------------------------------------------------
# 5) Tratamento de erro
# ------------------------------------------------------------------------------
def t_error(t):
    # Reporta a posição (linha e coluna) do caracter inesperado
    coluna = t.lexpos + 1
    print(f"Erro léxico em {t.lineno}:{coluna}: caracter inesperado '{t.value[0]}'")
    # Descarta o caracter e continua
    t.lexer.skip(1)

# ------------------------------------------------------------------------------
# 6) Ponto de entrada ao executar o script
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    # Verifica se o usuário passou exatamente um argumento (caminho do arquivo)
    if len(sys.argv) != 2:
        print("Uso: python partB.py <arquivo.lsi>")
        sys.exit(1)

    arquivo_fonte = sys.argv[1]
    with open(arquivo_fonte, encoding="utf-8") as f:
        dados = f.read()

    # Constroi o lexer e fornece os dados de entrada
    lexer = lex.lex()
    lexer.input(dados)

    # Imprime todos os tokens reconhecidos
    for token in lexer:
        print(token)
