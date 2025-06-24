import sys
import importlib
from parte1.parteB.lexer import lexer
from collections import defaultdict

EOF = '$'
sync_tokens = [';', '}', 'def', 'if', 'else', 'return', 'print']

def parse(tokens, parsing_table, linhas_arquivo, tokens_por_linha):
    stack = ['S']
    tokens.append(('$', '$', -1))  # (lexema, tipo, linha)
    index = 0
    had_error = False

    while stack:
        top = stack.pop()
        if index >= len(tokens):
            break

        lexeme, token_type, lineno = tokens[index]
        prev_lineno = tokens[index - 1][2] if index > 0 else lineno

        if top == token_type:
            index += 1
        elif top in parsing_table:
            if token_type in parsing_table[top]:
                production = parsing_table[top][token_type]
                for symbol in reversed(production):
                    if symbol not in ['', 'ε']:
                        stack.append(symbol)
            else:
                had_error = True
                if top in ["TERM'", "NUMEXPR'", "EXPR'", 'ATRIBST_ID_SUFFIX']:
                    if token_type in ['num', 'id', '(', ')']:
                        print(
                            f"\n✘ Erro na linha {prev_lineno}: operador ou separador esperado antes de '{lexeme}' ({token_type})")
                    elif token_type == ';':
                        print(f"\n✘ Erro na linha {prev_lineno}: expressão incompleta antes de ';'")
                    elif token_type == ')':
                        print(f"\n✘ Erro na linha {prev_lineno}: parêntese de fechamento inesperado")
                    elif token_type == '}':
                        print(f"\n✘ Erro na linha {prev_lineno}: chave de fechamento inesperada")
                    else:
                        print(f"\n✘ Erro na linha {prev_lineno}: erro de expressão próximo a '{lexeme}' ({token_type})")

                    print(f"Linha {prev_lineno}: {linhas_arquivo[prev_lineno - 1].strip()}")
                    print("  ➜", ' '.join(tokens_por_linha[prev_lineno]))
                else:
                    print(f"\n✘ Erro na linha {lineno}: token inesperado '{lexeme}' ({token_type}) em contexto '{top}'")
                    print(f"Linha {lineno}: {linhas_arquivo[lineno - 1].strip()}")
                    print("  ➜", ' '.join(tokens_por_linha[lineno]))

                # Modo pânico simples
                while index < len(tokens) and tokens[index][1] not in sync_tokens and tokens[index][0] not in sync_tokens:
                    index += 1
                while stack and (stack[-1] not in parsing_table or token_type not in parsing_table[stack[-1]]):
                    stack.pop()
        elif top == 'ε' or top == '':
            continue
        else:
            print(f"\n✘ Erro na linha {lineno}: esperado '{top}', mas encontrado '{lexeme}' ({token_type})")
            print(f"Linha {lineno}: {linhas_arquivo[lineno - 1].strip()}")
            print("  ➜", ' '.join(tokens_por_linha[lineno]))
            had_error = True

            while index < len(tokens) and tokens[index][1] not in sync_tokens and tokens[index][0] not in sync_tokens:
                index += 1
            while stack and (stack[-1] not in parsing_table or token_type not in parsing_table[stack[-1]]):
                stack.pop()

    if not had_error and index == len(tokens):
        print("\n✔ Análise sintática concluída com sucesso.")
        return True
    else:
        print("\n⚠ Análise concluída com erros.")
        return False


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Uso: python -m parte3.parser <arquivo.lsi> <modulo_parsing_table>")
        sys.exit(1)

    filename = sys.argv[1]
    parsing_table_module = sys.argv[2]

    parsing = importlib.import_module(parsing_table_module)
    parsing_table = parsing.parsing_table

    with open(filename, 'r', encoding='utf-8') as file:
        linhas_arquivo = file.readlines()

    lexer.input(''.join(linhas_arquivo))
    tokens = []
    tokens_por_linha = defaultdict(list)

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
        tokens_por_linha[tok.lineno].append(f"[{tok.type}: '{tok.value}']")

    print("Tokens para análise sintática:", [t[1] for t in tokens])
    parse(tokens, parsing_table, linhas_arquivo, tokens_por_linha)
