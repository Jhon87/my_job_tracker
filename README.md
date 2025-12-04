# My Job Tracker 🚀

Sistema web desenvolvido em **Python** e **Django** para organização pessoal de candidaturas a vagas de emprego. O projeto permite o gerenciamento completo (CRUD) do status de processos seletivos.

## 📸 Funcionalidades
- **Cadastro de Vagas:** Registro de empresa, cargo, localização e anotações.
- **Gestão de Status:** Acompanhamento visual (Enviado, Entrevista, Aprovado, etc).
- **CRUD Completo:** Criação, Leitura, Edição e Exclusão de registros.
- **Interface Responsiva:** Estilização limpa utilizando **Bootstrap 5**.

## 🛠 Tecnologias Utilizadas
- **Back-end:** Python 3, Django 5
- **Front-end:** HTML5, Bootstrap 5 (CDN)
- **Banco de Dados:** SQLite (Padrão Django)
- **Controle de Versão:** Git & GitHub

## ⚙️ Como rodar o projeto localmente

1. Clone o repositório:
   ```bash
   git clone [https://github.com/Jhon87/my_job_tracker.git](https://github.com/Jhon87/my_job_tracker.git)

2. Crie e ative o ambiente virtual

python -m venv venv
source venv/bin/activate  # No Linux/Mac
# venv\Scripts\activate   # No Windows

3. Instale as dependências:

pip install django

4. Execute as migrações e rode o servidor:

python manage.py migrate
python manage.py runserver

5. Acesse em: http://127.0.0.1:8000


Desenvolvido por **Jonathan Carneiro** como parte do portfólio de desenvolvimento Full Stack.