# 🚀 PolyGlot Data Orchestrator

> Ferramenta de infraestrutura e automação desenvolvida para gerenciar múltiplos paradigmas de bancos de dados de forma containerizada.

## 🛠️ Sobre o Projeto
O **PolyGlot Data Orchestrator** é um projeto focado em **DevOps e Engenharia de Dados**, projetado para subir e validar simultaneamente um ambiente híbrido de bancos de dados:
- **MySQL (Relacional / SQL)**
- **MongoDB (Não Relacional / NoSQL)**

A aplicação utiliza **Docker Compose** para orquestração de containers com volumes persistentes de dados e um script de automação em **Python** para realizar auditorias de saúde (*health checks*) em tempo real.

---

## ⚙️ Tecnologias Utilizadas
* **Docker & Docker Compose** (Orquestração e persistência de dados)
* **Python 3** (Automação e testes de conexão)
* **MySQL 8.0 & MongoDB** (Motores de banco de dados)

---

## 🚀 Como Executar o Projeto

Certifique-se de ter o **Docker** e o **Python** instalados na sua máquina.

### 1. Clonar o repositório
```bash
git clone [https://github.com/Pedro-H-Dev/polyglot-data-orchestrator.git](https://github.com/Pedro-H-Dev/polyglot-data-orchestrator.git)
cd polyglot-data-orchestrator
```
### 2 Subir os containers de banco de dados
```bash 
docker compose up -d
```
### 3. Instalar as dependências do Python
```Bash

pip install -r requirements.txt
```
### 4. Executar a auditoria de conexão
```Bash
python main.py
````

### Feito com 💻 por Pedro H.
