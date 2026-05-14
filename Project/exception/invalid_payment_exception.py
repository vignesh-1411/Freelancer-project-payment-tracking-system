class InvalidPaymentException(Exception):
    def __init__(self,message="Invalid Payment"):
        super().__init__(message)
        