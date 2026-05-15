from util.db_setup import setup_database
from dao.freelancer_repository import FreelancerRepository
from dao.freelancer_repository_impl import FreelancerRepositoryImpl

class FreelancerApp:

    def __init__(self):
        # self.repo = FreelancerRepositoryImpl()

#Write your code here

if __name__ == '__main__':
    setup_database()
    app = FreelancerApp()
    app.run()
