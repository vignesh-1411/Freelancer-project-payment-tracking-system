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

    def add_client(self)
        



    

if __name__ == '__main__':
    setup_database()
    # app = FreelancerApp()
    # app.run()
