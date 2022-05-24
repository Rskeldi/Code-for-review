# Code for review
##### Python 3.8.10


### Примечание
Если у вас уже работает `PostgreSQL` или `Redis`, то их нужно отключить
````
sudo systemctl stop postgresql.service 
sudo systemctl stop redis.service
````
Потом их надо будет включить. Команды в конце
<br>

#### Чтобы удобнее было читать код, я сделал pull request
[Pull request](https://github.com/Rskeldi/Test-Job/pull/1/files)


### START

Первым делом надо заполнить .env по образу .env.example
Для удобства можно просто скопировать содержимое .env.example, все будет работать

`cp .env.example .env`

<br>

### Docker
Если нету докера, то нужно установить
Установка на 
[Ubuntu](https://www.digitalocean.com/community/tutorials/docker-ubuntu-18-04-1-ru)




## Autotests

`docker-compose up autotests`

## Runserver

`docker-compose up runserver`

### Ссылки:
<br>

#### Admin
[Ссылка на админку](http://0.0.0.0:8000/admin/)
##### username: admin
##### password: admin
<br>

#### Page List
[PageListAPI](http://0.0.0.0:8000/api/v1/)

[Ссылка на 2 страницу пацинации](http://0.0.0.0:8000/api/v1/?page=2)

<br>

#### Detail 
[Детальная страница](http://0.0.0.0:8000/api/v1/1/)

[Детальная страница в виде JSON](http://0.0.0.0:8000/api/v1/1/?format=json)

### Docker контейнеры
Выключить контейнеры после docker-compose
`docker-compose down -v`

И не забудьте потом удалить ненужные Docker контейнеры и image

### ВАЖНО
Не забудьте включить 
````
sudo systemctl start postgresql.service 
sudo systemctl start redis.service
