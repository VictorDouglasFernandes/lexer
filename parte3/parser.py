import sys
from parteB.partB import lexer, keywords
from .parsing_table_2 import parsing_table
from .follow_sets import follow_sets

# Marcador de fim de arquivo
EOF = '$'

def is_terminal(symbol):
    """Verifica se um símbolo é terminal (não começa com maiúscula)."""
    return not symbol[0].isupper() if symbol and isinstance(symbol, str) else False

class PredictiveParser:
    """
    Implementa um analisador sintático preditivo table-driven com
    recuperação de erro em modo pânico.
    """
    def __init__(self, token_stream, parsing_table, follow_sets):
        # A lista de tokens no formato: [(tipo, valor, linha), ...]
        self.tokens = token_stream
        self.parsing_table = parsing_table
        self.follow_sets = follow_sets
        self.token_index = 0
        self.error_count = 0
        self.stack = ['$', 'S'] # Inicializa a pilha com o marcador e o símbolo inicial

    def get_current_lookahead(self):
        """Retorna o token atual sem avançar o ponteiro."""
        return self.tokens[self.token_index]

    def advance_input(self):
        """Avança para o próximo token."""
        if self.token_index < len(self.tokens) - 1:
            self.token_index += 1

    def handle_error(self):
        """
        Implementa a recuperação de erro em Modo Pânico.
        Esta função é chamada quando um erro de sintaxe é detectado.
        """
        self.error_count += 1
        lookahead_type, lookahead_value, lookahead_line = self.get_current_lookahead()
        
        # 1. Relata o erro com clareza
        print(f"Erro Sintático na Linha {lookahead_line}: Token inesperado '{lookahead_value}'")

        # 2. Sincroniza a pilha e a entrada
        top = self.stack[-1]
        
        # Descarta tokens da entrada até encontrar um que seja um ponto de sincronização seguro.
        # Um ponto seguro é um token que pode seguir o não-terminal no topo da pilha.
        sync_tokens = self.follow_sets.get(top, set())
        if not sync_tokens: # Se não houver follow set, a recuperação é mais difícil
            self.advance_input()
            return

        print(f"   Contexto: Esperando um token do conjunto FOLLOW de '{top}': {sync_tokens}")
        while lookahead_type not in sync_tokens:
            if lookahead_type == '$': # Nunca descarte o fim do arquivo
                return
            self.advance_input()
            lookahead_type, _, _ = self.get_current_lookahead()
            
        # Se o símbolo que causou o erro foi um não-terminal, ele é removido da pilha
        # para que o parser possa continuar a partir do token de sincronização.
        if top[0].isupper():
            self.stack.pop()
        
        print(f"   Recuperação: Parser resincronizado no token '{self.get_current_lookahead()[1]}'")

    def parse(self):
        """
        Executa o algoritmo de análise sintática preditiva.
        """
        while self.stack:
            top = self.stack[-1]
            lookahead_type, _, _ = self.get_current_lookahead()

            if top == '$' and lookahead_type == '$':
                break # Análise bem-sucedida

            if top == lookahead_type:
                self.stack.pop()
                self.advance_input()
            elif is_terminal(top):
                # Erro: Terminal na pilha não corresponde ao de entrada
                self.handle_error()
                self.stack.pop() # Remove o terminal esperado para destravar
            elif lookahead_type in self.parsing_table.get(top, {}):
                # Expande a produção
                self.stack.pop()
                production = self.parsing_table[top][lookahead_type]
                if production: # Se a produção não for para epsilon '[]'
                    for symbol in reversed(production):
                        self.stack.append(symbol)
            else:
                # Erro: Célula vazia na tabela
                self.handle_error()
                # Não removemos o não-terminal aqui, pois o handle_error já faz isso.
        
        # Relatório Final
        if self.error_count == 0:
            print("\n✔ Análise sintática concluída com sucesso.")
            return True
        else:
            print(f"\n✘ Análise concluída com {self.error_count} erro(s) sintático(s).")
            return False

# --- Bloco de Execução Principal ---
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Uso: python3 seu_parser.py <arquivo.lsi>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = file.read()
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")
        sys.exit(1)

    # 1. Executa o léxico UMA VEZ para obter a lista de tokens
    lexer.input(data)
    tokens_from_lexer = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        
        # Converte o token do PLY para o formato esperado pela tabela
        token_type = ''
        if tok.type in keywords.values():
            token_type = tok.value.lower()
        elif tok.type == 'ID':
            token_type = 'id'
        elif tok.type == 'NUM':
            token_type = 'num'
        else: # Para operadores e símbolos
            token_type = tok.value
            
        tokens_from_lexer.append((token_type, tok.value, tok.lineno))
    
    # Adiciona o marcador de fim de arquivo
    tokens_from_lexer.append(('$', '$', lexer.lineno))

    # 2. Inicia a análise sintática
    print(f"--- Iniciando Análise Sintática para o arquivo: {filename} ---")
    parser = PredictiveParser(tokens_from_lexer, parsing_table, follow_sets)
    parser.parse()