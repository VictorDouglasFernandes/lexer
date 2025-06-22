import sys
import importlib
from parteB.partB import lexer
from collections import defaultdict

EOF = '$'
sync_tokens = [';', '}', 'def', 'if', 'else', 'return', 'print']

def parse(tokens, parsing_table):
    stack = ['S']
    tokens.append(('$', '$', -1))  # (lexema, tipo, linha)
    index = 0
    had_error = False

    while stack:
        top = stack.pop()
        if index >= len(tokens):
            break

        lexeme, token_type, lineno = tokens[index]

        if top == token_type:
            index += 1
        elif top in parsing_table:
            if token_type in parsing_table[top]:
                production = parsing_table[top][token_type]
                for symbol in reversed(production):
                    if symbol not in ['', 'ε']:
                        stack.append(symbol)
            else:
                print(f"✘ Erro na linha {lineno}: token inesperado '{lexeme}' ({token_type}) em contexto '{top}'")
                had_error = True

                # Modo pânico simples
                while index < len(tokens) and tokens[index][1] not in sync_tokens and tokens[index][0] not in sync_tokens:
                    index += 1
                while stack and (stack[-1] not in parsing_table or token_type not in parsing_table[stack[-1]]):
                    stack.pop()
        elif top == 'ε' or top == '':
            continue
        else:
            print(f"✘ Erro na linha {lineno}: esperado '{top}', mas encontrado '{lexeme}' ({token_type})")
            had_error = True

            while index < len(tokens) and tokens[index][1] not in sync_tokens and tokens[index][0] not in sync_tokens:
                index += 1
            while stack and (stack[-1] not in parsing_table or token_type not in parsing_table[stack[-1]]):
                stack.pop()

    if not had_error and index == len(tokens):
        print("✔ Análise sintática concluída com sucesso.")
        return True
    else:
        print("⚠ Análise concluída com erros.")
        return False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python -m parte3.parser <arquivo.lsi> <modulo_parsing_table>")
        sys.exit(1)

    filename = sys.argv[1]
    parsing_table_module = sys.argv[2]

    # Importa tabela de parsing
    parsing = importlib.import_module(parsing_table_module)
    parsing_table = parsing.parsing_table

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    lexer.input(data)
    tokens = []
    linhas_tokens = defaultdict(list)

    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'ID':
            tipo = 'id'
        elif tok.type == 'NUM':
            tipo = 'num'
        elif tok.type in ['DEF', 'IF', 'ELSE', 'INT', 'RETURN', 'PRINT']:
            tipo = tok.value.lower()
        else:
            tipo = tok.value

        tokens.append((tok.value, tipo, tok.lineno))
        linhas_tokens[tok.lineno].append(f"[{tok.type}: '{tok.value}']")

    print("Tokens por linha:\n")
    for idx, linha in enumerate(data.splitlines(), start=1):
        print(f"Linha {idx}: {linha}")
        if idx in linhas_tokens:
            print("  ➜", ' '.join(linhas_tokens[idx]))
        print()

    print("Tokens para análise sintática:", [t[1] for t in tokens])
    parse(tokens, parsing_table)
