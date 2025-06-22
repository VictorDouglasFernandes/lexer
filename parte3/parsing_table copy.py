# Tabela de Análise Preditiva para a gramática LSI-2025-1 (LL-1)
# Derivada do trabalho da Parte 2.
# As chaves (terminais) devem corresponder exatamente aos tokens gerados pelo seu léxico.

parsing_table = {
    'MAIN': {
        'def': ['FLIST'],
        'int': ['STMT'],
        'id': ['STMT'],
        '{': ['STMT'],
        ';': ['STMT'],
        'print': ['STMT'],
        'return': ['STMT'],
        'if': ['STMT'],
        '$': []  # MAIN -> ε
    },
    'FLIST': {
        'def': ['FDEF', "FLIST'"]
    },
    "FLIST'": {
        'def': ['FDEF', "FLIST'"],
        '$': []  # FLIST' -> ε
    },
    'FDEF': {
        'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']
    },
    'PARLIST': {
        'int': ['int', 'id', "PARLIST'"],
        ')': []  # PARLIST -> ε
    },
    "PARLIST'": {
        ',': [',', 'PARLIST'],
        ')': []  # PARLIST' -> ε
    },
    'STMT': {
        'int': ['int', 'VARLIST', ';'],
        'id': ['ATRIBST', ';'],
        'print': ['PRINTST', ';'],
        'return': ['RETURNST', ';'],
        'if': ['IFSTMT'],
        '{': ['{', 'STMTLIST', '}'],
        ';': [';']
    },
    'VARLIST': {
        'id': ['id', "VARLIST'"]
    },
    "VARLIST'": {
        ',': [',', 'VARLIST'],
        ';': []  # VARLIST' -> ε
    },
    'ATRIBST': {
        # O PDF de vocês usa ':=', mas a gramática original usa '='.
        # Use o token que seu léxico realmente gera. Vou usar '='.
        'id': ['id', '=', "ATRIBST'"]
    },
    "ATRIBST'": {
        'num': ['num', "TERM'", "NUMEXPR'", "EXPR'"],
        '(': ['(', 'NUMEXPR', ')', "TERM'", "NUMEXPR'", "EXPR'"],
        'id': ['id', 'ATRIBST_ID_SUFFIX']
    },
    'ATRIBST_ID_SUFFIX': {
        '(': ['(', 'PARLISTCALL', ')'],
        # Esta é a regra para quando ATRIBST_ID_SUFFIX -> EXPR (sem FCALL)
        # Ela é escolhida com base no FOLLOW set.
        '*': ["TERM'", "NUMEXPR'", "EXPR'"],
        '/': ["TERM'", "NUMEXPR'", "EXPR'"],
        '+': ["TERM'", "NUMEXPR'", "EXPR'"],
        '-': ["TERM'", "NUMEXPR'", "EXPR'"],
        '<': ["TERM'", "NUMEXPR'", "EXPR'"],
        '<=': ["TERM'", "NUMEXPR'", "EXPR'"],
        '>': ["TERM'", "NUMEXPR'", "EXPR'"],
        '>=': ["TERM'", "NUMEXPR'", "EXPR'"],
        '==': ["TERM'", "NUMEXPR'", "EXPR'"],
        '!=': ["TERM'", "NUMEXPR'", "EXPR'"],
        ';': ["TERM'", "NUMEXPR'", "EXPR'"]
    },
    'PARLISTCALL': {
        'id': ['id', "PARLISTCALL'"],
        ')': []  # PARLISTCALL -> ε
    },
    "PARLISTCALL'": {
        ',': [',', 'id', "PARLISTCALL'"],
        ')': []  # PARLISTCALL' -> ε
    },
    'PRINTST': {
        'print': ['print', 'EXPR']
    },
    'RETURNST': {
        'return': ['return', "RETURNST'"]
    },
    "RETURNST'": {
        'id': ['id'],
        ';': []  # RETURNST' -> ε
    },
    'IFSTMT': {
        'if': ['if', '(', 'EXPR', ')', '{', 'STMT', '}', "IFSTMT'"]
    },
    "IFSTMT'": {
        'else': ['else', '{', 'STMT', '}'],
        # IFSTMT' -> ε, baseado no FOLLOW set de IFSTMT
        'def': [], 'int': [], 'id': [], '{': [], ';': [],
        'print': [], 'return': [], 'if': [], '}': [], '$': []
    },
    'STMTLIST': {
        'int': ['STMT', "STMTLIST'"],
        'id': ['STMT', "STMTLIST'"],
        'print': ['STMT', "STMTLIST'"],
        'return': ['STMT', "STMTLIST'"],
        'if': ['STMT', "STMTLIST'"],
        '{': ['STMT', "STMTLIST'"],
        ';': ['STMT', "STMTLIST'"],
        '}': [] # STMTLIST -> ε
    },
    "STMTLIST'": {
        'int': ['STMT', "STMTLIST'"],
        'id': ['STMT', "STMTLIST'"],
        'print': ['STMT', "STMTLIST'"],
        'return': ['STMT', "STMTLIST'"],
        'if': ['STMT', "STMTLIST'"],
        '{': ['STMT', "STMTLIST'"],
        ';': ['STMT', "STMTLIST'"],
        '}': []  # STMTLIST' -> ε
    },
    'EXPR': {
        'num': ['NUMEXPR', "EXPR'"],
        '(': ['NUMEXPR', "EXPR'"],
        'id': ['NUMEXPR', "EXPR'"]
    },
    "EXPR'": {
        '<': ['<', 'NUMEXPR'],
        '<=': ['<=', 'NUMEXPR'],
        '>': ['>', 'NUMEXPR'],
        '>=': ['>=', 'NUMEXPR'],
        '==': ['==', 'NUMEXPR'],
        '!=': ['!=', 'NUMEXPR'],
        # EXPR' -> ε, baseado no FOLLOW set de EXPR
        ';': [],
        ')': []
    },
    'NUMEXPR': {
        'num': ['TERM', "NUMEXPR'"],
        '(': ['TERM', "NUMEXPR'"],
        'id': ['TERM', "NUMEXPR'"]
    },
    "NUMEXPR'": {
        '+': ['+', 'TERM', "NUMEXPR'"],
        '-': ['-', 'TERM', "NUMEXPR'"],
        # NUMEXPR' -> ε, baseado no FOLLOW set de NUMEXPR
        '<': [], '<=': [], '>': [], '>=': [], '==': [], '!=': [],
        ';': [], ')': []
    },
    'TERM': {
        'num': ['FACTOR', "TERM'"],
        '(': ['FACTOR', "TERM'"],
        'id': ['FACTOR', "TERM'"]
    },
    "TERM'": {
        '*': ['*', 'FACTOR', "TERM'"],
        '/': ['/', 'FACTOR', "TERM'"],
        # TERM' -> ε, baseado no FOLLOW set de TERM
        '+': [], '-': [], '<': [], '<=': [], '>': [], '>=': [],
        '==': [], '!=': [], ';': [], ')': []
    },
    'FACTOR': {
        'num': ['num'],
        '(': ['(', 'NUMEXPR', ')'],
        'id': ['id']
    }
}