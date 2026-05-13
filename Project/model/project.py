class Project:
    def __init__(self, project_id=None,client_id=None,freelancer_id=None,project_name=None,description=None,deadline=None,status="OPEN"):
        self.project_id=project_id
        self.client_id=client_id
        self.freelancer_id=freelancer_id
        self.project_name=project_name
        self.description=description
        self.deadline=deadline
        self.status=status

    def __str__(self):
        return f"{self.project_id}, {self.client_id}, {self.freelancer_id}, {self.project_name}, {self.description}, {self.deadline}, {self.status}"
        