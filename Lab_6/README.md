## Lab_6: Автоматизація за допомогою CI/CD серверів.

## Хід роботи:
```python
def lab_2(travis):
     return {
        f'{travis}_task': 'Додано пропущені кроки'
    }

def lab_3(travis):
    return {
        f'{travis}_task':  'Додано скрипт travis-build.sh',
        f'{travis}_task2': 'Додано exit code 0 у цикли'
    }

def lab_4(travis):
    return {
        f'{travis}_task': 'Переписано білд для моніторинг контейнера'
    }

def lab_5(travis):
    return {
        f'{travis}_task': 'Додано функціонал Makefile директиви docker-push'
    }
```


### Travis [репозиторій](https://travis-ci.com/github/VasylFil/lbs/).
+ #### Файл `.travis.yml` [raw](https://github.com/VasylFil/lbs/blob/main/.travis.yml).
+ #### Travis [імедж](https://hub.docker.com/r/vasylfil/app) на Докері.
+ #### Файл `travis-build.sh` [raw](https://github.com/VasylFil/lbs/blob/main/Lab_3/scripts/travis-build.sh).
##
```
 _____ _            ____       _ _                     
|_   _| |__   ___  | __ )  ___| (_) _____   _____ _ __ 
  | | | '_ \ / _ \ |  _ \ / _ \ | |/ _ \ \ / / _ \ '__|
  | | | | | |  __/ | |_) |  __/ | |  __/\ V /  __/ |   
  |_| |_| |_|\___| |____/ \___|_|_|\___| \_/ \___|_|   

```
![](./img/mandalorian.jpg)
