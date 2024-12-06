import abc

from common.enums import TaskType


class AbstractTaskStorage(abc.ABC):
    @abc.abstractmethod
    def init(self) -> None:
        pass

    @abc.abstractmethod
    async def make_task(
        self, task_type: TaskType, task_params: dict | None = None
    ) -> str:
        pass
