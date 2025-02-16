import datetime
import json

"""Status: done; in progress, not done"""


class TaskTrackerMenu(object):
    def __init__(self):
        pass


class TaskBase(object):
    id: int = 0

    def __init__(self):
        self.task_base = []

    def check_base(self):
        pass

    def create_task(self, description):
        task: Task = Task(TaskBase.id, description)
        TaskBase.id += 1


class Task(object):
    def __init__(self, id: int, description: str) -> None:
        self._id: int = id
        self.description: str = description
        self.status: str = "not done"
        self._created_at: datetime = datetime.datetime.now()
        self._updated_at: datetime = None

    @property
    def id(self) -> int:
        return self._id

    @property
    def description(self) -> str:
        return self.description

    @description.setter
    def description(self, value: str) -> None:
        if value:
            self.description = value
        else:
            print("description cannot be None")

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        if value in ["not done", "in progress"]:
            self._status = value
        if value == "done":
            self._status = "done"
            self._updated_at = datetime.datetime.now()
        else:
            print("value must be 'done' or 'not done' or 'in progress'")


def main():
    pass


if __name__ == '__main__':
    main()
