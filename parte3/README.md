# Analisador Sintático para Linguagem LSI - Parte 3

Este projeto implementa um analisador sintático (parser) para a linguagem LSI, desenvolvido para a disciplina de Introdução a Compiladores (INE5622) da UFSC.
Este documento explica como instalar dependências e executar o analisador sintático da Parte3 usando os quatro exemplos fornecidos.

## Pré‑requisitos

- Python 3.12 ou superior (`python3 --version`)  
- `pip` (`pip --version`)

## Instalação

1. Clonando projeto e criando ambiente virtual
```bash
git clone https://github.com/VictorDouglasFernandes/lexer.git
cd lexer
pyenv virtualenv 3.12.3 lexer
pyenv activate lexer
```

2. Instalando dependências
```bash
pip install -r requirements.txt
```

## Execução

1. É preciso estar na pasta raíz do projeto.
2. Para rodar com o exemplo **correto**:
   ```bash
   cd ../
   python3 -m parte3.parser parte3/resources/valido.lsi parte3.parsing_table
   ```
3. Para rodar com os exemplos **com erro**:
   ```bash
   cd ../
   python3 -m parte3.parser parte3/resources/erro_chave.lsi parte3.parsing_table
   python3 -m parte3.parser parte3/resources/erro_ponto_virgula.lsi parte3.parsing_table
   python3 -m parte3.parser parte3/resources/erro_relop.lsi parte3.parsing_table
   ```
