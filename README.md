# ENCARGOS E NECESSIDADES DOCENTES

### Objetivo Geral:
Ter o controle de cursos, disciplinas, ofertas, encargos e necessidades docentes. O acesso deve
ser feito somente por coordenadores, diretores ou pela parte adiministrativa de um Campus.

### Casos de uso:
* Controle de usuários
    * Cada usuário só pode se logar em um campus.
* Controle dos Professores cadastrados
    * Cada professor está alocado em um único curso.
    * Cada professor atua em uma ou mais Areas.
    * Quem cadastra os professores sao usuários da administraçao ou RH.
* Controle dos Vinculos empregatícios
* Controle da Matriz Curricular de cada curso
* Controle dos Cursos
* Controle de Areas
* Controle das Disciplinas dos Cursos
    * Uma Disciplina pode conter uma ou mais Areas.
* Produzir Ofertas para os Cursos
    * O coordenador terá a opçao de definir ofertas.
* Contabilizar cargas horárias
    * Sinalizar se a carga horária está baixa, normal ou alta.
* Emitir relatório de cada carga horária

### Competências:
* Engenharia de Software/Banco de Dados (UML – Casos de uso e Classes)
* Desenvolvimento Web (Django):
    * Design (HTML, CSS, Javascript)
    * Programação (Python)

### Participantes:
* Eyder       -   eyder@phb.uespi.br
* George      -   georgelima11@hotmail.com
* Honorato    -   vishnora@hotmail.com
* Jefferson   -   jeffersonhcarvalho@gmail.com
* Germano     -   germanomgomes@hotmail.com
* Jean        -   otirbnaej@hotmail.com
* Luiz        -   luizrodrigo46@hotmail.com
* Athyrson    -   athyrsonmr@gmail.com
* Herbson     -   hbscjk@gmail.com
* Jordano     -   jordanolb95@hotmail.com
* Augusto     -   augustocalaca2@gmail.com
* Assis       -   netodamasceno12@gmail.com

## Instalando

### 1º passo: clonar o repositório para o seu computador:

No terminal, escolha um diretório, e execute o seguinte comando:
```
git clone https://github.com/JeffersonCarvalh0/encargos-e-necessidades-docentes.git
```

O projeto será baixado no diretório onde o comando foi executado.

### 2º passo: instalar os pré requisitos

Dentro do diretório do repositório clonado, execute do terminal:
```
pip install -r requirements.txt
```

### 3º passo: testar

Para testar, mude para a pasta ```sistema/``` dentro do projeto, e execute o
script ```manage.py```, passando o argumento ```runserver```.

```
./manage.py runserver
```
ou
```
python2 manage.py runserver
```
caso o script não tenha permissão de execução.

Após isso, basta acessar o endereço http://127.0.0.1:8000/ do navegador de sua preferência, para ter acesso ao site.

## Desenvolvido com
 * [Django 1.11](https://docs.djangoproject.com/pt-br/1.11/) - Framework para desenvolvimento web usando python
 * [django-admin-bootstrap](https://github.com/douglasmiranda/django-admin-bootstrap) - Tema bootstrap responsivo para a interface de administração do django
