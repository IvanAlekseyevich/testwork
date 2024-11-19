# # ТЗ Python_SMIT

***Приложение по расчёту стоимости страхования***

### Описание работы приложения
- Эндпоинт rate/ принимает данные в виде json и сохраняет их в БД
```json
{
  "2020-06-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.04"
    },
    {
      "cargo_type": "Other",
      "rate": "0.01"
    }
  ],
  "2020-07-01": [
    {
      "cargo_type": "Glass",
      "rate": "0.035"
    },
    {
      "cargo_type": "Other",
      "rate": "0.015"
    }
  ]
}
```
- Эндпоинт calculate/ принимает данные и возвращает подсчет суммы на данную дату 
```json
{
  "cargo_type": "Glass",
  "date": "2020-10-10",
  "price": "1000"
}
```

### Инструкция по работе с приложением

- Переименуйте файл *example.env* в *.env* и заполните его своими данными
- Для локального запуска создайте виртуальное окружение, активируйте его и установите зависимости
- Запустите установку миграций в БД
```commandline
alembic upgrade head
```
- Запустите приложение
```commandline
uvicorn main:app  --reload
```

### Переменные окружения

<details>
 <summary>
 Переменные окружения
 </summary>

```
ALLOWED_HOST=
APP_TITLE=
APP_DESCRIPTION=
DATABASE_URL=
POSTGRES_HOST=           
POSTGRES_USER=
POSTGRES_PASSWORD=
POSTGRES_DATABASE=
POSTGRES_PORT=
```

</details>

