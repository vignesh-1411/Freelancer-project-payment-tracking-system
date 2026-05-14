class ClientNotFoundException(Exception):
    def __init__(self,message="Client not found"):
        super().__init__(message)