from util.db_setup import setup_database
from dao.freelancer_repository_impl import FreelancerRepositoryImpl
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

class FreelancerApp:

    def __init__(self):
        self.repo = FreelancerRepositoryImpl()

#Write your code here

    def display_menu(self):
        print("-----------------------------FREELANCER PROJECT AND PAYMENT TRACKING SYSTEM----------------------------------")
        print("Freelancer Management------")
        print("1. Add Freelancer")
        print("2. Update Freelancer")
        print("3. Delete Freelancer")
        print("4. View Freelancer by ID")
        print("Client Management--------")
        print("5. Add Client")
        print("6. Update Client")
        print("7. Delete Client")
        print("Project Management---------")
        print("8. Create Project")
        print("9. Update Project status")
        print("10. View project by freelancer")
        print("11. View project by client")
        print("Task Management-------------")
        print("12. Add Task")
        print("13. Update Task status")
        print("14. View tasks by project")
        print("Payment Management-------------")
        print("15. Process Payment")
        print("16. View payments by project")
        print("System----------")
        print("17. View all payments")
        print("18. EXIT")

    #-------------------------------------

    def add_freelancer(self):
        print("\n-----Add Freelancer---------")
        try:
            name=input("Enter Name: ")
            email=input("Enter email: ")
            phone=input("Enter phone: ")
            skills=input("Enter skills: ")
            experience_years=int(input("Enter YOE: "))
            freelancer=Freelancer(name=name,email=email,phone=phone,skills=skills,experience_years=experience_years)
            if self.repo.add_freelancer(freelancer):
                print("Freelancer added successfully!")
            else:
                print("Failed to add Freelancer")
        except Exception as e:
            print(f"Error: {e}")

    def update_freelancer(self):
        print("\n--------Update Freelancer--------")
        try:
            freelancer_id=int(input("Enter freelancer ID to update: "))
            freelancer=self.repo.get_freelancer_by_id(freelancer_id)
            freelancer.name=input("Enter new name: ")
            freelancer.email=input("Enter new email: ")
            freelancer.phone=input("Enter new phone: ")
            freelancer.skills=input("Enter new skills: ")
            freelancer.experience_years=int(input("Enter new YOE: "))
            if self.repo.update_freelancer(freelancer):
                print("Freelancer updated successfully!")
            else:
                print("Failed to update freelancer")
        except FreelancerNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")
    
    def delete_freelancer(self):
        print("\n-----------Delete freelancer------------")
        try:
            freelancer_id=int(input("Enter freelancer ID to delete: "))
            if self.repo.delete_freelancer(freelancer_id):
                print("Freelancer deleted successfully")
            else:
                print("Failed to delete freelancer")
        except FreelancerNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_freelancer_by_id(self):
        print("\n-----------View freelancer by ID------------")
        try:
            freelancer_id=int(input("Enter freelancer ID: "))
            freelancer=self.repo.get_freelancer_by_id(freelancer_id)
            print(freelancer)
        except FreelancerNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    #----------------------CLIENT----------------------------

    def add_client(self):
        print("\n-------Add Client-------")
        try:
            name=input("Enter name: ")
            email=input("Enter email: ")
            phone=input("Enter phone: ")
            company=input("Enter company: ")
            address=input("Enter address: ")
            client=Client(name=name,email=email,phone=phone,company=company,address=address)
            if self.repo.add_client(client):
                print("Client added successfully")
            else:
                print("Failed to add client")
        except Exception as e:
            print(f"Error: {e}")

    def update_client(self):
        print("\n----------Update client---------")
        try:
            client_id=int(input("Enter client ID to update: "))
            client=self.repo.get_client_by_id(client_id)
            client.name=input("Enter new name: ")
            client.email=input("Enter new email: ")
            client.phone=input("Enter new phone: ")
            client.company=input("Enter new company: ")
            client.address=input("Enter new address: ")
            if self.repo.update_client(client):
                print("Client updated successfully!")
            else:
                print("Failed to update client")
        except ClientNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def delete_client(self):
        print("\n-----------Delete Client------------")
        try:
            client_id=int(input("Enter client ID to delete: "))
            if self.repo.delete_client(client_id):
                print("client deleted successfully")
            else:
                print("Failed to delete client")
        except ClientNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    #----------------------PROJECT---------------------------------

    def create_project(self):
        print("\n---------Create Project-----------")
        try:
            client_id=int(input("Enter client ID: "))
            freelancer_id=int(input("Enter freelancer ID: "))
            project_name=input("Enter project name: ")
            description=input("Enter description: ")
            deadline=input("Enter deadline (YYYY-MM-DD): ")
            project=Project(client_id=client_id,freelancer_id=freelancer_id,project_name=project_name,description=description,deadline=deadline)
            if self.repo.create_project(project):
                print("Project created successfully")
            else:
                print("Failed to create project")
        except ClientNotFoundException as e:
            print(e)
        except FreelancerNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")
    
    def update_project_status(self):
        print("\n--------Update project status--------")
        try:
            project_id=int(input("Enter project ID to update: "))
            print(" 1.OPEN   2.IN PROGRESS   3.COMPLETED   4.CANCELLED")
            choice=int(input("Enter choice: "))
            status_map={1:"OPEN", 2:"IN PROGRESS", 3:"COMPLETED", 4:"CANCELLED"}
            status=status_map.get(choice,"")
            if self.repo.update_project_status(project_id,status):
                print(f"Project status updated to {status} successfully!")
            else:
                print("Failed to update project status")
        except ProjectClosureException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_projects_by_freelancer(self):
        print("\n----------view projects by freelancer ID------------")
        try:
            freelancer_id=int(input("Enter freelancer ID: "))
            projects=self.repo.get_projects_by_freelancer(freelancer_id)
            if projects:
                print(f"\n Projects for freelancer id {freelancer_id}")
                print("-"*50)
                for p in projects:
                    print(f"ID={p.project_id} CLIENT ID: {p.client_id}"
                        f"Name={p.project_name} Deadline={p.deadline} Status={p.status}")
                print("-"*50)
            else:
                print("no projects found for this freelancer.")
        except FreelancerNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_projects_by_client(self):
        print("\n----------view projects by client--------------")
        try:
            client_id=int(input("Enter client ID: "))
            projects=self.repo.get_projects_by_client(client_id)
            if projects:
                print(f"\n Projects for client id {client_id}")
                print("-"*50)
                for p in projects:
                    print(f"ID={p.project_id} FREELANCER ID: {p.freelancer_id}"
                        f"Name={p.project_name} Deadline={p.deadline} Status={p.status}")
                print("-"*50)
            else:
                print("no projects found for this client.")
        except ClientNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    #--------------------------TASK---------------------
    def add_task(self):
        print("\n------------Add task-------------")
        try:
            project_id=int(input("Enter project ID: "))
            task_name=input("Enter task name: ")
            assigned_to=input("Enter assigned to: ")
            due_date=input("Enter due date (YYYY-MM-DD): ")
            print("1. PENDING   2.IN PROGRESS   3.COMPLETED     4.CANCELLED")
            choice=int(input("Enter task status choice: "))
            status_map={1:"PENDING", 2:"IN PROGRESS", 3:"COMPLETED", 4:"CANCELLED"}
            task_status=status_map.get(choice,"PENDING")
            task=Task(project_id=project_id,task_name=task_name,assigned_to=assigned_to,due_date=due_date,task_status=task_status)
            if self.repo.add_task(task):
                print("Task added successfully")
            else:
                print("Failed to add task")
        except ProjectClosureException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def update_task_status(self):
        print("\n--------Update task status----------")
        try:
            task_id=int(input("Enter task ID to update: "))
            print("1. PENDING   2.IN PROGRESS   3.COMPLETED     4.CANCELLED")
            choice=int(input("Enter task status choice: "))
            status_map={1:"PENDING", 2:"IN PROGRESS", 3:"COMPLETED", 4:"CANCELLED"}
            task_status=status_map.get(choice,"PENDING")
            if self.repo.update_task_status(task_id):
                print(f"Task status updated to {task_status} successfully!")
            else:
                print("Failed to update task status")
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_tasks_by_project(self):
        print("\n---------view tasks by project------------")
        try:
            project_id=int(input("Enter project ID: "))
            tasks=self.repo.get_tasks_by_project(project_id)
            if tasks:
                print(f"\n{'Task ID':<10}{'task name':<20}{'assigned to':<20}{'due date':<15}{'status'}")
                print("-"*50)
                for t in tasks:
                    print(f"{t.task_id:<10}{t.task_name:<20}{t.assigned_to:<20}{t.due_date:<15}{t.task_status}")
            else:
                print("No tasks found for the project")
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    #------------------------PAYMENT-------------------------------

    def process_payment(self):
        print("\n----------Process Payment------------")
        try:
            project_id=int(input("Enter project ID: "))
            client_id=int(input("Enter client ID: "))
            amount=float(input("Enter amount: "))
            payment_date=input("Enter payment date (YYYY-MM-DD): ")
            print("1. PENDING   2.PAID   3.PARTIALLY PAID     4.CANCELLED")
            choice=int(input("Enter task status choice: "))
            status_map={1:"PENDING", 2:"PAID", 3:"PARTIALLY PAID", 4:"CANCELLED"}
            payment_status=status_map.get(choice,"PENDING")
            payment=Payment(project_id=project_id,client_id=client_id,amount=amount,payment_date=payment_date,payment_status=payment_status)
            if self.repo.process_payment(payment):
                print("Payment processed successfully")
            else:
                print("Failed to process payment")
        except InvalidPaymentException as e:
            print(e)
        except ProjectClosureException as e:
            print(e)
        except ClientNotFoundException as e:
            print(e)
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_payments_by_project(self):
        print("\n-------view payments by project-----------")
        try:
            project_id=int(input("Enter project ID: "))
            payments=self.repo.get_payments_by_project(project_id)
            if payments:
                print(f"\n{'Pay ID':<10}{'Client ID':<12}{'amount':<12}{'date':<15}{'status'}")
                print("-"*50)
                for p in payments:
                    print(f"{p.payment_id:<10}{p.client_id:<12}{p.amount:<12}{p.payment_date:<15}{p.payment_status}")
            else:
                print("No payments found for the project")
        except ValueError:
            print("Invalid input format!")
        except Exception as e:
            print(f"Error: {e}")

    def view_all_payments(self):
        print("\n-----------view all payments--------------")
        try:
            payments=self.repo.get_all_payments()
            if payments:
                print(f"\n{'Pay ID':<10}{'Project ID':<12}{'Client ID':<12}{'amount':<12}{'date':<15}{'status'}")
                print("-"*50)
                for p in payments:
                    print(f"{p.payment_id:<10}{p.project_id:<12}{p.client_id:<12}{p.amount:<12}{p.payment_date:<15}{p.payment_status}")
            else:
                print("No payments found")
        except Exception as e:
            print(f"Error: {e}")

    #----------------------------------MAIN LOOP-------------------------------

    def run(self):
        while True:
            try:
                self.display_menu()
                choice=int(input("Enter your choice(1-18): "))
                if choice==1:
                    self.add_freelancer()
                elif choice==2:
                    self.update_freelancer()
                elif choice==3:
                    self.delete_freelancer()
                elif choice==4:
                    self.view_freelancer_by_id()
                elif choice==5:
                    self.add_client()
                elif choice==6:
                    self.update_client()
                elif choice==7:
                    self.delete_client()
                elif choice==8:
                    self.create_project()
                elif choice==9:
                    self.update_project_status()
                elif choice==10:
                    self.view_projects_by_freelancer()
                elihoice==11:
                    self.view_projects_by_client()
                elif choice==12:
                    self.add_task()
                elif choice==13:
                    self.update_task_status()
                elif choice==14:
                    self.view_tasks_by_project()
                elif choice==15:
                    self.process_payment()
                elif choice==16:
                    self.view_payments_by_project
                elif choice==17:
                    self.view_all_payments()
                elif choice==18:
                    print("THANK YOU FOR USING FREELANCER PROJECT AND PAYMENT TRACKING SYSTEM. GOODBYE!")
                    self.repo.close()
                    break
                else:
                    print("Invalid choice! Please try again (1-18)")
            except ValueError:
                print("Error: please enter valid number!")
            except KeyboardInterrupt:
                print("\nApplication terminated by user.")
                self.repo.close()
                break
            except Exception as e:
                print(f"Unexpected Error: {e}")
                self.repo.close()
                break
            
                
    

if __name__ == '__main__':
    setup_database()
    app = FreelancerApp()
    app.run()
