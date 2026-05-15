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
            phone=

    

if __name__ == '__main__':
    setup_database()
    # app = FreelancerApp()
    # app.run()
