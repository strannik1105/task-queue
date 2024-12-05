import asyncio
from collections import deque

from task_queue.task.abstract_task import AbstractTask


class TaskPool:
    def __init__(self) -> None:
        self._waiting: deque[AbstractTask] = deque()
        self._working: list[AbstractTask] = []

    def add_task(self, task: AbstractTask) -> None:
        self._waiting.append(task)

    def _next_task(self) -> AbstractTask | None:
        if len(self._working) >= 2:
            return None
        try:
            return self._waiting.pop()
        except IndexError:
            return None

    async def run(self) -> None:
        while True:
            task = self._next_task()
            if task is None:
                await asyncio.sleep(0.1)
                continue
            asyncio.create_task(task.exec())
            await task.exec()
