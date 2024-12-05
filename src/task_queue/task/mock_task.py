import random
import time

from task_queue.task.abstract_task import AbstractTask


class MockTask(AbstractTask):
    async def exec(self):
        time.sleep(random.randint(0, 10))
