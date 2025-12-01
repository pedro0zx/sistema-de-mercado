<div align="center">

# 🛒 Sistema de Mercado  
### CRUD Completo de Produtos  
**Django REST Framework + React + PostgreSQL + Docker**

<img src="https://img.shields.io/badge/Django-4.2-green?style=for-the-badge&logo=django">
<img src="https://img.shields.io/badge/React-18-blue?style=for-the-badge&logo=react">
<img src="https://img.shields.io/badge/PostgreSQL-14-blue?style=for-the-badge&logo=postgresql">
<img src="https://img.shields.io/badge/Docker-Compose-2496ED?style=for-the-badge&logo=docker">

</div>

# 📘 Sobre o Projeto

Este projeto consiste em um sistema de gestão de produtos (CRUD) utilizando:

- **Backend:** Django + Django REST Framework  
- **Frontend:** React  
- **Banco:** PostgreSQL  
- **Conteinerização:** Docker + docker-compose  

O sistema permite:

✔ Cadastrar produtos  
✔ Listar produtos  
✔ Editar produtos  
✔ Excluir produtos  
✔ Persistência com banco relacional  
✔ Comunicação via API REST  

---

# 🗂 Estrutura do Projeto

mercado-projeto/
│
├── backend/
│ ├── Dockerfile
│ ├── requirements.txt
│ ├── manage.py
│ ├── mercado_backend/
│ └── produtos/
│
├── frontend/
│ ├── Dockerfile
│ ├── package.json
│ └── src/
│
└── docker-compose.yml

---

# 🚀 Como Rodar o Projeto

## 🐳 **1. Executar com Docker (RECOMENDADO)**

### ▶️ Subir tudo:
```bash
docker-compose up --build

| Serviço                  | Porta | URL                                                                      |
| ------------------------ | ----- | ------------------------------------------------------------------------ |
| **Frontend (React)**     | 3000  | [http://localhost:3000](http://localhost:3000)                           |
| **Backend (API Django)** | 8000  | [http://localhost:8000/api/produtos](http://localhost:8000/api/produtos) |
| **PostgreSQL**           | 5432  | (usado internamente pelo backend)                                        |

cd backend
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
API:
➡ http://localhost:8000/api/produtos/

    #📌 Frontend (React)
cd frontend
npm install
npm start
App:
➡ http://localhost:3000/

🛠 Tecnologias Utilizadas
Backend

Python 3.10

Django

Django REST Framework

django-cors-headers

PostgreSQL

Frontend

React

Axios

Infraestrutura

Docker

    ##🧱 API Endpoints
docker-compose

| Método | Rota                  | Descrição               |
| ------ | --------------------- | ----------------------- |
| GET    | `/api/produtos/`      | Lista todos os produtos |
| POST   | `/api/produtos/`      | Cria um produto         |
| PUT    | `/api/produtos/{id}/` | Atualiza um produto     |
| DELETE | `/api/produtos/{id}/` | Remove um produto       |

##🎨 Interface do Usuário (Frontend)

✔ Formulário de cadastro
✔ Listagem dinâmica
✔ Botões de Editar / Excluir
✔ Atualização automática após ações
✔ Comunicação via Axios com Django REST

🐳 Arquitetura Docker

O arquivo docker-compose.yml cria três containers:

Serviço	Descrição
db	PostgreSQL
backend	Django API
frontend	React App
