import random
import time

from task_queue.task.abstract_task import AbstractTask


class MockTask(AbstractTask):
    def exec(self):
        print(f"Task {self.id} start")
        time.sleep(random.randint(0, 10))
        print(f"Task {self.id} end")
