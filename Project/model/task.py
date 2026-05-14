class Task:
    def __init__(self,task_id=0,project_id=0,task_name="",assigned_to="",due_date="",task_status="PENDING"):
        self.task_id=task_id
        self.project_id=project_id
        self.task_name=task_name
        self.assigned_to=assigned_to
        self.due_date=due_date
        self.task_status=task_status

    def __str__(self):
        return f"{self.task_id}, {self.project_id}, {self.task_name}, {self.assigned_to}, {self.due_date}, {self.task_status}"