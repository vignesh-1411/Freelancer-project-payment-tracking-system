class Freelancer:
    def __init__(self,freelancer_id=None,name=None,email=None,phone=None,skills=None,experience_years=None):
        self.freelancer_id=freelancer_id
        self.name=name
        self.email=email
        self.phone=phone
        self.skills=skills
        self.experience_years=experience_years

    def __str__(self):
        return f"{self.freelancer_id} {self.name}"