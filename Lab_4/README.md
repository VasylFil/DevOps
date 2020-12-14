# Лабораторна робота №4: Робота з Docker

### Docker [ID](https://hub.docker.com/u/vasylfil)
### Docker [Repository](https://hub.docker.com/repository/docker/vasylfil/app)

#### Перевірка коректної інсталяції
+ Перенаправлення виводу команд у файл `my_work.log`
```bash
echo -e "$(docker -v)\n$(docker -h)\n$(docker run docker/whalesay cowsay Docker is fun)" > my_work.log
```
#### Створення `Dockerfile`

+ Білд імеджа із `Dockerfile`
```
docker build -t vasylfil/app:v19.03 .
```
#### Імедж app успішно створено
+ Перевірка наявних імеджів
```
docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
vasylfil/app        monitoring          553a6257e0ba        3 weeks ago         326MB
vasylfil/app        v19.03              2446108687a1        3 weeks ago         326MB
python              3.8-slim            0f59d947500d        3 weeks ago         113MB
hello-world         latest              bf756fb1ae65        11 months ago       13.3kB
docker/whalesay     latest              6b362a9f73eb        5 years ago         247MB
```

#### ID Створеного імеджа `2446108687a1`


+ Запуск створеного Docker-імеджа
```bash
docker run -d -p 1903:8000 vasylfil/app:v19.03
```

##### Docker контейнер запущено із переадресацією на порт :1903


+ Завантаження імеджа на `DockerHub`

```
docker push vasylfil/app:v19.03
```

#### Створення `Dockerfile.monitoring`

+ Білд нового імеджу
```bash
docker build -t vasylfil/app:monitoring -f Dockerfile.monitoring . 
```

+ Запуск моніторингу
```
docker run -d vasylfil/app:monitoring
```

#### Засобами Docker Volume створено власний том `msf_venom`
```
docker volume create msf_venom
msf_venom
docker volume inspect msf_venom
[
    {
        "CreatedAt": "2020-12-13T17:51:00-05:00",
        "Driver": "local",
        "Labels": {},
        "Mountpoint": "/var/lib/docker/volumes/msf_venom/_data",
        "Name": "msf_venom",
        "Options": {},
        "Scope": "local"
    }
]
```

+ Запуск моніторинг імеджа із створеним томом:
```bash
docker run -it --net=host -v msf_venom:/app vasylfil/app:monitoring
```

![Mandalorian](./img/mandalorian.jpg)
```
 _____ _                _          _ _ 
|_   _| |__   ___      | | ___  __| (_)
  | | | '_ \ / _ \  _  | |/ _ \/ _` | |
  | | | | | |  __/ | |_| |  __/ (_| | |
  |_| |_| |_|\___|  \___/ \___|\__,_|_|

```