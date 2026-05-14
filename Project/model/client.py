class Client:
    def __init__(self,client_id=0,name="",email="",phone="",company="",address=""):
        self.client_id=client_id
        self.name=name
        self.email=email
        self.phone=phone
        self.company=company
        self.address=address

    def __str__(self):
        return f"ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Company: {self.company}, Address: {self.address}"