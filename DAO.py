import mysql.connector


class Employee:
    def __init__(self, emp_id, fname, lname, location, phone1, sex, email, password):
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
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="mahmoud2001",
            database="employee_managment_system",
        )
        self.cursor = self.connection.cursor(buffered=True)

    def get_emp_by_id(self, emp_id):
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

    def insert_emp(self, emp):
        """_summary_
        Insert one record to the Employee table

        Args:
            emp (_type_): _description_
            object or instance  of Employee class
        Returns:
            _type_: _description_
            last_row_id  which is INT
        """
        query = "INSERT INTO employee (fname, lname, location, phone1, sex, email, pass) VALUES (%s, %s,%s, %s,%s, %s,%s)"
        values = (
            emp.fname,
            emp.lname,
            emp.location,
            emp.phone1,
            emp.sex,
            emp.email,
            emp.password,
        )
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def update_user(self, user):
        query = "UPDATE users SET name = %s, email = %s WHERE id = %s"
        values = (user.name, user.email, user.id)
        self.cursor.execute(query, values)
        self.connection.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.connection.commit()
