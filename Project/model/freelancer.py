class Freelancer:
    def __init__(self,freelancer_id=0,name="",email="",phone="",skills="",experience_years=0):
        self.freelancer_id=freelancer_id
        self.name=name
        self.email=email
        self.phone=phone
        self.skills=skills
        self.experience_years=experience_years

    def __str__(self):
        return f"ID: {self.freelancer_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Skills: {self.skills}, Experience Years: {self.experience_years}"