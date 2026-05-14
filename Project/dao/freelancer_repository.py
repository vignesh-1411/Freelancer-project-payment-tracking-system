from abc import ABC,abstractmethod

from model.client import Client
from model.freelancer import Freelancer
from model.payment import Payment
from model.project import Project
from model.task import Task

class FreelancerRepository(ABC):
    
    @abstractmethod
    def add_freelancer(self,freelancer:Freelancer) -> bool:
        pass
    
    @abstractmethod
    def update_freelancer(self,freelancer:Freelancer) -> bool:
        pass
    
    @abstractmethod
    def delete_freelancer(self,freelancer_id:int) -> bool:
        pass

    @abstractmethod
    def get_freelancer_by_id(self,freelancer_id:int) -> Freelancer:
        pass

    @abstractmethod
    def add_client(self,client:Client) -> bool:
        pass
    
    @abstractmethod
    def update_client(self,client:Client) -> bool:
        pass
    
    @abstractmethod
    def delete_client(self,client_id:int) -> bool:
        pass

    @abstractmethod
    def get_freelancer_by_id(self,freelancer_id:int) -> Freelancer:
        pass
    
