# Сравнение тарифов мобильных операторов

Программа принимает значения фильтра выбранные пользователем и
предлагает список тарифов с небольшим разбросом значений для увеличения 
вариантов. 
В каждой строке с предлагаемым тарифом показаны дополнительные опции(при наличии) и ссылка на страницу оператора.
В проекте используется SQLAlchemy и база данных SQLite.

## Установка

Скачайте проект с github:

```
git clone https://github.com/theoneman44/operator_comparing
```
Создайте виртуальное окружение, необходимое для Вашей системы, и установите зависимости:

```
pip install -r requirements.txt
```

Создайте файл config.py и задайте в нем базовые переменные:

```
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'tarifs.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
UPLOAD_FOLDER = './images'
SECRET_KEY = "Ваш ключ"
```

## Запуск программы

Для запуска программы выполните команду `run` из дирректории в которой находится скачанная программа.

### P.S.
Для корректной работы программы понадобится файл базы данных `tarifs.db` заполненный в соответствии с параметрами моделей. 
На данный момент автоматическое наполнение базы данных в разработке.