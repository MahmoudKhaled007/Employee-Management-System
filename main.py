import DAO

# Employee
# EmployeeDAO = DAO.EmployeeDAO()

# # Retrieve a user by ID
# user = EmployeeDAO.get_emp_by_id(1)
# if user:
#     print(f"User: ID={user.emp_id}, Name={user.fname}, Email={user.email}")
# else:
#     print("User not found.")

# # emp_dao = DAO.EmployeeDAO()  # Create an instance of the EmployeeDAO class
# # emp = DAO.Employee(
# #     None, "Zidan", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
# # )
# # print(emp_dao.insert_emp(emp))

emp_dao = DAO.EmployeeDAO()
emp1 = DAO.Employee(
    2, "eee", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
)
emp2 = DAO.Employee(
    1, "qqq", "Doe", "London", "0123456789", "M", "john.doe@gmail.com", "456"
)

employees = ["1", "2", "3"]

# last_row_id = emp_dao.insert_emp(employees)

# print(last_row_id)

# x = emp_dao.update_emp(employees, fname="KWRGS", lname="DONEEEE")
# print(x)
# DELETE
# emp_dao.get_all_employees()
# empids = ["18", "19"]
# emp_dao.delete_emp(empids)
# emp_dao.get_all_employees()
# #TODO Depa
dep_obj = DAO.DepartmentDAO()
# dep_obj.get_all_departments()

# de0partment = dep_obj.get_dep_by_id(2)
# if department:
#     print(department)
# else:
#     print("department not found.")

# emp1 = DAO.Employee(
#     2, "eee", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
# )
# emp2 = DAO.Employee(
#     1, "qqq", "Doe", "London", "0123456789", "M", "john.doe@gmail.com", "456"
# )

# employees = [emp1, emp2]

# # # last_row_id = emp_dao.insert_emp(employees)

# Insert into
# dep1 = DAO.Department(5, "Data Science", "20000-25000", "Updated from python2")
# UPDATEEEEE
# # dep2 = DAO.Department(8, "Data Engineering", "20000-25000", "Updated from python4")
# departments = ["1", "2", "3"]
# # last_row_id = dep_obj.insert_dep(departments)

# x = dep_obj.update_dep(departments, name="Kwrgsssssssss", description="from KWRGS")
# print(x)
# dep_obj.get_all_departments()

# Insert into KWRGS
dep1 = DAO.Department(5, "Data Science", "20000-25000", "Updated from python2")

last_row_id = dep_obj.insert_dep(
    name="INSERT_KWRGS3", salary_range="1000-5000", description="HEYYYY from KWRGS"
)
# DELETEEE
# dep_obj.get_all_departments()
x = ["11", "10"]
dep_obj.delete_dep(x)
