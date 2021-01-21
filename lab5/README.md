Спробувала чи проєкт є працездатним перейшовши у папку, а після ініціалізації середовища виконала команди записані нижче:

pipenv --python 3.9
pipenv install -r requirements.txt
pipenv run python3 app.py

Ініціалузувала середовище для тестів у іншій вкладці шелу та запустила їх командою:

pipenv run pytest test_app.py --url http://localhost:5000

Тести були невдалі, тому що не було запущено redis-server

Ознайомилась з вмістом Dockerfile та Makefile. Директиви Makefile:
1)STATES -  variable to save the directives(змінна для зберігання директив);
2)REPO - variavble to save names of Docker repository (змінна для зберігання назви Docker репозиторію);
3).PHONY - allows to declare false integer (дозволяє оголошувати фальшиві цілі);
4)$(STATES) - directive to biult a container (директива для білда контейнера);
5)run - directive to create network (директива для створення мережі);
6)test-app - directive to start a container with monitoring(директива для запуску контейнера з моніторингом);
7)docker-prune - deleting containers, volumes, networks and images(видалення контейнерів, волюмів, мереж та імеджів).

Запустила додаток та тести. Пройшли успішно.

main page
hits
logs

Дві мережі: public - мережа з якої можуть підключатись користувачі та secret - для доступу до redis.

Веб-сайт працює. У браузері потрібно зайти на адресу localhost:80.

Зручніше використувати docker-compose.
