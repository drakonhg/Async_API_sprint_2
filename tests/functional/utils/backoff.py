from functools import wraps
from asyncio import wait_for, Event, sleep, create_task
from typing import Any, Callable
import logging
from random import randint


async def timeout(event: Event, time_out: int):
    """Вспомогательная функция которая по истечению time_out снимает блокировку с события event"""
    await sleep(time_out)
    event.set()
    return True


def delta_time() -> float:
    return randint(100, 1000) / 1000


def before_execution(
    total_timeout=20, request_timeout: int = 3, logging_level=logging.ERROR
) -> Any:
    """Декоратор, который пытается выполнить входящий вызываемый объект, в течении определенного времянки,
    в случае неудачи возвращает None"""
    event = Event()  # event блокирует выход из цикла

    def func_wrapper(func: Callable):
        @wraps(func)
        async def inner(*args, **kwargs):
            # по сути засекаем время которое будет работать цикл
            task = create_task(timeout(event, total_timeout))
            while not event.is_set():
                try:
                    result = await wait_for(func(*args, **kwargs), request_timeout)
                    # отменяем запущенный таймаут если он еще не кончился
                    if not task.done():
                        task.cancel()
                    return result
                except Exception as ex:
                    sec = randint(0, 1) + delta_time()
                    msg = (
                        f"db connection error...\n"
                        f"location: before_execution,  {ex}\n"
                        f"nested function: {func}\n"
                        f"sleep: {sec} sec\n"
                        f"task: {task.get_name()}\n"
                    )
                    logging.log(logging_level, msg)
                    await sleep(sec)

        return inner

    return func_wrapper
