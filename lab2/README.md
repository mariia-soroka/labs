Встановила pipenv та створила ізольоване середовище для Python:

pip install pipenv
pipenv --python 3.8
pipenv shell

Встановила бібліотеки requests, ntplib:

pipenv install requests
pipenv install ntplib

Створила файл app.py, скопіювала у нього код програми з репозиторію, програма працює правильно.

Встановила бібліотеку pytest та запустила тести, всі тести виконались успішно:

pipenv install pytest
pytest tests/tests.py

Дописала у програмі функцію, що перевіряє час доби на AM/PM та відповідно друкує "Доброго дня/ночі". Також написала тест, що перевіряє правильність роботи функції.

Перенаправила результат виконання функції та тестів у файл results.txt:

pipenv run pytest tests/tests.py >> results.txt
pipenv run python app.py append >> results.txt

Створила та закомітила до репозиторію Makefile.
