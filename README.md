# 📦 API de E-commerce com Flask

Esta é uma API de e-commerce desenvolvida em **Python** utilizando o framework **Flask**, criada com objetivo de aprendizado e prototipagem. O projeto inclui funcionalidades essenciais para um sistema de compras online, permitindo a manipulação de produtos, carrinho de compras e autenticação de usuários.

## 🚀 Funcionalidades

### Autenticação

- Registro de usuários (signup)
- Login e logout usando **JWT**
- Proteção de endpoints via JWT (`@jwt_required()`)

### CRUD de Produtos

- Criar, listar, visualizar, atualizar e deletar produtos
- Documentação automática dos endpoints via **Flask-RESTX** (`/docs`)

### Carrinho de Compras

- Adicionar itens ao carrinho
- Remover itens do carrinho
- Visualizar os itens do carrinho
- Finalizar compra (checkout)

### Listagem de Produtos

- Visualização de todos os produtos disponíveis
- Visualização individual de um produto específico

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Flask** (Web framework)
- **Flask-RESTX** (API + Swagger Docs)
- **Flask-JWT-Extended** (Autenticação via JWT)
- **Flask-Login** (Gerenciamento de sessão)
- **Flask-CORS** (Permite requisições cross-origin)
- **SQLAlchemy** (ORM para banco de dados)
- **SQLite** (Banco de dados leve para desenvolvimento)

## 📌 Endpoints Principais

### Produtos

| Método | Endpoint              | Descrição                      |
| ------ | --------------------- | ------------------------------ |
| GET    | /api/v1/products/     | Lista todos os produtos        |
| GET    | /api/v1/products/<id> | Retorna detalhes de um produto |
| POST   | /api/v1/products/     | Cria um novo produto           |
| PUT    | /api/v1/products/<id> | Atualiza um produto existente  |
| DELETE | /api/v1/products/<id> | Remove um produto              |

### Carrinho

| Método | Endpoint                         | Descrição                       |
| ------ | -------------------------------- | ------------------------------- |
| GET    | /api/v1/cart/                    | Visualiza o carrinho do usuário |
| POST   | /api/v1/cart/add/<product_id>    | Adiciona um item ao carrinho    |
| DELETE | /api/v1/cart/remove/<product_id> | Remove um item do carrinho      |
| POST   | /api/v1/cart/checkout            | Finaliza a compra               |

### Autenticação

| Método | Endpoint            | Descrição         |
| ------ | ------------------- | ----------------- |
| POST   | /api/v1/auth/login  | Login de usuário  |
| POST   | /api/v1/auth/logout | Logout de usuário |

## 📖 Documentação

A API possui documentação automática via **Swagger**. Acesse:  
http://127.0.0.1:5000/docs


## ⚡ Como Rodar

1. Clonar o repositório

```bash
git clone https://github.com/mariaandrezacs/api_ecommerce.git
```

2. Criar e ativar o ambiente virtual:

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/macOS
```

3. Instalar dependências:

```bash
pip install -r requirements.txt
```

4. Rodar a aplicação:

```bash
python run.py
```
