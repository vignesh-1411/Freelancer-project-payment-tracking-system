from util.db_setup import setup_database
class FreelancerApp:

    def __init__(self):
        self.repo = FreelancerRepositoryImpl()

#Write your code here

if __name__ == '__main__':
    setup_database()
    app = FreelancerApp()
    app.run()
