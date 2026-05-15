from dao.freelancer_repository import FreelancerRepository
from model.freelancer import Freelancer
from model.client import Client
from model.payment import Payment
from model.project import Project
from model.task import Task
from util.db_connection import DBConnection 
from exception.client_not_found_exception import ClientNotFoundException 
from exception.freelancer_not_found_exception import FreelancerNotFoundException
from exception.invalid_payment_exception import InvalidPaymentException
from exception.project_closure_exception  import ProjectClosureException


class FreelancerRepositoryImpl(FreelancerRepository):
    def __init__(self):
        self.conn=DBConnection.get_connection()
        self.cursor=self.conn.cursor()

    def add_freelancer(self,freelancer:Freelancer) -> bool:
        try:
            self.cursor.execute(
                "insert into Freelancers (name,email,phone,skills,experience_years) values (?,?,?,?,?)",
                (freelancer.name,freelancer.email,freelancer.phone,freelancer.skills,freelancer.experience_years)
            )
            self.conn.commit()
            return True
        except Exception:
            return False

    def update_freelancer(self,freelancer:Freelancer) -> bool:
        self.get_freelancer_by_id(freelancer.freelancer_id)
        self.cursor.execute(
            "update Freelancers set name=?, email=?, phone=?, skills=?, experience_years=? where freelancer_id=?",
            (freelancer.name,freelancer.email,freelancer.phone,freelancer.skills,freelancer.experience_years,freelancer.freelancer_id)

        )
        self.conn.commit()
        return True

    def delete_freelancer(self,freelancer_id:int) -> bool:
        self.get_freelancer_by_id(freelancer_id)
        self.cursor.execute(
            "delete from Freelancers where freelancer_id=?",
            (freelancer_id,)
        )
        self.conn.commit()
        return True

    def get_freelancer_by_id(self,freelancer_id:int) -> Freelancer:
        self.cursor.execute(
            "select * from Freelancers where freelancer_id=?",
            (freelancer_id,)
        )
        row=sel