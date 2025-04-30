# Lexer - Parte B

Este documento explica como instalar dependências e executar o analisador léxico da Parte B usando os dois exemplos fornecidos em um ambiente Linux.

## Pré‑requisitos

- Python 3.x (`python3 --version`)  
- `pip` (`pip --version`)

## Instalação

1. Abra o terminal na pasta raiz `lexer` (onde estão `parteA` e `parteB`):  
   ```bash
   cd /caminho/para/lexer
   ```
2. Instale o PLY (use `pip install -r requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

## Execução

1. Entre na pasta da Parte B:
   ```bash
   cd parteB
   ```
2. Para rodar com o exemplo **correto**:
   ```bash
   python3 partB.py example_correct.lsi
   ```
3. Para rodar com o exemplo **com erro**:
   ```bash
   python3 partB.py example_error.lsi
   ```

## Saída Esperada

- **example_correct.lsi**  
  Impressão de uma lista de tokens, por exemplo:
  ```
  ['def','id','(','id',')','{', … ]
  ```
- **example_error.lsi**  
  Mensagem de erro léxico indicando linha e coluna do caractere inválido.