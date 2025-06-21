parsing_table = {
    'S': {
        'def': ['MAIN', '$'], 'id': ['MAIN', '$'], '(': ['MAIN', '$'], '{': ['MAIN', '$'],
        'int': ['MAIN', '$'], ';': ['MAIN', '$'], 'print': ['MAIN', '$'], 'return': ['MAIN', '$'],
        'if': ['MAIN', '$'], '$': ['MAIN', '$']
    },
    'MAIN': {
        'def': ['FLIST'], 'id': ['STMT'], 'int': ['STMT'], '(': ['STMT'], '{': ['STMT'],
        ';': ['STMT'], 'print': ['PRINTST', ';'], 'return': ['RETURNST', ';'], 'if': ['IFSTMT'], '$': []
    },
    'FLIST': {
        'def': ['FDEF', "FLIST'"]
    },
    "FLIST'": {
        'def': ['FDEF', "FLIST'"], 'id': [], '$': []
    },
    'FDEF': {
        'def': ['def', 'id', '(', 'PARLIST', ')', '{', 'STMTLIST', '}']
    },
    'PARLIST': {
        'int': ['int', 'id', "PARLIST'"], ')': []
    },
    "PARLIST'": {
        ',': [',', 'PARLIST'], ')': []
    },
    'STMT': {
        'id': ['ATRIBST', ';'], '{': ['{', 'STMTLIST', '}'], 'int': ['int', 'VARLIST', ';'],
        ';': [';'], 'print': ['PRINTST', ';'], 'return': ['RETURNST', ';'], 'if': ['IFSTMT']
    },
    'VARLIST': {
        'id': ['id', "VARLIST'"]
    },
    "VARLIST'": {
        ',': [',', 'VARLIST'], ';': []
    },
    'ATRIBST': {
        'id': ['id', '=', "ATRIBST'"]
    },
    "ATRIBST'": {
        'id': ['id', 'ATRIBST_ID_SUFFIX'], '(': ['(', 'NUMEXPR', ')', "TERM'", "NUMEXPR'", "EXPR'"],
        'num': ['num', "TERM'", "NUMEXPR'", "EXPR'"]
    },
    'ATRIBST_ID_SUFFIX': {
        '(': ['(', 'PARLISTCALL', ')'],
        '+': ["TERM'", "NUMEXPR'", "EXPR'"], '-': ["TERM'", "NUMEXPR'", "EXPR'"],
        '*': ["TERM'", "NUMEXPR'", "EXPR'"], '/': ["TERM'", "NUMEXPR'", "EXPR'"],
        '<': ["TERM'", "NUMEXPR'", "EXPR'"], '<=': ["TERM'", "NUMEXPR'", "EXPR'"],
        '>': ["TERM'", "NUMEXPR'", "EXPR'"], '>=': ["TERM'", "NUMEXPR'", "EXPR'"],
        '==': ["TERM'", "NUMEXPR'", "EXPR'"], '!=': ["TERM'", "NUMEXPR'", "EXPR'"]
    },
    'PARLISTCALL': {
        'id': ['id', "PARLISTCALL'"], ')': []
    },
    "PARLISTCALL'": {
        'id': ['id', "PARLISTCALL'"], ')': []
    },
    'PRINTST': {
        'print': ['print', 'EXPR']
    },
    'RETURNST': {
        'return': ['return', "RETURNST'"]
    },
    "RETURNST'": {
        'id': ['id'], ';': []
    },
    'IFSTMT': {
        'if': ['if', '(', 'EXPR', ')', '{', 'STMT', '}', "IFSTMT'"]
    },
    "IFSTMT'": {
        'else': ['else', '{', 'STMT', '}'], '$': [], ';': [], '}': []
    },
    'STMTLIST': {
        'id': ['STMT', "STMTLIST'"], 'int': ['STMT', "STMTLIST'"], '{': ['STMT', "STMTLIST'"],
        ';': ['STMT', "STMTLIST'"], 'print': ['STMT', "STMTLIST'"], 'return': ['STMT', "STMTLIST'"],
        'if': ['STMT', "STMTLIST'"]
    },
    "STMTLIST'": {
        'id': ['STMT', "STMTLIST'"], 'int': ['STMT', "STMTLIST'"], '{': ['STMT', "STMTLIST'"],
        ';': ['STMT', "STMTLIST'"], 'print': ['STMT', "STMTLIST'"], 'return': ['STMT', "STMTLIST'"],
        'if': ['STMT', "STMTLIST'"], '}': []
    },
    'EXPR': {
        'id': ['NUMEXPR', "EXPR'"], '(': ['NUMEXPR', "EXPR'"], 'num': ['NUMEXPR', "EXPR'"]
    },
    "EXPR'": {
        '<': ['<', 'NUMEXPR'], '<=': ['<=', 'NUMEXPR'], '>': ['>', 'NUMEXPR'], '>=': ['>=', 'NUMEXPR'],
        '==': ['==', 'NUMEXPR'], '!=': ['!=', 'NUMEXPR'], ')': []
    },
    'NUMEXPR': {
        'id': ['TERM', "NUMEXPR'"], '(': ['TERM', "NUMEXPR'"], 'num': ['TERM', "NUMEXPR'"]
    },
    "NUMEXPR'": {
        '+': ['+', 'TERM', "NUMEXPR'"], '-': ['-', 'TERM', "NUMEXPR'"],
        '<': [], '<=': [], '>': [], '>=': [], '==': [], '!=': [], ')': []
    },
    'TERM': {
        'id': ['FACTOR', "TERM'"], '(': ['FACTOR', "TERM'"], 'num': ['FACTOR', "TERM'"]
    },
    "TERM'": {
        '*': ['*', 'FACTOR', "TERM'"], '/': ['/', 'FACTOR', "TERM'"],
        '+': [], '-': [], '<': [], '<=': [], '>': [], '>=': [], '==': [], '!=': [], ')': []
    },
    'FACTOR': {
        'id': ['id'], '(': ['(', 'NUMEXPR', ')'], 'num': ['num']
    }
}
