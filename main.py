import datetime
import json
import os


class TaskTrackerMenu:
    def __init__(self):
        self.task_base = TaskBase()

    def show_menu(self):
        while True:
            print("\nTask Tracker Menu:")
            print("1. Add task")
            print("2. List all tasks")
            print("3. List tasks by status")
            print("4. Change task status")
            print("5. Delete task")
            print("6. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.task_base.list_tasks()
            elif choice == "3":
                self.list_tasks_by_status()
            elif choice == "4":
                self.change_task_status()
            elif choice == "5":
                self.delete_task()
            elif choice == "6":
                self.task_base.save_base()
                print("Exiting...")
                break
            else:
                print("Invalid choice, please try again.")

    def add_task(self):
        description = input("Enter task description: ")
        if description:
            self.task_base.create_task(description)
            self.task_base.save_base()
            print("Task added successfully!")
        else:
            print("Description cannot be empty!")

    def list_tasks_by_status(self):
        status = input("Enter status (not done / in progress / done): ")
        if status in ["not done", "in progress", "done"]:
            self.task_base.list_tasks_by_status(status)
        else:
            print("Invalid status.")

    def change_task_status(self):
        try:
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (not done / in progress / done): ")

            task = next((t for t in self.task_base.task_base if t.id == task_id), None)
            if task and status in ["not done", "in progress", "done"]:
                task.status = status
                self.task_base.save_base()
                print("Task status updated successfully!")
            else:
                print("Invalid task ID or status.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")

    def delete_task(self):
        try:
            task_id = int(input("Enter task ID to delete: "))
            if self.task_base.delete_task(task_id):
                print("Task deleted successfully!")
            else:
                print("Task not found.")
        except ValueError:
            print("Invalid input. Task ID must be a number.")


class TaskBase(object):
    def __init__(self):
        self.task_base: list[dict] = []
        self.check_base()
        self.load_base()
        self._id = len(self.task_base)

    def check_base(self) -> None:
        if not os.path.exists("task_base.json"):
            with open("task_base.json", "w") as file:
                json.dump([], file)

    def load_base(self) -> None:
        with open("task_base.json", "r") as file:
            try:
                self.task_base = [Task.from_dict(task) for task in json.load(file)]
            except json.JSONDecodeError:
                self.task_base = []

    def save_base(self) -> None:
        with open("task_base.json", "w") as file:
            json.dump([task.to_dict() for task in self.task_base], file, indent=4)

    def create_task(self, description) -> None:
        task = Task(self._id, description)
        self._id += 1
        self.task_base.append(task)

    def list_tasks(self) -> None:
        print(f"{'ID':<5} {'Description':<20} {'Status':<12} {'Created At':<20} {'Updated At'}")
        print("-" * 70)
        for task in self.task_base:
            print(f"{task.id:<5} {task.description:<20} {task.status:<12} {task.created_at:<20} {task.updated_at}")

    def list_tasks_by_status(self, status) -> None:
        print(f"{'ID':<5} {'Description':<20} {'Status':<12} {'Created At':<20} {'Updated At'}")
        print("-" * 70)
        for task in self.task_base:
            if task.status == status:
                print(f"{task.id:<5} {task.description:<20} {task.status:<12} {task.created_at:<20} {task.updated_at}")


class Task(object):
    def __init__(self, id: int, description: str) -> None:
        self._id: int = id
        self._description: str = description
        self._status: str = "not done"
        self._created_at: datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        self._updated_at: datetime = None

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "description": self._description,
            "status": self._status,
            "created_at": self._created_at,
            "updated_at": self._updated_at
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Task":
        task = cls(data["id"], data["description"])
        task._status = data["status"]
        task._created_at = data["created_at"]
        task._updated_at = data["updated_at"]
        return task

    @property
    def id(self) -> int:
        return self._id

    @property
    def description(self) -> str:
        return self._description

    @description.setter
    def description(self, value: str) -> None:
        if value:
            self._description = value
        else:
            print("description cannot be None")

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str) -> None:
        if value in ["not done", "in progress", "done"]:
            self._status = value
            if value == "done":
                self._updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        else:
            print("value must be 'done', 'not done', or 'in progress'")

    @property
    def created_at(self) -> str:
        return self._created_at

    @property
    def updated_at(self) -> str:
        return self._updated_at


if __name__ == '__main__':
    menu = TaskTrackerMenu()
    menu.show_menu()
