# base_back_python - README

### Montar projeto local


Instalar requirements.txt
```
pip install -r requirements.txt
```

Projeto backend

```bash
git clone https://github.com/JansenDF/base_back_python.git
cd base_back_python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
export FLASK_APP=manage.py
flask run
```

### Testes

```bash
flask test
```

## Banco de Dados

### Executar os comandos ao modificar ou incluir modelos
``` bash
flask db init  # so quando iniciar o banco
flask db migrate --message 'migration'
flask db upgrade
```

## Docker

### Remoto
``` bash

```

### Local


``` bash

```

Antes do commit executar:

```
flake8 ./manage.py 
flake8 ./base_back_python
flake8 ./tests/

bandit --skip B104 --verbose --recursive ./base_back_python
bandit --skip B104 --verbose --recursive ./tests
bandit --skip B104 --verbose --recursive ./manage.py
