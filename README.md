# api-flask-clientes

---

API desenvolvida para a prova do programa Trainee Smart NX 2021.

### 🎯 Endpoints:

Para buscar todos os clientes:

**GET** /cliente

Para buscar um cliente específico:

**GET** /cliente/{codigo_cliente}

Para adicionar um cliente:

**POST** /cliente?nome={nome_cliente}&razao_social={razao_cliente}&cnpj={cnpj_cliente}

Para atualizar um cliente:

**PATCH** /cliente/{codigo_cliente}?nome={nome_cliente}&razao_social={razao_cliente}&cnpj={cnpj_cliente}

Para deletar um cliente:

**DEL** /cliente/{codigo_cliente}

---

### 👨🏾‍🏫 Para rodar o projeto:

Abra um terminal e instale o virtualenv com o comando:

pip install virtualenv

Inicie um ambiente virtual na pasta do projeto:

virtualenv nome_do_ambiente

Ative o ambiente virtual:

.\nome_do_ambiente\Scripts\activate

Instale os requerimentos:

pip install -r requirements.txt

Após a intalação podemos rodar a api:

python app.py

---

### ⚙️ requirements

aniso8601==8.1.1

click==7.1.2

Flask==1.1.2

Flask-Cors==3.0.10

Flask-RESTful==0.3.8

Flask-SQLAlchemy==2.4.4

itsdangerous==1.1.0

Jinja2==2.11.2

MarkupSafe==1.1.1

psycopg2==2.8.6

pytz==2020.5

six==1.15.0

SQLAlchemy==1.3.22

Werkzeug==1.0.1