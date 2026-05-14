class FreelancerNotFoundException(Exception):
    def __init__(self,message="Freelancer not found"):
        super().__init__(message)