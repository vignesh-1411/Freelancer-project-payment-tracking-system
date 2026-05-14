from util.db_connection import DBConnection

def setup_database():
    conn=DBConnection.get_connection()
    cursor=conn.cursor()

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Freelancers' AND xtype='U')
        CREATE TABLE Freelancers(
            freelancer_id INT PRIMARY KEY IDENTITY(1,1),
            name VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(20),
            skills VARCHAR(200),
            experience_years INT
        )
    """)

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Clients' AND xtype='U')
        CREATE TABLE Clients(
            client_id INT PRIMARY KEY IDENTITY(1,1),
            name VARCHAR(100),
            email VARCHAR(100),
            phone VARCHAR(20),
            company VARCHAR(100),
            address VARCHAR(200)
        )
    """)

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Projects' AND xtype='U')
        CREATE TABLE Projects(
            project_id INT PRIMARY KEY IDENTITY(1,1),
            client_id INT FOREIGN KEY REFERENCES Clients(client_id),
            freelancer_id INT FOREIGN KEY REFERENCES Freelancers(freelancer_id),
            project_name VARCHAR(100),
            description VARCHAR(300),
            deadline VARCHAR(50),
            status VARCHAR(20) DEFAULT 'OPEN'
        )
    """)   

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Tasks' AND xtype='U')
        CREATE TABLE Tasks(
            task_id INT PRIMARY KEY IDENTITY(1,1),
            project_id INT FOREIGN KEY REFERENCES Projects(project_id),
            task_name VARCHAR(100),
            assigned_to VARCHAR(100),
            due_date VARCHAR(50),
            task_status VARCHAR(20) DEFAULT 'OPEN'
        )
    """)

    cursor.execute("""
        IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='Payments' AND xtype='U')
        CREATE TABLE Payments(
            payment_id INT PRIMARY KEY IDENTITY(1,1),
            project_id INT FOREIGN KEY REFERENCES Projects(project_id),
            client_id INT FOREIGN KEY REFERENCES Clients(client_id),
            amount DECIMAL(10,2),
            payment_date VARCHAR(50),
            payment_status VARCHAR(20) DEFAULT 'OPEN'
        )
    """)

    conn.commit()
    cursor.close()