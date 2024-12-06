from common.router import BaseRouter, HttpMethod
from common.schemas import Msg
from producer.router.schema import MockTaskSchema, MockTaskCreateSchema
from task_storage.deps import RedisTaskStorage


class TaskRouter(BaseRouter):
    def register_handlers(self) -> None:
        self.register_route("/create_task", self.create_task, HttpMethod.POST)

    async def create_task(
        self, storage: RedisTaskStorage, task: MockTaskCreateSchema
    ) -> MockTaskSchema:
        task_id = await storage.make_task(task.task_type, task.task_params)
        return MockTaskSchema(task_id=task_id)
