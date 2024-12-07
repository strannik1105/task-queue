import abc


class AbstractTask(abc.ABC):
    def __init__(self, *, task_id):
        self.id = task_id

    @abc.abstractmethod
    def exec(self) -> None:
        pass
