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
        row=self.cursor.fetchone()
        if row is None:
            raise FreelancerNotFoundException(f"Freelancer with ID {freelancer_id} not found")
        return Freelancer(row[0], row[1], row[2], row[3], row[4], row[5])

    #------------client methods-----------------------

    def add_client(self,client:Client) -> bool:
        try:
            self.cursor.execute(
                "insert into Clients (name,email,phone,company,address) values (?,?,?,?,?)",
                (client.name,client.email,client.phone,client.company,client.address)
            )
            self.conn.commit()
            return True
        except Exception:
            return False

    def update_client(self,client:Client) -> bool:
        self.get_client_by_id(client.client_id)
        self.cursor.execute(
            "update Clients set name=?, email=?, phone=?, company=?, address=? where client_id=?",
            (client.name,client.email,client.phone,client.company,client.address,client.client_id)
        )
        self.conn.commit()
        return True
    
    def delete_client(self,client_id:int) -> bool:
        self.get_client_by_id(client_id)
        self.cursor.execute(
            "delete from Clients where client_id=?",
            (client_id,)
        )
        self.conn.commit()
        return True

    def get_client_by_id(self,client_id:int) -> Client:
        self.cursor.execute(
            "select * from Clients where client_id=?",
            (client_id,)
        )
        row=self.cursor.fetchone()
        if row is None:
            raise ClientNotFoundException(f"Client with ID {client_id} not found")
        return Client(row[0], row[1], row[2], row[3], row[4]. row[5])

    #---------------------project methods--------------------

    def create_project(self,project:Project) -> bool:
        try:
            self.get_client_by_id(project.client_id)
            self.get_freelancer_by_id(project.freelancer_id)
            self.cursor.execute(
                "insert into Projects(client_id,freelancer_id,project_name,description,deadline,status) values (?,?,?,?,?,?)",
                (project.client_id,project.freelancer_id,project.project_name,project.description,project.deadline,project.status)
            )
            self.conn.commit()
            return True
        except (ClientNotFoundException,FreelancerNotFoundException):
            raise
        except Exception:
            return False
    
    def update_project_status(self,project_id:int,status:str) -> bool:
        valid_status=["OPEN","IN PROGRESS", "COMPLETED", "CANCELLED"]
        if status not in valid_status:
            raise ProjectClosureException(f"Invalid status '{status}'")
        self.cursor.execute(
            "update Projects set status=? where project_id=?",
            (status,project_id)
        )
        self.conn.commit()
        return True

    def get_projects_by_freelancer(self,freelancer_id:int):
        self.get_freelancer_by_id(freelancer_id)
        self.cursor.execute(
            "select * from Projects where freelancer_id=?",(freelancer_id,)
        )
        rows=self.cursor.fetchall()
        return [Project(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]

    def get_projects_by_clients(self,client_id:int):
        self.get_client_by_id(client_id)
        self.cursor.execute(
            "select * from Projects where client_id=?",(client_id,)
        )
        rows=self.cursor.fetchall()
        return [Project(r[0], r[1], r[2], r[3], r[4], r[5], r[6]) for r in rows]

    #----------------------task methods-------------------------------------------------------

    def add_task(self,task:Task) ->bool:
        try:
            if not task.task_name or task.task_name.strip()=="":
                raise ProjectClosureException("Task name must not be empty")
            if not task.assigned_to or task.assigned_to.strip()=="":
                raise ProjectClosureException("Assigned to must not be empty")
            self.cursor.execute(
                "insert into Tasks(project_id,task_name,assigned_to,due_date,task_status) values (?,?,?,?,?)",
                (task.project_id,task.task_name,task.assigned_to,task.due_date,task.task_status)
            )
            self.conn.commit()
            return True
        except ProjectClosureException:
            raise
        except Exception:
            return False

    def update_task_status(self,task_id:int,task_status:str) -> bool:
        self.cursor.execute(
            "update Tasks set task_status=? where task_id=?",(task_status,task_id)
        )
        self.conn.commit()
        return True

    def get_tasks_by_project(self,project_id:int):
        self.cursor.execute(
            "select * from Tasks where project_id=?",(project_id,)
        )
        rows=self.cursor.fetchall()
        return [Task(r[0], r[1], r[2], r[3], r[4], r[5]) for r in rows]

    #-------------------payment method-----------------------------------------------------

    def process_payment(self,payment:Payment) -> bool:
        try:
            if payment.amount<=0:
                raise InvalidPaymentException("Amount must be greater than 0")
            if not payment.payment_date or payment.payment_date.strip()=="":
                raise InvalidPaymentException("Payment date must not be empty")
            self.cursor.execute(
                "select * from Projects where project_id=?",(payment.project_id,)
            )
            if self.cursor.fetchone() is None:
                raise ProjectClosureException(f"Project with ID {payment.project_id} not found")
            self.get_client_by_id(payment.client_id)
            self.cursor.execute(
                "insert into Payments(project_id,client_id,amount,payment_date,payment_status) values (?,?,?,?,?)",
                (payment.project_id,payment.client_id,payment.amount,payment.payment_date,payment.payment_status)
            )
            self.conn.commit()
            return True
        except (InvalidPaymentException,ProjectClosureException,ClientNotFoundException):
            raise
        except Exception:
            return False
    
    def get_payments_by_project(self,project_id:int):
        self.cursor.execute(
            "select * from Payments where project_id=?",(project_id,)
        )
        rows=self.cursor.fetchall()
        return [Task(r[0], r[1], r[2], float(r[3]), r[4], r[5]) for r in rows]

    def get_all_payments(self):
        self.cursor.execute(
            "select * from Payments"
        )
        rows=self.cursor.fetchall()
        return [Task(r[0], r[1], r[2], float(r[3]), r[4], r[5]) for r in rows]


    
    def close(self):
        self.cursor.close()
        DBConnection.close_connection()


            
            