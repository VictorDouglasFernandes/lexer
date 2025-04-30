# Parte B – Lexer com PLY

## Requisitos
- Python 3.12.3
- PLY

## Instalação
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install ply
```

## Execução
```bash
chmod +x partB.py
./partB.py example_correct.lsi   # imprime lista de tokens
./partB.py example_error.lsi     # imprime erros léxicos
```