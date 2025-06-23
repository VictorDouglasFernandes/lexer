"""
Analisador Léxico Parte A
Integrantes: 
- Gustavo Cortez de brito (21202331)
- Víctor Douglas Fernandes (21204918)
- João Vitor Duarte Domingos (21203405)
- Manuela Schmitz (20102278)
"""

import sys

# Define as palavras reservadas da linguagem que serão reconhecidas como keywords
keywords = ['if', 'else', 'def', 'return', 'print', 'int']
# Inicializa a tabela de símbolos com as keywords. A tabela de símbolos mantém um registro de todos os identificadores encontrados
symbol_table = {k: 'keyword' for k in keywords}

# Define os caracteres válidos que podem ser usados na linguagem
# Lista de dígitos permitidos
numbers = ['0','1','2','3','4','5','6','7','8','9']
# Lista de letras permitidas (maiúsculas e minúsculas)
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z',
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
# Caracteres que podem iniciar um operador relacional
firstOperators = ['>','<','=','!']
# Caracteres que podem aparecer na segunda posição de um operador relacional
secondOperators = ['=']

def relationalOperator(char: str, current: str) -> bool:
    """
    Verifica se um caractere pode fazer parte de um operador relacional
    Args:
        char: Caractere atual sendo analisado
        current: Operador parcialmente construído até agora
    Returns:
        bool: True se o caractere pode fazer parte do operador, False caso contrário
    """
    if len(current) >= 2:  # Operadores relacionais têm no máximo 2 caracteres
        return False
    if len(current) == 1:  # Se já temos um caractere, só podemos adicionar '='
        return (current in ['>','<','!'] and char in secondOperators)
    return char in firstOperators  # Primeiro caractere deve ser >, <, = ou !

# Verifica se foi fornecido um arquivo como argumento
if len(sys.argv) < 2:
    print("You should specify the file name")
    sys.exit(1)

filename = sys.argv[1]

# Lê o conteúdo do arquivo
with open(filename, 'r') as file:
    code = file.read()

# Lista para armazenar os tokens identificados
tokens = []

# Processa o código linha por linha
for line in code.split('\n'):
    remaining = line
    while len(remaining) > 0:
        # Ignora espaços em branco
        if remaining[0] == ' ':
            remaining = remaining[1:]
            continue
        
        # Variáveis para construir os tokens
        variable, number, operator = '', '', ''
        # Flags para controlar quando parar de construir cada tipo de token
        stop_var, stop_num, stop_op = False, False, False

        # Analisa caractere por caractere
        for char in remaining:
            has_match = False

            # Tenta reconhecer números (sequência de dígitos)
            if not stop_num and char in numbers:
                number += char
                has_match = True
            else:
                stop_num = True

            # Tenta reconhecer identificadores (começam com letra, podem conter letras e números)
            if not stop_var and ((variable == '' and char in chars) or (variable and (char in chars + numbers))):
                variable += char
                has_match = True
            else:
                stop_var = True

            # Tenta reconhecer operadores relacionais
            if not stop_op and relationalOperator(char, operator):
                operator += char
                has_match = True
            else:
                stop_op = True

            # Se nenhum padrão foi reconhecido, para a análise do token atual
            if not has_match:
                break

        # Determina qual é o token mais longo reconhecido
        # Não acontece de mais de um ter um tamanho igual pois todos começam com caracteres diferentes
        max_len = max(len(variable), len(number), len(operator))
        if max_len == 0:
            # Se nenhum token foi reconhecido, reporta erro e avança um caractere
            print(f"Erro léxico: caractere inválido '{remaining[0]}' na linha '{line}'")
            remaining = remaining[1:]
            continue

        # Adiciona o token reconhecido à lista de tokens
        if len(variable) == max_len:
            # Verifica se é uma keyword ou um identificador
            token_type = 'keyword' if variable in keywords else 'ID'
            if variable not in symbol_table and token_type == 'ID':
                symbol_table[variable] = 'ID'  # Adiciona novo identificador à tabela de símbolos
            tokens.append((variable, token_type))
            remaining = remaining[len(variable):]
        elif len(number) == max_len:
            tokens.append((number, 'NUM'))
            remaining = remaining[len(number):]
        elif len(operator) == max_len:
            tokens.append((operator, 'RELOP'))
            remaining = remaining[len(operator):]

# Imprime os tokens encontrados
print("\nLista de Tokens:")
for token, tipo in tokens:
    print(f"Token: {token} \t Tipo: {tipo}")

# Imprime a tabela de símbolos final
print("\nTabela de Símbolos:")
for lexema, tipo in symbol_table.items():
    print(f"Lexema: {lexema} \t Tipo: {tipo}")