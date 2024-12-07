from typing import Any

from aredis_om import Migrator, NotFoundError  # type: ignore

from common.enums import StatusType, TaskType
from task_storage.abstract_task_storage import AbstractTaskStorage
from task_storage.redis.models import Task


class RedisTaskStorage(AbstractTaskStorage):
    migrated = False

    async def init(self) -> None:
        if not self.migrated:
            await Migrator().run()
            self.migrated = True

    async def make_task(
        self, task_type: TaskType, task_params: dict | None = None
    ) -> str:
        task = Task(type=task_type, params=task_params)
        await task.save()
        return task.pk

    async def get_task(self) -> Any:
        try:
            task = (
                await Task.find(Task.status == StatusType.IN_QUEUE)
                .sort_by("created_at")
                .first()
            )
            return task
        except NotFoundError:
            raise IndexError

    async def change_task_status(self, key: str, status: StatusType) -> None:
        task = await Task.get(key)
        task.status = status
        await task.save()
