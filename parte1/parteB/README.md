# Lexer - Parte B

Este projeto implementa um analisador léxico (lexer), desenvolvido para a primeira parte do trabalho da disciplina de Introdução a Compiladores (INE5622) da UFSC.
Este documento explica como instalar dependências e executar o analisador léxico da Parte B usando os dois exemplos fornecidos.

## Pré‑requisitos

- Python 3.12 ou superior (`python3 --version`)  
- `pip` (`pip --version`)

## Instalação

1. Clonando projeto e criando ambiente virtual
```bash
git clone https://github.com/VictorDouglasFernandes/lexer.git
cd lexer
pyenv virtualenv 3.12.3 venv
pyenv activate venv
```

2. Instalando dependências
```bash
pip install -r requirements.txt
```

## Execução

1. Acessa a pasta do projeto:
   ```bash
   cd parte1/parteB/
   ```
2. Para rodar com o exemplo **correto**:
   ```bash
   python3 lexer.py resources/example_correct.lsi
   ```
3. Para rodar com o exemplo **com erro**:
   ```bash
   python3 lexer.py resources/example_error.lsi
   ```

## Saída Esperada

- **example_correct.lsi**  
  Impressão de uma lista de tokens, por exemplo:
  ```
  ['def','id','(','id',')','{', … ]
  ```
- **example_error.lsi**  
  Mensagem de erro léxico indicando linha e coluna do caractere inválido.