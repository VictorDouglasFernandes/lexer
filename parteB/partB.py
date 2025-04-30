#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisador Léxico Parte B
Integrantes: 
- Gustavo Cortez de brito (21202331)
- Víctor Douglas Fernandes (21204918)
- João Vitor Duarte Domingos (21203405)
- Manuela Schmitz (20102278)
"""

import sys
import ply.lex as lex

# Palavras-chave da linguagem
keywords = {
    'def': 'DEF',
    'int': 'INT',
    'if': 'IF',
    'else': 'ELSE',
    'return': 'RETURN',
    'print': 'PRINT'
}

symbol_table = {
    'lexemas': set(),  # Armazena identificadores
    'keywords': list(keywords.keys())  # Armazena palavras-chave
}

# Lista de tokens
tokens = [
    'ID', 'NUM',
    'RELOP', 'ATRIB',
    'ABRE_PAR', 'FECHA_PAR',
    'ABRE_CHAVE', 'FECHA_CHAVE',
    'VIRGULA', 'PONTO_VIRGULA',
    'MAIS', 'MENOS', 'VEZES', 'DIVIDE'
] + list(keywords.values())

# Operadores relacionais
rel_ops = {
    '<=': 'RELOP',
    '>=': 'RELOP',
    '==': 'RELOP',
    '!=': 'RELOP',
    '<': 'RELOP',
    '>': 'RELOP'
}

# Símbolos especiais
literals = ['=', '+', '-', '*', '/', '(', ')', '{', '}', ',', ';']

# Expressões regulares
t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # Verifica se é palavra-chave ou ID
    if t.value not in symbol_table['keywords']:
        symbol_table['lexemas'].add(t.value)  # Adiciona à tabela
    t.type = keywords.get(t.value, 'ID')
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_RELOP(t):
    r'<=|>=|==|!=|<|>'
    t.type = rel_ops.get(t.value, 'RELOP')
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    pos = t.lexpos + 1
    print(f"Erro léxico na linha {t.lineno}, coluna {pos}: Caractere inválido '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex.lex()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python parteB.py arquivo.lsi")
        sys.exit(1)

    try:
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            data = f.read()
        
        lexer.input(data)
        tokens = []
        symbol_table['lexemas'].clear()  # Limpa a tabela para cada execução
        
        while True:
            tok = lexer.token()
            if not tok: 
                break
                
            # Formata a saída dos tokens
            if tok.type == 'ID':
                tokens.append('id')
            elif tok.type == 'NUM':
                tokens.append('int')
            elif tok.type in keywords.values():
                tokens.append(tok.value.lower())
            elif tok.type == 'RELOP':
                tokens.append(tok.value)
            else:
                tokens.append(tok.value)
        
        # Saída dos tokens e tabela de símbolos
        print("Tokens:", tokens)
        print("\nTabela de Símbolos:")
        print("Palavras-chave:", symbol_table['keywords'])
        print("Identificadores:", list(symbol_table['lexemas']))
        
    except FileNotFoundError:
        print(f"Erro: Arquivo {sys.argv[1]} não encontrado")
        sys.exit(1)