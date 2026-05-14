class ProjectClosureException(Exception):
    def __init__(self,message="Project closure error"):
        super().__init__(message)