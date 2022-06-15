from asyncio import sleep
from elasticsearch import AsyncElasticsearch
from aioredis import Redis
from aioredis.exceptions import ConnectionError
from typing import Union

from .backoff import before_execution


@before_execution()
async def waiters_one(cli: Union[AsyncElasticsearch, Redis]) -> bool:
    while True:
        await sleep(1)
        try:
            if await cli.ping():
                return True
        except ConnectionError:
            pass
        except Exception:
            pass
