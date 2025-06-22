# Analisador Léxico e Sintático para Linguagem LSI

Este projeto implementa um analisador léxico (lexer) e sintático (parser) para a linguagem LSI, desenvolvido para a disciplina de Introdução a Compiladores (INE5622) da UFSC.

---

## Integrantes

Gustavo Cortez de Brito (21202331)  
Víctor Douglas Fernandes (21204918)  
João Vitor Duarte Domingos (21203405)  
Manuela Schmitz (20102278)

---

## Requisitos

Este projeto requer Python 3.12 ou superior e o gerenciador de pacotes pip para instalação das dependências.

---

## Configuração do ambiente


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

3. Execução e exemplo prático
```bash
python -m parte3.parser <arquivo.lsi> <modulo_parsing_table>
python -m parte3.parser <arquivo.lsi> <modulo_parsing_table>
```