
class FreelancerApp:

    def __init__(self):
        self.repo = FreelancerRepositoryImpl()

#Write your code here

if __name__ == '__main__':
    app = FreelancerApp()
    app.run()
