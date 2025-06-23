# Tabela de Análise Preditiva para a gramática LSI-2025-1 (LL-1)

parsing_table = {
    'S': {
        'def': ['MAIN', '$'],
        'int': ['MAIN', '$'],
        'id': ['MAIN', '$'],
        '{': ['MAIN', '$'],
        ';': ['MAIN', '$'],
        'print': ['MAIN', '$'],
        'return': ['MAIN', '$'],
        'if': ['MAIN', '$'],
        '$': ['MAIN', '$']
    },
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
        'id': ['id', '=', "ATRIBST'"]
    },
    "ATRIBST'": {
        'num': ['num', "TERM'", "NUMEXPR'", "EXPR'"],
        '(': ['(', 'NUMEXPR', ')', "TERM'", "NUMEXPR'", "EXPR'"],
        'id': ['id', 'ATRIBST_ID_SUFFIX']
    },
    'ATRIBST_ID_SUFFIX': {
        '(': ['(', 'PARLISTCALL', ')'],
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
        'id' : ['id', "PARLISTCALL'"],
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
        'int': [],
        'id': [],
        '{': [],
        ';': [],
        'print': [],
        'return': [],
        'if': [],
        '}': [],
        '$': []
    },
    'STMTLIST': {
        'int': ['STMT', "STMTLIST'"],
        'id': ['STMT', "STMTLIST'"],
        'print': ['STMT', "STMTLIST'"],
        'return': ['STMT', "STMTLIST'"],
        'if': ['STMT', "STMTLIST'"],
        '{': ['STMT', "STMTLIST'"],
        ';': ['STMT', "STMTLIST'"]
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
        '<': [],
        '<=': [],
        '>': [],
        '>=': [],
        '==': [],
        '!=': [],
        ';': [],
        ')': []
    },
    'TERM': {
        'num': ['FACTOR', "TERM'"],
        '(': ['FACTOR', "TERM'"],
        'id': ['FACTOR', "TERM'"]
    },
    "TERM'": {
        '*': ['*', 'FACTOR', "TERM'"],
        '/': ['/', 'FACTOR', "TERM'"],
        '+': [],
        '-': [],
        '<': [],
        '<=': [],
        '>': [],
        '>=': [],
        '==': [],
        '!=': [],
        ';': [],
        ')': []
    },
    'FACTOR': {
        'num': ['num'],
        '(': ['(', 'NUMEXPR', ')'],
        'id': ['id']
    }
}