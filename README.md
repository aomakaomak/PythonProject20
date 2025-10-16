# Курсовой проект: выгрузка вакансий из HH.ru в PostgreSQL и отчёты

Проект получает данные о работодателях и их вакансиях через **публичный API hh.ru** (без авторизации) и сохраняет их в **PostgreSQL**. Затем предоставляет набор отчётных запросов (средняя зарплата, вакансии с зарплатой выше средней, поиск по ключевому слову и др.).

## Стек
- Python 3.11+  
- PostgreSQL 14+  
- Библиотеки: `requests`, `psycopg2`  
- Источник данных: `https://api.hh.ru`

## Структура проекта
```
project/
├─ src/
│  ├─ main.py
│  ├─ final_func_for_main.py
│  ├─ utils_api.py
│  ├─ utils_bd.py
│  └─ db_manager.py
└─ README.md
```

## Установка
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate   # Windows
pip install requests psycopg2-binary
```

Создай БД PostgreSQL:
```sql
CREATE DATABASE pythontask;
CREATE USER postgres WITH PASSWORD 'yompks83new';
GRANT ALL PRIVILEGES ON DATABASE pythontask TO postgres;
```

## Как работает
1. Список компаний задаётся в `main.py`.
2. Для каждой — получение id, вакансий, запись в БД.
3. Далее выполняются отчёты (`DBManager`).

## Запуск
```bash
python -m src.main
```

## Схема БД
```sql
CREATE TABLE IF NOT EXISTS employers (
    employer_id int PRIMARY KEY,
    employer_name varchar(300)
);

CREATE TABLE IF NOT EXISTS vacancies (
    vacancy_id serial PRIMARY KEY,
    vacancy_name varchar(300),
    employer_id int REFERENCES employers (employer_id),
    city varchar(100),
    salary int,
    vacancy_link varchar(300)
);
```

## Основные функции
- `utils_api.py`: `get_id`, `get_vacancies_per_id`
- `utils_bd.py`: создание и наполнение таблиц
- `final_func_for_main.py`: оркестрация
- `db_manager.py`: SQL-отчёты

## Пример запросов
Средняя зарплата:
```sql
SELECT AVG(salary) FROM vacancies;
```
Вакансии с ключевым словом:
```sql
SELECT vacancy_name FROM vacancies WHERE vacancy_name ILIKE '%курьер%';
```

## Лицензия
Используются публичные данные HH.ru с соблюдением правил нагрузки и указанием User-Agent.
