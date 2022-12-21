# Stepik Selenium Cource Final Project - Page Object Pattern

[ссылка](https://stepik.org/lesson/238819/)

## Запуск тестов

### Подготовка окружения
в чистом виртуальном окружении нужно выполнить команду
```
pip install -r requirements.txt
```

### Запуск pytest

Из корня проекта выполнить команду:

```
python -m pytest -v --tb=line -m need_review --language=en --headless
```

`--headless` и `--language` - необязательные аргументы


Если у вас ОС linux, то доступны команды:

```
make review-tests  # запуск тестов, помеченных как need_review
make all-tests-headless  # запуск всех тестов с использованием headless браузера
make all-tests  # запуск всех тестов
```
