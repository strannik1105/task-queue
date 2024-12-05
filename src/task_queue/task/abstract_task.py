import abc


class AbstractTask(abc.ABC):
    @abc.abstractmethod
    async def exec(self) -> None:
        pass
