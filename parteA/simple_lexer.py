"""
Analisador Léxico Parte A
Integrantes: 
- Gustavo Cortez de brito (21202331)
- Víctor Douglas Fernandes (21204918)
- João Vitor Duarte Domingos (21203405)
- Manuela Schmitz (20102278)
"""

import sys

# Palavras-chave pré-definidas
keywords = ['if', 'else', 'def', 'return', 'print', 'int']
symbol_table = {k: 'keyword' for k in keywords}  # Tabela de símbolos inicializada com keywords

# Caracteres válidos
numbers = ['0','1','2','3','4','5','6','7','8','9']
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
firstOperators = ['>','<','=','!']
secondOperators = ['=']

def relationalOperator(char: str, current: str) -> bool:
    if len(current) >= 2:
        return False
    if len(current) == 1:
        return (current in ['>','<','!'] and char in secondOperators)
    return char in firstOperators

if len(sys.argv) < 2:
    print("You should specify the file name")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    code = file.read()

tokens = []  # Lista para armazenar os tokens

for line in code.split('\n'):
    remaining = line
    while len(remaining) > 0:
        if remaining[0] == ' ':
            remaining = remaining[1:]
            continue
        
        variable, number, operator = '', '', ''
        stop_var, stop_num, stop_op = False, False, False

        for char in remaining:
            has_match = False

            # Reconhece números
            if not stop_num and char in numbers:
                number += char
                has_match = True
            else:
                stop_num = True

            # Reconhece identificadores/palavras-chave
            if not stop_var and ((variable == '' and char in chars) or (variable and (char in chars + numbers))):
                variable += char
                has_match = True
            else:
                stop_var = True

            # Reconhece operadores relacionais
            if not stop_op and relationalOperator(char, operator):
                operator += char
                has_match = True
            else:
                stop_op = True

            if not has_match:
                break

        # Determina qual token tem prioridade
        max_len = max(len(variable), len(number), len(operator))
        if max_len == 0:
            print(f"Erro léxico: caractere inválido '{remaining[0]}' na linha '{line}'")
            remaining = remaining[1:]
            continue

        if len(variable) == max_len:
            # Verifica se é palavra-chave
            token_type = 'keyword' if variable in keywords else 'ID'
            if variable not in symbol_table and token_type == 'ID':
                symbol_table[variable] = 'ID'  # Adiciona novo ID à tabela
            tokens.append((variable, token_type))
            remaining = remaining[len(variable):]
        elif len(number) == max_len:
            tokens.append((number, 'NUM'))
            remaining = remaining[len(number):]
        elif len(operator) == max_len:
            tokens.append((operator, 'RELOP'))
            remaining = remaining[len(operator):]

print("\nLista de Tokens:")
for token, tipo in tokens:
    print(f"Token: {token} \t Tipo: {tipo}")

print("\nTabela de Símbolos:")
for lexema, tipo in symbol_table.items():
    print(f"Lexema: {lexema} \t Tipo: {tipo}")