import sys
from parteB.partB import lexer
from .parsing_table_2 import parsing_table


EOF = '$'

def parse(tokens):
    stack = ['S']
    tokens.append(EOF)
    index = 0

    while stack:
        top = stack.pop()
        current_token = tokens[index] if index < len(tokens) else EOF

        if top == current_token:
            index += 1
        elif top in parsing_table:
            if current_token in parsing_table[top]:
                production = parsing_table[top][current_token]
                for symbol in reversed(production):
                    if symbol != '':
                        stack.append(symbol)
            else:
                print(f"Erro sintático: token inesperado '{current_token}' em contexto '{top}'")
                return False
        elif top == 'ε' or top == '':
            continue
        else:
            print(f"Erro sintático: esperado '{top}', mas encontrado '{current_token}'")
            return False

    if index == len(tokens):
        print("✔ Análise sintática concluída com sucesso.")
        return True
    else:
        print("✘ Erro: tokens restantes após o fim da pilha.")
        return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python parser.py <arquivo.lsi>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()

    lexer.input(data)
    # while True:
    #     tok = lexer.token()
    #     if not tok:
    #         break
    #     print(f'{tok.type}: {tok.value}')
    tokens = []

    while True:
        tok = lexer.token()
        if not tok:
            break

        if tok.type == 'ID':
            tokens.append('id')
        elif tok.type == 'NUM':
            tokens.append('num')
        elif tok.type in ['DEF', 'IF', 'ELSE', 'INT', 'RETURN', 'PRINT']:
            tokens.append(tok.value.lower())
        else:
            tokens.append(tok.value)

    print("Tokens:", tokens)
    parse(tokens)
