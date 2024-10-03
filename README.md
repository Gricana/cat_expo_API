# REST API для онлайн-выставки котят 🐱✨

Добро пожаловать в проект REST API для онлайн-выставки котят! Этот API позволяет взаимодействовать с данными о котятах и их породах, обеспечивая удобные методы для получения, добавления, изменения и удаления информации.

## Стек технологий ⚙️

![Django](https://img.icons8.com/color/48/000000/django.png)
![JWT](https://img.icons8.com/?size=48&id=rHpveptSuwDz&format=png&color=000000)
![Swagger](https://img.shields.io/badge/Swagger-85EA2D?logo=swagger&logoColor=white&style=for-the-badge)
![PostgreSQL](https://img.icons8.com/color/48/000000/postgreesql.png)
![Docker Compose](https://img.icons8.com/ios/48/000000/docker.png)
![Bash](https://img.icons8.com/color/48/000000/bash.png)

## Методы API

### Доступные эндпоинты:

- **Получение списка пород**  
  `GET /api/breeds/`

- **Получение списка всех котят**  
  `GET /api/cats/`

- **Получение списка котят определенной породы по фильтру**  
  `GET /api/cats/?breed_id=<breed_id>`

- **Получение подробной информации о котенке**  
  `GET /api/cats/<cat_id>/`

- **Добавление информации о котенке**  
  `POST /api/cats/`

- **Изменение информации о котенке**  
  `PUT /api/cats/<cat_id>/`
   `PATCH /api/cats/<cat_id>/`

- **Удаление информации о котенке**  
  `DELETE /api/cats/<cat_id>/`

- **Регистрация пользователей**  
  Для регистрации используйте `POST /auth/register/`

- **JWT Авторизация пользователей**  
  Для авторизации используйте `POST /auth/token/`.

## Запуск проекта через Docker Compose 🐳

Следуйте этим шагам для успешного запуска проекта **_на OS Linux_**:

1. Перейдите по пути `dbconf/db.env` и укажите свои кастомные значения для 
   подключения к БД.
  
2. Запустите инфраструктуру проекта из корневой директории проекта командой: 
   ```bash
   docker-compose up -d
   ```
   ### Важные замечания! ⚠️

- **HTTP-порт 80 должен быть свободен!**
- Дайте разрешение всем bash-скриптам на выполнение в директории `dbconf`. Это можно сделать с помощью команды:

  ```bash
  chmod +x dbconf/*.sh
  ```
- Для удобства тестирования в директории _dbconf_ имеется дамп БД _dump.sql_. 
Он автоматически выполняется перед стартом gunicorn в bash-скрипте _entrypoint.sh_. 
Если Вам не нужно это делать, закомментируйте эту строку:
    ```bash
    psql -h db -U $DB_USER -d $DB_NAME -f /expo/dbconf/dump.sql
    ```

- Проект успешно запущен! 🎉 ![cat meow](https://img.icons8.com/?size=30&id=8VdeCQ3puqEp&format=png&color=000000)

    Для тестирования API перейдите по следующему 
    пути: [Cat Expo API](localhost/api/docs)

- Для авторизации и корректного выполнения всех эндпоинтов нажмите на кнопку 
**'Authorize'**. 

    В открывшейся форме введите актуальный _**access_token**_ в формате:
    ```bash
    Bearer <token> 
    ```
