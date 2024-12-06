import abc


class AbstractService(abc.ABC):
    @abc.abstractmethod
    async def run(self) -> None:
        pass
