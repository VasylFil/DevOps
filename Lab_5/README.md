# Лабораторна робота №5. Автоматизація за допомогою Makefile VS Docker Compose

## Docker [ID](https://hub.docker.com/u/vasylfil) & Docker [Repository](https://hub.docker.com/repository/docker/vasylfil/flask)
#### Скріншоти до цієї лабораторної роботи розміщені [тут](https://github.com/VasylFil/lbs/tree/main/Lab_5/img/) 
### Завдання 1-6.
#### Ініціалізація віртуального середовища `pipenv --python 3.8`
```
Using /usr/bin/python3.8 (3.8.0) to create virtualenv...
⠹ Creating virtual environment...created virtual environment CPython3.8.0.final.0-64 in 719ms
  creator CPython3Posix(dest=/root/.local/share/virtualenvs/my_app-fMOJg03G, clear=False, no_vcs_ignore=False, global=False)
  seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/root/.local/share/virtualenv)
    added seed packages: pip==20.3.1, setuptools==51.0.0, wheel==0.36.1
  activators BashActivator,CShellActivator,FishActivator,PowerShellActivator,PythonActivator,XonshActivator

✔ Successfully created virtual environment! 
Virtualenv location: /root/.local/share/virtualenvs/my_app-fMOJg03G
requirements.txt found, instead of Pipfile! Converting...
✔ Success! 
Warning: Your Pipfile now contains pinned versions, if your requirements.txt did. 
We recommend updating your Pipfile to specify the "*" version, instead.
```
#### Інсталяція залежностей `pipenv install -r requirements.txt`

```
Requirements file provided! Importing into Pipfile...
Pipfile.lock not found, creating...
Locking [dev-packages] dependencies...
Locking [packages] dependencies...
Building requirements...
Resolving dependencies...
✔ Success! 
Updated Pipfile.lock (dff687)!
Installing dependencies from Pipfile.lock (dff687)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 7/7 — 00:00:05
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```
#### Запуск додатку `pipenv run python app.py`
#### Запуск тестування `pipenv run pytest test_app.py --url http://localhost:5000`

```
====================================== test session starts ======================================
platform linux -- Python 3.6.9, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /home/ubuntu/Desktop/lab5/tests
collected 4 items                                                                               

test_app.py ....                                                                          [100%]

======================================= 4 passed in 0.22s =======================================
```
### Завдання 7-8.
+ `PHONY` - ціль `Make` призначена для явного задання псевдоцілей 
+ `run` - директива `Make` ініціалізація та запуск імеджів
+ `test-app`- директива `Make` запуск процесу тестування 
+ `docker-prune`- директива `Make` очищає середовище `docker`  

### Завдання 9-12.
#### Виконання директиви *Makefile*: `make .PHONY`
```
✔ Successfully created virtual environment! 
...
<(○_○)>
...
⠙ Locking..✔ Success!
Updated Pipfile.lock (15b487)!
...
Successfully built 782b31cabbd2
Successfully tagged vasylfil/flask:tests
```

#### Виконання директиви *Makefile*: `make run`
```
...
<(○_○)>
6ec7b7d162b2: Pull complete 
Digest: sha256:0f724af268d0d3f5fb1d6b33fc22127ba5cbca2d58523b286ed3122db0dc5381
Status: Downloaded newer image for redis:latest
3885c7cd90195fcfc0c911c4b933f85a4784237993a4e533c8dd92fd6a811577
```

#### Виконання директиви *Makefile*:  `make test-app`
```
============================= test session starts ==============================
platform linux -- Python 3.8.6, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
rootdir: /tests
collected 4 items                                                              

test_app.py ....                                                         [100%]

============================== 4 passed in 0.24s ===============================
```
#### Виконання директиви *Makefile*:  `make docker-prune`
```
...
<(○_○)>
Total reclaimed space: 0B
Deleted Networks:
appnet
...
Total reclaimed space: 0B
```

#### Виконання директиви *Makefile*: `make docker-push`
```
Authenticating with existing credentials...
Login Succeeded
The push refers to repository [docker.io/vasylfil/flask]
...
```

#### Виконання директиви *Makefile*: `make docker-wipe`
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
```
### Завдання 13-19.
#### Перевірка коректної інсталяції `docker-compose version`
```
docker-compose version 1.27.4, build 40524192
docker-py version: 4.3.1
CPython version: 3.7.7
OpenSSL version: OpenSSL 1.1.0l  10 Sep 2019
```

#### Створення проекту `Flask` засобами `docker-compose`: 

`docker-compose -p Flask up`
```
tests    | ============================= test session starts ==============================
tests    | platform linux -- Python 3.8.6, pytest-6.2.0, py-1.10.0, pluggy-0.13.1
tests    | rootdir: /tests
tests    | collected 4 items
tests    | 
app      | 172.21.0.3 - - [14/Dec/2020 13:03:56] "GET /hits HTTP/1.1" 200 -
app      | 172.21.0.3 - - [14/Dec/2020 13:03:56] "GET /logs HTTP/1.1" 200 -
app      | 172.21.0.3 - - [14/Dec/2020 13:03:56] "GET /hits HTTP/1.1" 200 -
app      | 172.21.0.3 - - [14/Dec/2020 13:03:56] "GET /logs HTTP/1.1" 200 -
app      | 172.21.0.3 - - [14/Dec/2020 13:03:56] "GET / HTTP/1.1" 200 -
tests    | test_app.py ....                                                         [100%]
tests    | 
tests    | ============================== 4 passed in 0.21s ===============================
```
###### Проект успішно запущено. Коректне функціонування проекту підтверджується пройденими тестами. Очистка імеджів здійснювалась за допомогою розробленої `Make` директиви `docker-wipe`.
#### Завантаження `docker-compose` імеджів до репозиторію:
`docker-compose push`


### Завдання 20.

#### Створення `docker-compose` для `Django` проекту.

#### Запуск `Django` проекту: `docker-compose -p Django up` 
#### Перевірка наявних імеджів: `docker images`
```
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
vasylfil/app        compose-mon         b7dfb5c66b88        6 minutes ago       331MB
vasylfil/app        compose-app         43140f3d0a24        6 minutes ago       331MB
python              3.8-slim            9285a41f0b19        3 days ago          113MB
vasylfil/app        monitoring          553a6257e0ba        8 days ago          326MB
vasylfil/app        v19.03              2446108687a1        3 weeks ago         326MB
```
#### Завантаження нових імеджів до репозиторію: `docker-compose push`
#### Розроблений файл `docker-compose.yaml` завантажено до репозиторію [4ї](https://github.com/VasylFil/lbs/tree/main/Lab_4) ЛР. Посилання на [raw](https://github.com/VasylFil/lbs/tree/main/Lab_4/docker-compose.yaml) файлу. Нові імеджі завантажено на докер [репозиторій](https://hub.docker.com/repository/docker/vasylfil/app).

![](./img/mandalorian.jpg)
```
 _____ _            _____                         _       
|_   _| |__   ___  |_   _| __ __ _  __ _  ___  __| |_   _ 
  | | | '_ \ / _ \   | || '__/ _` |/ _` |/ _ \/ _` | | | |
  | | | | | |  __/   | || | | (_| | (_| |  __/ (_| | |_| |
  |_| |_| |_|\___|   |_||_|  \__,_|\__, |\___|\__,_|\__, |
                                   |___/            |___/ 
```