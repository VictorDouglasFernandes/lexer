# grammar = {
#     "MAIN": [["STMT"], ["FLIST"], ["ε"]],
#     "FLIST": [["FDEF", "FLIST"], ["FDEF"]],
#     "FDEF": [["def", "id", "(", "PARLIST", ")", "{", "STMTLIST", "}"]],
#     "PARLIST": [["int", "id", ",", "PARLIST"], ["int", "id"], ["ε"]],
#     "STMT": [
#         ["int", "VARLIST", ";"],
#         ["ATRIBST", ";"],
#         ["PRINTST", ";"],
#         ["RETURNST", ";"],
#         ["IFSTMT"],
#         ["{", "STMTLIST", "}"],
#         [";"],
#     ],
#     "VARLIST": [["id", ",", "VARLIST"], ["id"]],
#     "ATRIBST": [["id", "=", "EXPR"], ["id", "=", "FCALL"]],
#     "FCALL": [["id", "(", "PARLISTCALL", ")"]],
#     "PARLISTCALL": [["id", ",", "PARLISTCALL"], ["id"], ["ε"]],
#     "PRINTST": [["print", "EXPR"]],
#     "RETURNST": [["return", "id"], ["return"]],
#     "IFSTMT": [
#         ["if", "(", "EXPR", ")", "{", "STMT", "}", "else", "{", "STMT", "}"],
#         ["if", "(", "EXPR", ")", "{", "STMT", "}"],
#     ],
#     "STMTLIST": [["STMT", "STMTLIST"], ["STMT"]],
#     "EXPR": [
#         ["NUMEXPR", "<", "NUMEXPR"],
#         ["NUMEXPR", "<=", "NUMEXPR"],
#         ["NUMEXPR", ">", "NUMEXPR"],
#         ["NUMEXPR", ">=", "NUMEXPR"],
#         ["NUMEXPR", "==", "NUMEXPR"],
#         ["NUMEXPR", "!=", "NUMEXPR"],
#         ["NUMEXPR"],
#     ],
#     "NUMEXPR": [["NUMEXPR", "+", "TERM"], ["NUMEXPR", "-", "TERM"], ["TERM"]],
#     "TERM": [["TERM", "*", "FACTOR"], ["TERM", "/", "FACTOR"], ["FACTOR"]],
#     "FACTOR": [["num"], ["(", "NUMEXPR", ")"], ["id"]],
# }
import re

token_patterns = [
    (r'\bdef\b', 'DEF'),
    (r'\bint\b', 'INT'),
    (r'\bprint\b', 'PRINT'),
    (r'\breturn\b', 'RETURN'),
    (r'\bif\b', 'IF'),
    (r'\belse\b', 'ELSE'),
    (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),
    (r'\d+', 'NUM'),
    (r'==', 'EQ'),
    (r'=', 'ASSIGN'),
    (r'\+', 'PLUS'),
    (r'-', 'MINUS'),
    (r'\*', 'TIMES'),
    (r'/', 'DIVIDE'),
    (r'<', 'LT'),
    (r'>', 'GT'),
    (r',', 'COMMA'),
    (r';', 'SEMICOLON'),
    (r'\(', 'LPAREN'),
    (r'\)', 'RPAREN'),
    (r'\{', 'LBRACE'),
    (r'\}', 'RBRACE'),
    (r'\s+', None)
]

# Função de tokenização
def lex_analyser(code):
    position = 0
    line = 1
    column = 1
    complete_tokens_list = []
    tokens_list = ['$']
    
    while position < len(code):
        match = None
        for token_pattern in token_patterns:
            pattern, tag = token_pattern
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                text = match.group(0)
                if tag:
                    token = (text, tag, line, column)
                    complete_tokens_list.append(token)
                    if tag == 'ID':
                        tokens_list.append('id')
                    elif tag == 'NUM':
                        tokens_list.append('num')
                    else:
                        tokens_list.append(text)
                break
        if not match:
            raise SyntaxError(f"Caractere não reconhecido na linha {line}, coluna {column}: {code[position]}")
        else:
            newlines = text.count('\n')
            if newlines > 0:
                line += newlines
                column = len(text) - text.rfind('\n')
            else:
                column += len(text)
            position = match.end(0)
    
    return tokens_list

# ------------------------

parse_table = {
    'MAIN': {'def': ['FLIST'], 'int': ['STMT'], 'id': ['STMT'], 'print': ['STMT'], 'return': ['STMT'], 'if': ['STMT'], '{': ['STMT'], ';': ['STMT'], '$': []},
    'FLIST': {'def': ['FDEF', 'FLIST'], '$': []},
    'FDEF': {'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']},
    'PARLIST': {'int': ['int', 'id', 'PARLISTTAIL'], ')': [], '$': []},
    'PARLISTTAIL': {',': [',', 'int', 'id', 'PARLISTTAIL'], ')': []},
    'STMT': {'int': ['int', 'id', ';'], 'id': ['ATRIBST'], 'print': ['PRINTST', ';'], 'return': ['RETURNST', ';'], 'if': ['IFSTMT'], '{': ['{', 'STMTLIST', '}'], ';': [';']},
    'ATRIBST': {'id': ['id', '=', 'EXPR', ';']},
    'FCALL': {'id': ['id', '(', 'PARLISTCALL', ')']},
    'PARLISTCALL': {'id': ['id', 'PARLISTCALLTAIL'], ')': [], '$': []},
    'PARLISTCALLTAIL': {',': [',', 'id', 'PARLISTCALLTAIL'], ')': []},
    'PRINTST': {'print': ['print', 'EXPR']},
    'RETURNST': {'return': ['return', 'EXPR'], ';': ['return', ';']},
    'IFSTMT': {'if': ['if', '(', 'EXPR', ')', 'STMT', 'ELSEPART']},
    'ELSEPART': {'else': ['else', 'STMT'], '': [], '$': []},
    'STMTLIST': {'int': ['STMT', 'STMTLIST'], 'id': ['STMT', 'STMTLIST'], 'print': ['STMT', 'STMTLIST'], 'return': ['STMT', 'STMTLIST'], 'if': ['STMT', 'STMTLIST'], '{': ['STMT', 'STMTLIST'], ';': ['STMT', 'STMTLIST'], '}': [], '$': []},
    'EXPR': {'id': ['NUMEXPR', 'EXPRTAIL'], 'num': ['NUMEXPR', 'EXPRTAIL'], '(': ['NUMEXPR', 'EXPRTAIL'], ';': [';', '}']},
    'EXPRTAIL': {'+': ['+', 'NUMEXPR', 'EXPRTAIL'], '-': ['-', 'NUMEXPR', 'EXPRTAIL'], '==': ['==', 'NUMEXPR', 'EXPRTAIL'], '$': [], ')': [], ';': []},
    'NUMEXPR': {'id': ['TERM', 'NUMEXPRTAIL'], 'num': ['TERM', 'NUMEXPRTAIL'], '(': ['TERM', 'NUMEXPRTAIL']},
    'NUMEXPRTAIL': {'+': ['+', 'TERM', 'NUMEXPRTAIL'], '-': ['-', 'TERM', 'NUMEXPRTAIL'], '$': [], ')': [], ';': [], '==': ['==', 'TERM', 'NUMEXPRTAIL']},
    'TERM': {'id': ['FACTOR', 'TERMTAIL'], 'num': ['FACTOR', 'TERMTAIL'], '(': ['FACTOR', 'TERMTAIL']},
    'TERMTAIL': {'*': ['*', 'FACTOR', 'TERMTAIL'], '$': [], ')': [], ';': [], '+': [], '-': [], '==': []},
    'FACTOR': {'id': ['id'], 'num': ['num'], '(': ['(', 'EXPR', ')']}
}

# Função de análise sintática
def syn_analyser(tokens):
    stack = ['MAIN', '$']
    tokens.append('$')
    index = 0
    
    while stack:
        top = stack.pop()
        current_token = tokens[index]
        
        if top in parse_table:
            if current_token in parse_table[top]:
                production = parse_table[top][current_token]
                if production:
                    stack.extend(reversed(production))
            else:
                print(f"Erro: token inesperado {current_token} na posição {index}. Top: {top} {parse_table[top]}")
                return False
        else:
            if top == current_token:
                index += 1
            else:
                print(f"Erro: esperado {top}, porém encontrado {current_token} na posição {index}")
                return False
    
    if index == len(tokens) - 1:
        return True
    else:
        print("Erro: tokens restantes na entrada")
        return False

# ------------------------

tokens = lex_analyser('''def teste (int a) {
    
    int abc;
}''')

print(f"Tokens: {tokens}")

result = syn_analyser(tokens)

if result:
    print("Is valid")
else:
    print("Is NOT valid")