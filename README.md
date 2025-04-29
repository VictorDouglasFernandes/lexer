# Lexer

## Requerimento

É necessário o python instalado para rodar o programa. Durante desenvolvimento foi utilizado python 3.

## Como rodar

Acesse pelo terminal diretamente ou de sua IDE a pasta do projeto.

Rode `python3 simple_lexer.py wrong_input.pokemon` para testar com input errado onde o analisador não consegue reconhecer um token dentro do arquivo.

Rode `python3 simple_lexer.py input.pokemon` para testar com input correto onde o analisador consegue reconhecer todos os token dentro do arquivo.

## Prints

Os prints seguem o padrão de valor do token em `token=${VALOR_DO_TOKEN}` seguido do tipo `type=${TIPO_DO_TOKEN}`.

O `VALOR_DO_TOKEN` é dinâmico de acordo com o texto do arquivo.

O `TIPO_DO_TOKEN` pode ser:
- `var` para variáveis e nomes de funções que comecem com números e depois números ou letras intercalados (Não aceita `_` já que não é mencionado na descrição).
- `int` para números inteiros.
- `operator` para operadores relacionais já mapeados `>,<,=,>=,<=,!=`.


## Diagrama

Diagrama para variáveis e nomes de funções:

 ![image](https://github.com/user-attachments/assets/1c190502-f8bd-4dfe-b3a9-ddd5db4cd50d)


Diagrama para números inteiros:

![image](https://github.com/user-attachments/assets/b921d8ef-0cf4-452a-9515-80842431b480)


Diagrama para números operadores relacionais:

![image](https://github.com/user-attachments/assets/bb1ca655-360f-4fe4-a402-ae01cb450c06)
