import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

import pytest
from dao.freelancer_repository_impl import FreelancerRepositoryImpl
from model.freelancer import Freelancer
from model.client import Client
from model.project import Project
from model.task import Task
from model.payment import Payment
from exception.freelancer_not_found_exception import FreelancerNotFoundException
from exception.client_not_found_exception import ClientNotFoundException
from exception.invalid_payment_exception import InvalidPaymentException
from exception.project_closure_exception import ProjectClosureException

# ----------------------- Directory & File Existence Tests (18) ----------------------- #

PROJECT_PATH = "."

# --- Directory Existence Tests (4) ---
def test_model_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "model")), "Directory model is missing!"

def test_dao_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "dao")), "Directory dao is missing!"

def test_exception_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "exception")), "Directory exception is missing!"

def test_util_folder_exists():
    assert os.path.isdir(os.path.join(PROJECT_PATH, "util")), "Directory util is missing!"

# --- Model File Existence Tests (5) ---
def test_freelancer_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "freelancer.py")), "File freelancer.py is missing!"

def test_client_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "client.py")), "File client.py is missing!"

def test_project_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "project.py")), "File project.py is missing!"

def test_task_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "task.py")), "File task.py is missing!"

def test_payment_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "model", "payment.py")), "File payment.py is missing!"

# --- DAO File Existence Tests (2) ---
def test_freelancer_repository_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "dao", "freelancer_repository.py")), "File freelancer_repository.py is missing!"

def test_freelancer_repository_impl_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "dao", "freelancer_repository_impl.py")), "File freelancer_repository_impl.py is missing!"

# --- Exception File Existence Tests (4) ---
def test_freelancer_not_found_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "freelancer_not_found_exception.py"))

def test_client_not_found_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "client_not_found_exception.py"))

def test_invalid_payment_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "invalid_payment_exception.py"))

def test_project_closure_exception_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "exception", "project_closure_exception.py"))

# --- Util File Existence Test (1) ---
def test_db_util_file_exists():
    assert os.path.isfile(os.path.join(PROJECT_PATH, "util", "db_connection.py")), "File db_connection.py is missing!"


# ---------------------------- Functional Tests (22) ---------------------------- #

@pytest.fixture(scope="function", autouse=True)
def setup_and_teardown():
    repo = FreelancerRepositoryImpl()
    # Cleanup in correct dependency order
    repo.cursor.execute("DELETE FROM Payments")
    repo.cursor.execute("DELETE FROM Tasks")
    repo.cursor.execute("DELETE FROM Projects")
    repo.cursor.execute("DELETE FROM Freelancers")
    repo.cursor.execute("DELETE FROM Clients")
    repo.conn.commit()
    yield repo
    repo.close()

# --- FREELANCER TESTS (5) ---
def test_add_freelancer(setup_and_teardown):
    repo = setup_and_teardown
    f = Freelancer(name="Alice", email="alice@mail.com", phone="9876543210", skills="Python", experience_years=3)
    assert repo.add_freelancer(f) == True

def test_get_freelancer_by_id_success(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="Bob"))
    repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    assert repo.get_freelancer_by_id(fid).name == "Bob"

def test_get_freelancer_not_found(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(FreelancerNotFoundException):
        repo.get_freelancer_by_id(9999)

def test_update_freelancer(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="OldFreelancer"))
    repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    assert repo.update_freelancer(Freelancer(fid, "NewFreelancer", "new@mail.com", "111", "Java", 5)) == True

def test_delete_freelancer(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="TempFreelancer"))
    repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    assert repo.delete_freelancer(fid) == True

# --- CLIENT TESTS (5) ---
def test_add_client(setup_and_teardown):
    repo = setup_and_teardown
    c = Client(name="TechCorp", email="corp@mail.com", phone="1234567890", company="TechCorp Ltd", address="123 St")
    assert repo.add_client(c) == True

def test_get_client_by_id_success(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_client(Client(name="Carol"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.get_client_by_id(cid).name == "Carol"

def test_get_client_not_found(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises(ClientNotFoundException):
        repo.get_client_by_id(8888)

def test_update_client(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_client(Client(name="OldClient"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.update_client(Client(cid, "NewClient", "new@corp.com", "999", "NewCo", "456 Ave")) == True

def test_delete_client(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_client(Client(name="TempClient"))
    repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    assert repo.delete_client(cid) == True

# --- PROJECT TESTS (4) ---
def test_create_project_success(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="F1")); repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    repo.add_client(Client(name="C1")); repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    p = Project(client_id=cid, freelancer_id=fid, project_name="Website", description="Build site", deadline="2025-12-01")
    assert repo.create_project(p) == True

def test_create_project_invalid_client(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="F2")); repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    with pytest.raises(ClientNotFoundException):
        repo.create_project(Project(client_id=99999, freelancer_id=fid, project_name="App"))

def test_get_projects_by_freelancer(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_freelancer(Freelancer(name="F3")); repo.cursor.execute("SELECT @@IDENTITY"); fid = repo.cursor.fetchone()[0]
    assert isinstance(repo.get_projects_by_freelancer(fid), list)

def test_update_project_status_method_exists(setup_and_teardown):
    repo = setup_and_teardown
    assert hasattr(repo, 'update_project_status')



def test_add_task_empty_name(setup_and_teardown):
    repo = setup_and_teardown
    # task_name empty should raise ProjectClosureException or ValueError from model/dao
    with pytest.raises((ProjectClosureException, ValueError)):
        task = Task(project_id=1, task_name="", assigned_to="Alice", due_date="2025-11-01", task_status="PENDING")
        repo.add_task(task)

def test_get_tasks_by_project_type(setup_and_teardown):
    repo = setup_and_teardown
    assert isinstance(repo.get_tasks_by_project(1), list)

def test_task_model_str(setup_and_teardown):
    t = Task(1, 1, "Fix Bug", "Dev", "2025-10-01", "IN PROGRESS")
    assert "Fix Bug" in str(t)

# --- PAYMENT TESTS (4) ---
def test_process_payment_invalid_amount(setup_and_teardown):
    repo = setup_and_teardown
    with pytest.raises((InvalidPaymentException, ValueError)):
        payment = Payment(project_id=1, client_id=1, amount=-50.0, payment_date="2025-10-01", payment_status="PAID")
        repo.process_payment(payment)

def test_process_payment_invalid_project(setup_and_teardown):
    repo = setup_and_teardown
    repo.add_client(Client(name="PayClient")); repo.cursor.execute("SELECT @@IDENTITY"); cid = repo.cursor.fetchone()[0]
    with pytest.raises(ProjectClosureException):
        repo.process_payment(Payment(project_id=99999, client_id=cid, amount=500.0, payment_date="2025-10-01", payment_status="PAID"))

def test_get_all_payments_type(setup_and_teardown):
    repo = setup_and_teardown
    assert isinstance(repo.get_all_payments(), list)



if __name__ == "__main__":
    pytest.main(["-v", "tests.py"])