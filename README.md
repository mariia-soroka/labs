# Лабораторна робота №4: Робота з Docker


+ Я створила файл `my_work.log`
```
(docker -v; docker --help; docker run docker/whalesay cowsay Docker is fun;) > my_work.log
```

+ Робимо білд імеджа із `Dockerfile`
```
docker build -t mariiasoroka/lab4:django .
```
+ Далі перевірила наявні імеджи
```
docker images
```

+ Запустила Docker-імеджа, який я створила до того
```
docker run -it -p 8000:8000 mariiasoroka/lab4:django
```

+ Побудувала новий імедж
```
docker build -t mariiasoroka/lab4:monitoring -f Dockerfile.monitoring . 
```

+ Далі запустила моніторинг
```
docker run -it mariiasoroka/lab4:monitoring
```

+ Далі завантажила імедж на `DockerHub`

```
docker push mariiasoroka/lab4:django
docker push mariiasoroka/lab4:monitoring
```
+ Запустила моніторинг імеджа із створеним томом:
```
docker run -it --net=host -v /home/ubuntu/Desktop/lab4:/app/ mariiasoroka/lab4:monitoring
```

### Docker [ID](https://hub.docker.com/u/mariiasoroka)
### Docker [Repository](https://hub.docker.com/repository/docker/mariiasoroka/lab4)