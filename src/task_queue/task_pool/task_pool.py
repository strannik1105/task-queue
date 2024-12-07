import asyncio
from threading import Thread
from typing import Callable

from common.enums import StatusType
from task_queue.task.abstract_task import AbstractTask
from task_queue.task.factory import TaskFactory
from task_storage import AbstractTaskStorage


class TaskExecutor:
    def __init__(self, task: AbstractTask, callback: Callable) -> None:
        self._task = task
        self._callback = callback

    def __call__(self) -> None:
        self._task.exec()
        self._callback(self._task)


class TaskPool:
    def __init__(self, storage: AbstractTaskStorage) -> None:
        self._storage = storage
        self._working: dict[AbstractTask, Thread] = {}

    async def _next_task(self) -> AbstractTask | None:
        if len(self._working.keys()) >= 2:
            return None
        try:
            task = await self._storage.get_task()
            return TaskFactory.get_task(task.type, task_id=task.pk, **task.params)
        except IndexError:
            return None

    async def run(self) -> None:
        await self._storage.init()
        loop = asyncio.get_event_loop()

        def callback(task: AbstractTask) -> None:
            loop.create_task(
                self._storage.change_task_status(task.id, StatusType.COMPLETED)
            )

        while True:
            task = await self._next_task()
            if task is None:
                await asyncio.sleep(0.1)
                continue

            await self._storage.change_task_status(task.id, StatusType.RUN)
            task_thread = Thread(target=TaskExecutor(task, callback))
            self._working[task] = task_thread
            task_thread.start()
