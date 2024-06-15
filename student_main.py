from datetime import date, timedelta

class Task:
    def __init__(self, title, description, due_date, status="Pending", priority="Medium", notes="", duration=1, recurrence=None, dependencies=None):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status
        self.priority = priority
        self.notes = notes
        self.duration = duration
        self.recurrence = recurrence
        self.dependencies = dependencies

    def is_due_today(self):
        return self.due_date == date.today()

class Schedule:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task_title):
        self.tasks = [task for task in self.tasks if task.title != task_title]

    def get_task(self, task_title):
        for task in self.tasks:
            if task.title == task_title:
                return task

    def list_overdue_tasks(self):
        return [task for task in self.tasks if task.due_date < date.today() and task.status != "Completed"]

    def list_tasks_due_today(self):
        return [task for task in self.tasks if task.is_due_today()]

    def sort_tasks_by_due_date(self):
        return sorted(self.tasks, key=lambda x: x.due_date)

    def update_task(self, task_title, **kwargs):
        task = self.get_task(task_title)
        if task:
            for key, value in kwargs.items():
                setattr(task, key, value)

    def weekly_schedule(self, start_date):
        end_date = start_date + timedelta(days=6)
        return [task for task in self.tasks if start_date <= task.due_date <= end_date]

    def monthly_schedule(self, year, month):
        return [task for task in self.tasks if task.due_date.year == year and task.due_date.month == month]

    def list_tasks_by_priority(self, priority):
        return [task for task in self.tasks if task.priority == priority]

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.title},{task.description},{task.due_date},{task.status},{task.priority},{task.notes},{task.duration},{task.recurrence},{task.dependencies}\n")

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            for line in f:
                task_data = line.strip().split(',')
                task = Task(title=task_data[0], description=task_data[1], due_date=date.fromisoformat(task_data[2]), status=task_data[3], priority=task_data[4], notes=task_data[5], duration=int(task_data[6]), recurrence=task_data[7], dependencies=task_data[8])
                self.add_task(task)

    def list_tasks_with_notes(self):
        return [task for task in self.tasks if task.notes]

    def mark_as_completed(self, task_title):
        task = self.get_task(task_title)
        if task:
            task.status = "Completed"

    def list_completed_tasks(self):
        return [task for task in self.tasks if task.status == "Completed"]

    def find_task_by_keyword(self, keyword):
        return [task for task in self.tasks if keyword in task.title or keyword in task.description]

    def check_deadlines(self):
        return [task for task in self.tasks if task.due_date == date.today() + timedelta(days=1)]

    def list_all_tasks(self):
        return self.tasks

    def list_tasks_by_duration(self, min_duration, max_duration):
        return [task for task in self.tasks if min_duration <= task.duration <= max_duration]

    def task_history(self):
        history = []
        for task in self.tasks:
            history.append(("added", task))
        return history

    def clear_completed_tasks(self):
        self.tasks = [task for task in self.tasks if task.status != "Completed"]

    def list_recurring_tasks(self):
        return [task for task in self.tasks if task.recurrence]

    def set_reminder(self, task_title, reminder_date):
        task = self.get_task(task_title)
        if task:
            task.reminder_date = reminder_date

    def completion_percentage(self):
        completed_tasks = len([task for task in self.tasks if task.status == "Completed"])
        total_tasks = len(self.tasks)
        return (completed_tasks / total_tasks) * 100 if total_tasks > 0 else 0

    def find_dependencies(self, task):
        dependencies = []
        for dependency_title in task.dependencies:
            dependency = self.get_task(dependency_title)
            if dependency:
                dependencies.append(dependency)
        return dependencies