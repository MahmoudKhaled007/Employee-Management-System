import mysql.connector


class Employee:
    def __init__(
        self,
        emp_id=None,
        fname=None,
        lname=None,
        location=None,
        phone1=None,
        sex=None,
        email=None,
        password=None,
    ):
        self.emp_id = emp_id
        self.fname = fname
        self.lname = lname
        self.location = location
        self.phone1 = phone1
        self.sex = sex
        self.email = email
        self.password = password


class EmployeeDAO:
    """
    _summary_
    This class for to represent Database Tables and provides the encapsulation of the database-specific code,
    that is, it is isolated from the main program.
    To achieve principle of Separation of Logic and it make it easy when testing
    """

    def __init__(self):
        """_summary_
        When the class being called every time will open a new connection to the database
        """
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mahmoud2001",
            database="employee_managment_system",
        )
        self.cursor = self.connection.cursor(buffered=True)

    def get_all_employees(self):
        """
            Select Statement to retrieve all data for the employees
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT emp_id,fname,lname,location,phone1,sex,email,pass FROM employee"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        [print(i) for i in result]
        return result

    def get_emp_by_id(self, emp_id):
        """
            Select Statement to retrieve all data for the employees based on their id
        Args:
            emp_id (_type_): _description_
                emp_id (int): id of employee needs to retrieve
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT emp_id,fname,lname,location,phone1,sex,email,pass FROM employee WHERE emp_id = %s"
        self.cursor.execute(query, (emp_id,))
        result = self.cursor.fetchone()
        if result:
            emp_id, fname, lname, location, phone1, sex, email, password = result
            employee = Employee(
                emp_id, fname, lname, location, phone1, sex, email, password
            )
            return employee
        else:
            return None

    def insert_emp(self, employees):
        """Insert multiple records to the Employee table

        Args:
            employees (list): List of Employee objects

        Returns:
            int: The last inserted row ID
        """
        query = "INSERT INTO employee (fname, lname, location, phone1, sex, email, pass) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        values = [
            (
                emp.fname,
                emp.lname,
                emp.location,
                emp.phone1,
                emp.sex,
                emp.email,
                emp.password,
            )
            for emp in employees
        ]
        self.cursor.executemany(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def update_emp(self, employees):
        """Update  multiple records to the Employee table

        Args:
            employees (list): List of Employee objects

        Returns:
            int: Number of rows affected
        """
        query = "UPDATE employee SET fname=%s, lname=%s, location=%s, phone1=%s, sex=%s, email=%s, pass=%s WHERE emp_id = %s"
        values = [
            (
                emp.fname,
                emp.lname,
                emp.location,
                emp.phone1,
                emp.sex,
                emp.email,
                emp.password,
                emp.emp_id,
            )
            for emp in employees
        ]
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

    def delete_emp(self, emp_id):
        """Delete  one record to the Employee table

        Args:
            emp_id (int): Id of employee mustn't be a foreign key in another table

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM employee WHERE emp_id = %s"
        self.cursor.execute(query, (emp_id,))
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

