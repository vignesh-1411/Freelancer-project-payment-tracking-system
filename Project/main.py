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
            status_map={1:"OPEN", 2:"IN PROGRESS", 3:"COMPLETED", 4."CANCELLED"}
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



        



    

if __name__ == '__main__':
    setup_database()
    # app = FreelancerApp()
    # app.run()
