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
#---------------------------------------------------------------------------------------
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
    def get_client_by_id(self,client_id:int) -> Client:
        pass
#-----------------------------------------------------------------------------------------

    @abstractmethod
    def create_project(self,project:Project) -> bool:
        pass
    @abstractmethod
    def update_project_status(self, project_id:int, status:str) -> bool:
        pass
    @abstractmethod
    def get_projects_by_freelancer(self,freelancer_id:int):#------------------
        pass
    @abstractmethod
    #-----------------------no need----------------
    def get_projects_by_clients(self,client_id:int):#-------------------
        pass

#----------------------------------------------------------------------------------

    @abstractmethod
    def add_task(self,task:Task) -> bool:
        pass
        #---------------------update task status-----------------
    @abstractmethod
    def update_task_status(self,task_id:int,task_status:str) -> bool:
        pass

    @abstractmethod
    def get_tasks_by_project(self,project_id:int):#-------------------------
        pass
        
    @abstractmethod
    def process_payment(self,payment:Payment) -> bool:
        pass
        #----------------------------get payment by project
    
    @abstractmethod
    def get_payment_by_project(self,project_id:int):#----------------------
        pass
    
    @abstractmethod
    def get_all_payments(self):
        pass
    
