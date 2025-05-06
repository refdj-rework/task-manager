class TaskModel:
    def __init__(self):
        self.in_progress = []
        self.sucses = []
        self.load_tasks()

    def load_tasks(self):
        try:
            with open("list_inprgrss.txt", "r") as f:
                self.in_progress = f.read().splitlines()
        except FileNotFoundError:
            self.in_progress = []
        try:
            with open("list_sucsess.txt", "r") as f:
                self.sucses = f.read().splitlines()
        except FileNotFoundError:
            self.sucses = []

    def save_tasks(self):
        with open("list_inprgrss.txt", "w+") as f:
            for task in self.in_progress:
                f.write(task + "\n")
        with open("list_sucsess.txt", "w+") as f:
            for task in self.sucses:
                f.write(task + "\n")

    def clear_tasks(self):
        self.in_progress = []
        self.sucses = []
        with open("list_inprgrss.txt", "w+") as f:
            f.write("")
        with open("list_sucsess.txt", "w+") as f:
            f.write("")

    def add_in_progress(self, task):
        self.in_progress.append(task)

    def remove_in_progress(self, task):
        if task in self.in_progress:
            self.in_progress.remove(task)

    def add_success(self, task):
        self.sucses.append(task)
