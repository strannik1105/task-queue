from common.enums import TaskType
from task_queue.task.abstract_task import AbstractTask
from task_queue.task.mock_task import MockTask


TASK_MAPPER = {TaskType.Mock: MockTask}


class TaskFactory:
    @staticmethod
    def get_task(type_: TaskType, *args, **kwargs) -> AbstractTask:
        return TASK_MAPPER[type_](*args, **kwargs)
