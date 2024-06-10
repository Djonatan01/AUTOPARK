
# AutoPrak-App

###### Apresentamos um protótipo AutoPrak para gerenciamento de estacionamento, que utiliza tecnologias RFID e ESP32 para um controle preciso de entrada e saída de veículos, integrado a um sistema web robusto desenvolvido em Python Flask com HTML, JavaScript e CSS. Este projeto redefine a eficiência e segurança na administração de estacionamentos.

###### Protótipo desenvolvido para trabalho de graduação Fatec de Cruzeiro-SP.

## Libraries and Tools

### Backend

* 🐍 [Python](https://www.python.org/)
* 🧪 [Flask](https://flask.palletsprojects.com/en/2.3.x/)
* ⚗️ [SQLAlchemy (Object Relational Mapper - ORM)](https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/)

### Frontend
* 🖥️ [HTML5](https://developer.mozilla.org/en-US/docs/Glossary/HTML5)
* ⚡️ [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
* ✨ [BootStrap](https://getbootstrap.com/)

## Project Organization

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