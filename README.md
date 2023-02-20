# Desafio-Python-WeDev-Software

## Installation

Use [git](https://gitforwindows.org) to clone this repository.

```bash
git clone https://github.com/victorhenrique07/Desafio-Python-WeDev-Software
```

## How to run

### Linux (need Docker and docker-compose)
```bash
# if you are not inside directory:
cd Desafio-Python-WeDev-Software && docker-compose up -d
```
```bash
# create the super user:
docker exec -it django python wedev/manage.py createsuperuser

```

# Documentation
## Routes
```
localhost:8000/accounts/login
```
Return a login template to Alunos and Professores.
After log in, you'll be redirect to:

```
localhost:8000/app/user/profile/<str:pk>/
```
Return profile user logged in.
Need to be logged in to access.

```
localhost:8000/app/user/profile/edit/<int:pk>/ 
```
Need to be logged in to access.
Return all editable fields. <br> Need to pass the user ID <int:pk>/ to access <br>
Just users with "editar_perfil" permission can access.
```
app/users/alunos
```
Need to be logged in to access. <br>
Return all alunos registered. <br>
Need "view_aluno" permission to access. 
```
app/cursos
```
Need to be logged in to access. <br>
Return all cursos registered.
Need "view_curso" permission to access