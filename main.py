import json
import uuid


class TaskTrackerMenu(object):
    def __init__(self):
        pass


class TaskBase(object):
    def __init__(self):
        pass


class Task(object):
    def __init__(self, name: str, description: str):
        self.task_info = {"name": name,
                          "description": description,
                          "id": uuid.uuid4()}

    @property
    def name(self):
        return self.task_info["name"]

    @name.setter
    def name(self, value):
        if value:
            self.task_info["name"] = value

    @property
    def description(self):
        return self.task_info["description"]

    @description.setter
    def description(self, value):
        if value:
            self.task_info["description"] = value


def main():
    pass


if __name__ == '__main__':
    main()
