class Task:
    def __init__(self,task_id=None,project_id=None,task_name=None,assigned_to=None,due_date=None,task_status="PENDING"):
        self.task_id=task_id
        self.project_id=project_id
        self.task_name=task_name
        self.assigned_to=assigned_to
        self.due_date=due_date
        self.task_status=task_status

    def __str__(self):
        return f"{self.task_id}, {self.project_id}, {self.task_name}, {self.assigned_to}, {self.due_date}, {self.task_status}"