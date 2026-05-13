class Client:
    def __init__(self,client_id=None,name=None,email=None,phone=None,company=None,address=None):
        self.client_id=client_id
        self.name=name
        self.email=email
        self.phone=phone
        self.company=company
        self.address=address

    def __str__(self):
        return f"ID: {self.client_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Company: {self.company}, Address: {self.address}"