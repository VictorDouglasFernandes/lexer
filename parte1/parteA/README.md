# Lexer - Parte A

Este projeto implementa um analisador léxico simples (lexer), desenvolvido para a primeira parte do trabalho da disciplina de Introdução a Compiladores (INE5622) da UFSC.
Este documento explica como instalar dependências e executar o analisador léxico da Parte A usando os dois exemplos fornecidos.

## Pré‑requisitos

- Python 3.12 ou superior (`python3 --version`);

## Instalação

1. Clonando projeto e criando ambiente virtual
```bash
git clone https://github.com/VictorDouglasFernandes/lexer.git
cd lexer
pyenv virtualenv 3.12.3 venv
pyenv activate venv
```

## Execução

1. Acesse pelo terminal diretamente ou de sua IDE a pasta do projeto:
   ```bash
   cd parte1/parteA/
   ```

2. Para testar com input errado onde o analisador não consegue reconhecer um token dentro do arquivo:
   ```bash
   python3 simple_lexer.py resources/wrong_input.pokemon
   ```

3. Para testar com input correto onde o analisador consegue reconhecer todos os token dentro do arquivo:
   ```bash
   python3 simple_lexer.py resources/input.pokemon
   ```

## Saída esperada

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
