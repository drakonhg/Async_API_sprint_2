import asyncio

import aioredis
from elasticsearch import AsyncElasticsearch
from fastapi import Request, FastAPI
from fastapi.responses import ORJSONResponse

import src.api.v1.model.api_model as genre
from src.api.v1.api_films import film_router
from src.api.v1.api_genre import genre_router
from src.api.v1.api_person import person_router
from src.core.config import Settings
from src.db import elastic
from src.db import redis

from icecream import ic

ic.includeContext = True
first_update_genre = True
settings = Settings()


app = FastAPI(
    # Конфигурируем название проекта. Оно будет отображаться в документации
    title=settings.project_name,
    # Адрес документации в красивом интерфейсе
    docs_url="/api/openapi",
    # Адрес документации в формате OpenAPI
    openapi_url="/api/openapi.json",
    description="Информация о фильмах, жанрах и людях, участвовавших в создании произведения",
    version="1.0.0",
    # Можно сразу сделать небольшую оптимизацию сервиса
    # и заменить стандартный JSON-сереализатор на более шуструю версию, написанную на Rust
    default_response_class=ORJSONResponse,
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    global first_update_genre
    response = await call_next(request)
    ic(first_update_genre)
    if (request.url.path == "/api/openapi") or first_update_genre:
        genre.GenreEnum = await genre.GenreEnum.update_genre()
        if len(genre.GenreEnum):
            first_update_genre = False
    return response


@app.on_event("startup")
async def startup():
    # Подключаемся к базам при старте сервера
    # Подключиться можем при работающем event-loop
    # Поэтому логика подключения происходит в асинхронной функции
    redis.redis = await aioredis.Redis.from_url(
        f"redis://{settings.redis_host}:{settings.redis_port}/{settings.redis_db_number}"
    )
    elastic.es = AsyncElasticsearch(
        f"http://{settings.elastic_host}:{settings.elastic_port}", api_key="hello world"
    )


@app.on_event("shutdown")
async def shutdown():
    # Отключаемся от баз при выключении сервера
    print(*asyncio.all_tasks(), "\n")
    await redis.redis.close()
    await elastic.es.close()


# Подключаем роутер к серверу, указав префикс /v1/films
# Теги указываем для удобства навигации по документации
app.include_router(film_router, prefix="/api/v1/films", tags=["Фильмы"])
app.include_router(genre_router, prefix="/api/v1/genres", tags=["Жанры"])
app.include_router(person_router, prefix="/api/v1/person", tags=["Персоны"])
