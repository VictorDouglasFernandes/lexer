"""
Analisador Léxico Parte A
Integrantes: 
- Gustavo Cortez de brito (21202331)
- Víctor Douglas Fernandes (21204918)
- João Vitor Duarte Domingos (21203405)
- Manuela Schmitz (20102278)
"""

import sys

numbers = ['0','1','2','3','4','5','6','7','8','9']
chars = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','x','z',
'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','Y','X','Z']
firstOperators = ['>','<','=','>','<','!']
secondOperators = ['=']

def relationalOperator(char: str, current: str) -> bool:
    if len(current) >= 2:
        return False
    if len(current) == 1:
        if current in ['>','<','!'] and char in secondOperators:
            return True
        return False

    return char in firstOperators

if len(sys.argv) < 2:
    print("You should specify the file name")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r') as file:
    code = file.read()

for line in code.split('\n'):
    remaining = line
    while len(remaining) > 0:
        
        if remaining[0] == ' ':
            index = remaining.find(' ')
            remaining = remaining[:index] + remaining[index + len(' '):]
            continue
        
        variable = ''
        number = ''
        operator = ''
        
        stopVariable = False
        stopNumber = False
        stopOperator = False
        
        for char in remaining:
            hasMatch = False
            if (not stopNumber and char in numbers):
                number += char
                hasMatch = True
            else:
                stopNumber = True
            
            if (not stopVariable and ((variable == '' and char in chars) or (len(variable) > 0 and (char in chars or char in numbers)))):
                variable += char
                hasMatch = True
            else:
                stopVariable = True

            if (not stopOperator and relationalOperator(char, operator)):
                operator += char
                hasMatch = True
            else:
                stopOperator = True
            
            if not hasMatch:
                break
        
        if len(variable) > len(number) and len(variable) > len(operator):
            
            print(f'token={variable} type=var')
            index = remaining.find(variable)
            remaining = remaining[:index] + remaining[index + len(variable):]
        elif len(number) > len(variable) and len(number) > len(operator):
            
            print(f'token={number} type=int')
            index = remaining.find(number)
            remaining = remaining[:index] + remaining[index + len(number):]
        elif len(operator) > len(variable) and len(operator) > len(variable):

            print(f'token={operator} type=operator')
            index = remaining.find(operator)
            remaining = remaining[:index] + remaining[index + len(operator):]
        else:
            # No match
            print(f'no match: {remaining}')
            break
        
        # if len(remaining) > 0:
            # print(f'remaining: {remaining}')
