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
            return result
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

    def update_emp(self, employees_id, **kwargs):
        """Update multiple records in the employee table

        Args:
            employees (list): List of employees_ids
            **kwargs: Additional key-value pairs for updating specific columns

        Returns:
            int: Number of rows affected
        """
        # Construct the SET clause dynamically based on kwargs
        set_clause = ", ".join([f"{key}=%s" for key in kwargs.keys()])

        query = f"UPDATE employee SET {set_clause} WHERE emp_id = %s"
        values = [tuple(list(kwargs.values()) + [emp]) for emp in employees_id]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

    def delete_emp(self, emp_ids):
        """Delete  records to the Employee table

        Args:
            emp_ids (list): Ids of employees, mustn't be a foreign key in another table

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM employee WHERE emp_id = %s"
        values = [([emp]) for emp in emp_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")


class Department:
    def __init__(self, dep_id=None, name=None, salary_range=None, description=None):
        self.dep_id = dep_id
        self.name = name
        self.salary_range = salary_range
        self.description = description


class DepartmentDAO:
    """
    _summary_
    This class for to represent Database Department Tables and provides the encapsulation of the database-specific code,
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

    def get_all_departments(self):
        """
            Select Statement to retrieve all data for the employees
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT dep_id,name,salary_range, description FROM department"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            [print(i) for i in result]
            return result
        else:
            return None

    def get_dep_by_id(self, dep_id):
        """
            Select Statement to retrieve all data for the Departments based on their id
        Args:
            dep_id (_type_): _description_
                dep_id (int): id of employee needs to retrieve
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT dep_id,name,salary_range, description FROM department WHERE dep_id = %s"
        self.cursor.execute(query, (dep_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return None

        # def insert_dep(self):
        """Insert multiple records to the Department table

        Args:
            departments (list): List of department objects

        Returns:
            int: The last inserted row ID
        """
        query = "INSERT INTO department (dep_id,name,salary_range, description) VALUES (%s,%s, %s,%s)"
        values = [
            (
                dep.dep_id,
                dep.name,
                dep.salary_range,
                dep.description,
            )
            for dep in departments
        ]
        self.cursor.executemany(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

    def insert_dep(self, **kwargs):
        """Insert a record into the Department table

        Args:
            **kwargs: Key-value pairs for inserting specific columns

        Returns:
            int: The last inserted row ID
        """
        column_names = ", ".join(kwargs.keys())
        value_placeholders = ", ".join(["%s" for _ in kwargs.keys()])
        query = f"INSERT INTO department ({column_names}) VALUES ({value_placeholders})"
        values = tuple(kwargs.values())
        self.cursor.execute(query, values)
        self.connection.commit()
        return self.cursor.lastrowid

        # def update_dep(self, departments):
        """Update  multiple records to the Department table

        Args:
            departments (list): List of department objects

        Returns:
            int: Number of rows affected
        """
        # DONE add What valeus to update maybe we can use **kwrgs
        query = "UPDATE department SET  name=%s, salary_range=%s, description=%s WHERE dep_id = %s"
        values = [
            (dep.name, dep.salary_range, dep.description, dep.dep_id)
            for dep in departments
        ]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

    def update_dep(self, departments, **kwargs):
        """Update multiple records in the Department table

        Args:
            departments (list): List of department objects
            **kwargs: Additional key-value pairs for updating specific columns

        Returns:
            int: Number of rows affected
        """
        # Construct the SET clause dynamically based on kwargs
        set_clause = ", ".join([f"{key}=%s" for key in kwargs.keys()])

        query = f"UPDATE department SET {set_clause} WHERE dep_id = %s"
        values = [tuple(list(kwargs.values()) + [dep]) for dep in departments]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

    def delete_dep(self, dep_ids):
        """Delete  records to the Department table

        Args:
            dep_ids (list): Ids of Departments, mustn't be a foreign key in another table

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM department WHERE dep_id = %s"
        values = [([dep]) for dep in dep_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")


class Leave:
    def __init__(
        self, leave_id=None, Employee_emp_id=None, date=None, status=None, reason=None
    ):
        self.leave_id = leave_id
        self.Employee_emp_id = Employee_emp_id
        self.date = date
        self.status = status
        self.reason = reason


class LeaveDAO:
    """
    _summary_
    This class for to represent Database Leave Tables and provides the encapsulation of the database-specific code,
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

    def get_all_leaves(self):
        """
            Select Statement to retrieve all data for the Leave table
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        # `` because leave is reserved keyword in python
        query = "SELECT leave_id,Employee_emp_id,date, status,reason FROM `leave`"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        if result:
            [print(i) for i in result]
            return result
        else:
            return None

    def get_leave_by_id(self, leave_id):
        """
            Select Statement to retrieve all data for the Departments based on their id
        Args:
            dep_id (_type_): _description_
                dep_id (int): id of employee needs to retrieve
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT leave_id,Employee_emp_id,date, status,reason FROM `leave` WHERE leave_id = %s"
        self.cursor.execute(query, (leave_id,))
        result = self.cursor.fetchone()
        if result:
            return result
        else:
            return None

    def insert_leave(self, **kwargs):
        """Insert a record into the leave table
            Employee_emp_id: Foreign Key is Mandatory to add in Arguments
        Args:
            **kwargs: Key-value pairs for inserting specific columns
            Employee_emp_id(String),
            date(String),
            status(String),
            reason(String)
        Returns:
            int: The last inserted row ID
        """
        if "Employee_emp_id" in kwargs:
            column_names = ", ".join(list(kwargs.keys()))
            value_placeholders = ", ".join(["%s" for _ in kwargs.keys()])
            query = (
                f"INSERT INTO `leave` ({column_names}) VALUES ({value_placeholders})"
            )
            values = tuple(kwargs.values())
            self.cursor.execute(query, values)
            self.connection.commit()
            return self.cursor.lastrowid
        else:
            raise TypeError(
                "Missing Mandatory Foreign Key : Please add Employee_emp_id to the arguments"
            )

    def update_leave(self, leaves, **kwargs):
        """Update multiple records in the leaves table

        Args:
            leaves (list): List of leaves objects
            **kwargs: Additional key-value pairs for updating specific columns

        Returns:
            int: Number of rows affected
        """
        # Construct the SET clause dynamically based on kwargs
        set_clause = ", ".join([f"{key}=%s" for key in kwargs.keys()])

        query = f"UPDATE `leave` SET {set_clause} WHERE leave_id = %s"
        values = [tuple(list(kwargs.values()) + [lea]) for lea in leaves]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")

    def delete_leave(self, leave_ids):
        """Delete  records to the Leaves table

        Args:
            dep_ids (list): Ids of Departments, mustn't be a foreign key in another table

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM `leave` WHERE leave_id = %s"
        values = [([lea]) for lea in leave_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()
        print(self.cursor.rowcount, "record(s) affected")
