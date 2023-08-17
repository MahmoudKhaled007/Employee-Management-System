import DAO

EmployeeDAO = DAO.EmployeeDAO()

# Retrieve a user by ID
user = EmployeeDAO.get_emp_by_id(1)
if user:
    print(f"User: ID={user.emp_id}, Name={user.fname}, Email={user.email}")
else:
    print("User not found.")

# emp_dao = DAO.EmployeeDAO()  # Create an instance of the EmployeeDAO class
# emp = DAO.Employee(
#     None, "Zidan", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
# )
# print(emp_dao.insert_emp(emp))

emp_dao = DAO.EmployeeDAO()
emp1 = DAO.Employee(
    2, "eee", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
)
emp2 = DAO.Employee(
    1, "qqq", "Doe", "London", "0123456789", "M", "john.doe@gmail.com", "456"
)

employees = [emp1, emp2]

# # last_row_id = emp_dao.insert_emp(employees)

# # print(last_row_id)
# print(emp2.emp_id)
# x = emp_dao.update_emp(employees)
# print(x)

empids = [4, 5, 6]
# emp_dao.delete_emp(6)
emp_dao.get_all_employees()
