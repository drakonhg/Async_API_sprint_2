# Проектная работа 5 спринта
______
 __Состав команды__ 
 - [Сергиевский Алексей](https://github.com/VIVERA83?tab=repositories)
 - [Чириков Андрей](https://github.com/drakonhg)
 
репозиторий [Async_API_sprint_2](https://github.com/VIVERA83/Async_API_sprint_2)

** ETL **
-  [docker репозиторий](https://hub.docker.com/r/vivera83/etl/tags)
-  [git репозиторий](https://github.com/VIVERA83/ETL_end)
______

** Admin_panel **  
- [docker репозиторий](https://hub.docker.com/r/vivera83/admin_panel/tags)
- [git репозиторий](https://github.com/VIVERA83/ETL_end)

вызов:
- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/api/openapi

запуск через docker-compose

````
docker-compose up --build 
````
ОБРАТИ ВНИМАНИЕ:   

- POSTGRES пустой, наполнить можно взяв бд из первых спринтов. Таблицы в Postgres созданы, так же открыт port 5432
- Не забудь создать .env для докера, образец лежит в [.env_example](.env_example)
- __На всякий пожарный.__ В Redis в data - хранятся состояния, для того что бы переписать elastic, просто удали или обнули запись
_____
____

В папке tasks ваша команда найдёт задачи, которые необходимо выполнить во втором спринте модуля "Сервис Async API".

Как и в прошлом спринте, мы оценили задачи в стори поинтах.

Вы можете разбить эти задачи на более маленькие, например, распределять между участниками команды не большие куски задания, а маленькие подзадачи. В таком случае не забудьте зафиксировать изменения в issues в репозитории.

От каждого разработчика ожидается выполнение минимум 40% от общего числа стори поинтов в спринте.