
# AutoPrak-App

###### Apresentamos AutoPrak um protótipo para gerenciamento de estacionamento, que utiliza tecnologias RFID e ESP32 para um controle preciso de entrada e saída de veículos, integrado a um sistema web robusto desenvolvido em Python Flask com HTML, JavaScript e CSS. Este projeto redefine a eficiência e segurança na administração de estacionamentos.

###### Protótipo desenvolvido para trabalho de graduação Fatec de Cruzeiro-SP.

## Bibliotecas e Ferramentas

### Backend

* 🐍 [Python](https://www.python.org/)
* 🧪 [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* ⚗️  [SQLAlchemy (Object Relational Mapper - ORM)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

### Frontend
* [![HTML5](https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/HTML5_logo_and_wordmark.svg/50px-HTML5_logo_and_wordmark.svg.png)](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* [![CSS Icon](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d5/CSS3_logo_and_wordmark.svg/50px-CSS3_logo_and_wordmark.svg.png)](https://developer.mozilla.org/en-US/docs/Web/CSS)
* [![JavaScript Icon](https://github.com/Djonatan01/AutoPark/assets/103201121/5f6f6e3b-3c7a-4af8-ab59-b5603657e9e0)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [![Bootstrap Icon](https://upload.wikimedia.org/wikipedia/commons/thumb/b/b2/Bootstrap_logo.svg/50px-Bootstrap_logo.svg.png)](https://getbootstrap.com/)



## Project Organizatio

The API was designed using the Model-View-Controller (MVC) pattern:

#### View (Directory that contains the classes for the project activities)

* [User](Src/View/User.py), [Traffic](Src/View/Traffic.py), [Login](Src/View/Login.py), [Home](Src/View/Home.py), [Employee](Src/View/Employee.py) and [About](Src/View/About.py)

#### Controller (Action methods)

* [Users](Src/Controller/Users.py), [Employees](Src/Controller/Employees.py) and [RFID](Src/Controller/RFID.py)

#### Model (The logical structure of a database)

* There is only one database file that is responsible for managing the database of all entities
* [DataBase](Src/Model/BancoDados.py)

## Project Setup

First, create a virtual env to host the project dependencies.
Install the necessary dependencies with the following commands:
////////////////////

## Organização do Projeto

* O protótipo foi desenvolvido usando o padrão Model-View-Controller (MVC):

#### Visão (Diretório que contém as classes para as atividades do protótipo)

* [User](Src/View/User.py), [Tráfego](Src/View/Traffic.py), [Login](Src/View/Login.py), [Página Inicial](Src/View/Home.py) and [Sobre](Src/View/About.py)

Controlador (Métodos de ação)
Usuários, Funcionários e RFID
Modelo (A estrutura lógica de um banco de dados)
Há apenas um arquivo de banco de dados que é responsável por gerenciar o banco de dados de todas as entidades
BancoDados
Configuração do Projeto
Primeiro, crie um ambiente virtual para hospedar as dependências do projeto.
Instale as dependências necessárias com os seguintes comandos:




/////////////////////
Linux:

```bash
cd Backend
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Windows:

```bash
cd Backend
python3 -m venv .venv
env\Scripts\activate.bat
pip install -r requirements.txt
```

Then, initialize the API server:

```bash
python main.py
```

#
### Navigate the project
 - ###### [Backend](https://github.com/adaatii/EasyInOut/tree/main/Src)
 - ###### [Frontend](https://github.com/adaatii/EasyInOut/tree/main/Templates)
