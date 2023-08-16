import DAO

EmployeeDAO = DAO.EmployeeDAO()

# Retrieve a user by ID
user = EmployeeDAO.get_emp_by_id(100)
if user:
    print(f"User: ID={user.emp_id}, Name={user.fname}, Email={user.email}")
else:
    print("User not found.")
