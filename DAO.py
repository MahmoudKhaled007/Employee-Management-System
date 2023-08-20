import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


# ! NOTES
""""
# ! I am using VALUES in SQL queries to prevent SQL injection
# !I am using **Kwrgs to make function dynamic and take inputs and to not make the function or the query long
#! when it comes to mandatory fields with **kwrgs i handled it with if condtions and raising a Type Error
#! DAO is for Data Access Object Design Pattern
#! he DAO pattern typically involves creating a set of classes or objects that encapsulate the database operations, such as CRUD (Create, Read, Update, Delete) operations. The DAO acts as an intermediary between the application and the database, providing methods or functions to interact with the data.

# !Here are some key characteristics and benefits of using the DAO pattern in Python:
#
#! 1. Encapsulation: The DAO encapsulates the database operations, abstracting away the complexities of the underlying database system. This allows the application code to focus on the business logic without worrying about the database details.
#
# !2. Separation of Concerns: The DAO pattern separates the database operations from the application logic, promoting a cleaner and more maintainable codebase. It ensures that the business logic remains independent of specific database implementations.
#
# !3. Reusability: By encapsulating the database operations within DAO classes or objects, the code becomes more reusable. The same set of DAO methods can be used across different parts of the application, promoting code reuse and reducing duplication.
#
# !4. Testability: The DAO pattern facilitates easier unit testing of the application logic by allowing the creation of mock or stub DAO objects. This enables isolated testing of the business logic without the need for an actual database connection.
#
#!5. Scalability: With the DAO pattern, it becomes easier to switch or scale the database system without affecting the application code. The DAO layer acts as an abstraction, shielding the application from the underlying database changes.
#
#! In Python, the DAO pattern can be implemented using various libraries and frameworks such as SQLAlchemy, Django ORM, or by writing custom database access code using SQL queries or ORM techniques.
#
#! Overall, the DAO pattern provides a structured approach to handle database interactions in Python applications, promoting code reusability, maintainability, and testability.
"""


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
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        self.cursor = self.connection.cursor(buffered=True)

    def get_all_employees(self):
        """
            Select Statement to retrieve all data for the employees
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = (
            "SELECT emp_id,fname,lname,location,phone1,sex,email,password FROM employee"
        )
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def login(self, email, password):
        """
            Select Statement to retrieve email and password for the employees
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT email,password FROM employee WHERE email =%s and password= %s"
        self.cursor.execute(query, (email, password))
        result = self.cursor.fetchone()

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
        query = "SELECT emp_id,fname,lname,location,phone1,sex,email,password FROM employee WHERE emp_id = %s"
        self.cursor.execute(query, (emp_id,))
        result = self.cursor.fetchone()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def insert_emp(self, **kwargs):
        column_names = ", ".join(kwargs.keys())
        value_placeholders = ", ".join(["%s" for _ in kwargs.keys()])
        query = f"INSERT INTO employee ({column_names}) VALUES ({value_placeholders})"
        values = tuple(kwargs.values())
        self.cursor.execute(query, values)
        self.connection.commit()

        print("Inserted", self.cursor.lastrowid, "record")
        return self.cursor.lastrowid

    #
    def update_emp(self, employees, **kwargs):
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
        values = [tuple(list(kwargs.values()) + [emp]) for emp in employees]
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
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
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
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

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
        column_names = [desc[0] for desc in self.cursor.description]
        #
        #
        return result, column_names

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
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
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
            column_names = [desc[0] for desc in self.cursor.description]

            return result, column_names
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
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def insert_leave(self, **kwargs):
        """Insert a record into the leave table
            employee_emp_id: Foreign Key is Mandatory to add in Arguments
        Args:
            **kwargs: Key-value pairs for inserting specific columns
            employee_emp_id(String),
            date(String),
            status(String),
            reason(String)
        Returns:
            int: The last inserted row ID
        """
        if "employee_emp_id" in kwargs:
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
            leaves (list): List of leaves ids
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
            leave_ids (list): Ids of leave needs to be deleted

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM `leave` WHERE leave_id = %s"
        values = [([lea]) for lea in leave_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()

        print(self.cursor.rowcount, "record(s) affected")


class Salary:
    def __init__(
        self,
        salary_id=None,
        amount=None,
        bounes=None,
        annual=None,
        overtime=None,
        department_dep_id=None,
    ):
        self.salary_id = salary_id
        self.amount = amount
        self.bounes = bounes
        self.annual = annual
        self.overtime = overtime
        self.department_dep_id = department_dep_id


class SalaryDAO:
    """
    _summary_
    This class for to represent Database Salary Tables and provides the encapsulation of the database-specific code,
    that is, it is isolated from the main program.
    To achieve principle of Separation of Logic and it make it easy when testing
    """

    def __init__(self):
        """_summary_
        When the class being called every time will open a new connection to the database
        """
        self.connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        self.cursor = self.connection.cursor(buffered=True)

    def get_all_salary(self):
        """
            Select Statement to retrieve all data for the Leave table
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        # `` because leave is reserved keyword in python
        query = "SELECT salary_id,amount,bounes,annual,overtime,department_dep_id FROM salary"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def join_all_salary(self):
        query = """SELECT salary.salary_id, salary.amount, salary.bounes, salary.annual, salary.overtime, salary.department_dep_id,department.name
                    FROM salary
                    JOIN department ON salary.department_dep_id = department.dep_id"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]
        return result, column_names

    def get_salary_by_id(self, salary_id):
        """
            Select Statement to retrieve all data for the Salary based on their id
        Args:
            salary_id (_type_): _description_
                salary_id (int): id of salary needs to retrieve
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT salary_id,amount,bounes,annual,overtime,department_dep_id FROM salary WHERE salary_id = %s"
        self.cursor.execute(query, (salary_id,))
        result = self.cursor.fetchone()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def insert_salary(self, **kwargs):
        """Insert a record into the leave table
            department_dep_id: Foreign Key is Mandatory to add in Arguments
        Args:
            **kwargs: Key-value pairs for inserting specific columns
            department_dep_id(String),
            date(String),
            status(String),
            reason(String)
        Returns:
            int: The last inserted row ID
        """
        if "department_dep_id" in kwargs:
            column_names = ", ".join(list(kwargs.keys()))
            value_placeholders = ", ".join(["%s" for _ in kwargs.keys()])
            query = f"INSERT INTO salary ({column_names}) VALUES ({value_placeholders})"
            values = tuple(kwargs.values())
            self.cursor.execute(query, values)
            self.connection.commit()

            return self.cursor.lastrowid
        else:
            raise TypeError(
                "Missing Mandatory Foreign Key : Please add department_dep_id to the arguments"
            )

    def update_salary(self, salaries, **kwargs):
        """Update multiple records in the salary table

        Args:
            salaries (list): List of salaries objects
            **kwargs: Additional key-value pairs for updating specific columns

        Returns:
            int: Number of rows affected
        """
        # Construct the SET clause dynamically based on kwargs
        set_clause = ", ".join([f"{key}=%s" for key in kwargs.keys()])

        query = f"UPDATE salary SET {set_clause} WHERE salary_id = %s"
        values = [tuple(list(kwargs.values()) + [sal]) for sal in salaries]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()

        print(self.cursor.rowcount, "record(s) affected")

    def delete_salary(self, salary_ids):
        """Delete  records to the Leaves table

        Args:
            salary_ids (list): Ids of Salary needs to be deleted

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM salary WHERE salary_id = %s"
        values = [([sal]) for sal in salary_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()

        print(self.cursor.rowcount, "record(s) affected")


class Payroll:
    def __init__(
        self,
        payroll_id=None,
        date=None,
        report=None,
        total_amount=None,
        employee_emp_id=None,
        leave_leave_id=None,
        salary_salary_id=None,
        department_dep_id=None,
    ):
        self.payroll_id = payroll_id
        self.date = date
        self.report = report
        self.total_amount = total_amount
        self.employee_emp_id = employee_emp_id
        self.leave_leave_id = leave_leave_id
        self.salary_salary_id = salary_salary_id
        self.department_dep_id = department_dep_id


class PayrollDAO:
    """
    _summary_
    This class for to represent Database Payroll Tables and provides the encapsulation of the database-specific code,
    that is, it is isolated from the main program.
    To achieve principle of Separation of Logic and it make it easy when testing
    """

    def __init__(self):
        """_summary_
        When the class being called every time will open a new connection to the database
        """
        self.connection = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            port=os.getenv("PORT"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE"),
        )
        self.cursor = self.connection.cursor(buffered=True)

    def get_all_payroll(self):
        """
            Select Statement to retrieve all data for the payroll table
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        # `` because leave is reserved keyword in python
        query = "SELECT payroll_id,date,report,total_amount,employee_emp_id,leave_leave_id,salary_salary_id,department_dep_id FROM payroll"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def get_payroll_by_id(self, payroll_id):
        """
            Select Statement to retrieve all data for the Salary based on their id
        Args:
            salary_id (_type_): _description_
                payroll_id (int): id of payroll needs to retrieve
        Returns:
            _type_: _description_
            Object: which contains Record data
        """
        query = "SELECT payroll_id,date,report,total_amount,employee_emp_id,leave_leave_id,salary_salary_id,department_dep_id FROM payroll WHERE payroll_id = %s"
        self.cursor.execute(query, (payroll_id,))
        result = self.cursor.fetchone()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names

    def insert_payroll(self, **kwargs):
        """Insert a record into the payroll table

        Args:
            **kwargs: Key-value pairs for inserting specific columns
            department_dep_id(String): Foreign Key is Mandatory to add in Arguments
            employee_emp_id(String): Foreign Key is ! Mandatory to add in Arguments
            leave_leave_id(String): Foreign Key is Mandatory to add in Arguments
            salary_salary_id(String): Foreign Key is Mandatory to add in Arguments
        Returns:
            int: The last inserted row ID
        """

        if "department_dep_id" in kwargs:
            if "employee_emp_id" in kwargs:
                if "leave_leave_id" in kwargs:
                    if "salary_salary_id" in kwargs:
                        # Code to be executed if all conditions are met
                        column_names = ", ".join(list(kwargs.keys()))
                        value_placeholders = ", ".join(["%s" for _ in kwargs.keys()])
                        query = f"INSERT INTO payroll ({column_names}) VALUES ({value_placeholders})"
                        values = tuple(kwargs.values())
                        self.cursor.execute(query, values)
                        self.connection.commit()

                        return self.cursor.lastrowid
                    else:
                        raise TypeError(
                            "Missing Mandatory Foreign Key: Please add salary_salary_id to the arguments"
                        )
                else:
                    raise TypeError(
                        "Missing Mandatory Foreign Key: Please add leave_leave_id to the arguments"
                    )
            else:
                raise TypeError(
                    "Missing Mandatory Foreign Key: Please add employee_emp_id to the arguments"
                )
        else:
            raise TypeError(
                "Missing Mandatory Foreign Key: Please add department_dep_id to the arguments"
            )

    def update_payroll(self, payroll_ids, **kwargs):
        """Update multiple records in the salary table

        Args:
            payroll_ids (list): List of ids payrolls
            **kwargs: Additional key-value pairs for updating specific columns

        Returns:
            int: Number of rows affected
        """
        # Construct the SET clause dynamically based on kwargs
        set_clause = ", ".join([f"{key}=%s" for key in kwargs.keys()])
        query = f"UPDATE payroll SET {set_clause} WHERE payroll_id = %s"
        values = [tuple(list(kwargs.values()) + [pay]) for pay in payroll_ids]
        print(values)
        self.cursor.executemany(query, values)
        self.connection.commit()

        print(self.cursor.rowcount, "record(s) affected")

    def delete_payroll(self, payroll_ids):
        """Delete  records to the Leaves table

        Args:
            payroll_ids (list): Ids of payroll_ids needs to be deleted

        Returns:
            int: Number of rows affected
        """
        query = "DELETE FROM payroll WHERE payroll_id = %s"
        values = [([pay]) for pay in payroll_ids]
        self.cursor.executemany(query, values)
        self.connection.commit()

        print(self.cursor.rowcount, "record(s) affected")

    def join_all_payroll(self):
        """
        The function `join_all_payroll` retrieves data from multiple tables in a database and returns
        the result along with the column names.

        :return: a tuple containing two elements. The first element is the result of the SQL query
        execution, which is a list of rows retrieved from the database. Each row represents a payroll
        entry and contains various attributes such as payroll_id, date, report, total_amount,
        employee_emp_id, employee_fname, leave_leave_id, leave_status, salary_salary_id, salary_amount,
        department_dep_id,
        """
        query = """SELECT payroll.payroll_id, payroll.date, payroll.report, payroll.total_amount, 
                    employee.emp_id AS employee_emp_id,employee.fname as employee_fname,`leave`.leave_id AS leave_leave_id,`leave`.status as leave_status,  
                    salary.salary_id AS salary_salary_id,salary.amount as salary_amount, department.dep_id AS department_dep_id, department.name as department_name
                    FROM payroll
                    JOIN employee ON payroll.employee_emp_id = employee.emp_id
                    JOIN `leave` ON payroll.leave_leave_id = `leave`.leave_id
                    JOIN salary ON payroll.salary_salary_id = salary.salary_id
                    JOIN department ON payroll.department_dep_id = department.dep_id;"""
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        column_names = [desc[0] for desc in self.cursor.description]

        return result, column_names
