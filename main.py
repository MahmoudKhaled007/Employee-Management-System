import DAO

# Employee
EmployeeDAO = DAO.EmployeeDAO()

# # Retrieve a user by ID
# user = EmployeeDAO.get_emp_by_id(1)
# if user:
#     print(f"User: ID={user.emp_id}, Name={user.fname}, Email={user.email}")
# else:
#     print("User not found.")


# INSERT EMPLOYEEE
# emp_dao = DAO.EmployeeDAO()
# emp1 = DAO.Employee(
#     None, "eee", "Mohamed", "New Cairo", "01065216622", "M", "zidan@gmail.com", "123"
# )
# emp2 = DAO.Employee(
#     None, "qqq", "Doe", "London", "0123456789", "M", "john.doe@gmail.com", "456"
# )

# employees = [emp1,emp2]

# last_row_id = emp_dao.insert_emp(employees)

# print(last_row_id)
# emp_dao.get_all_employees()
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
# # UPDATEEEEE
# # dep2 = DAO.Department(8, "Data Engineering", "20000-25000", "Updated from python4")
# departments = ["1", "2", "3"]
# last_row_id = dep_obj.insert_dep(departments)

# x = dep_obj.update_dep(departments, name="Kwrgsssssssss", description="from KWRGS")
# print(x)
# dep_obj.get_all_departments()

# # Insert into KWRGS
# dep1 = DAO.Department(5, "Data Science", "20000-25000", "Updated from python2")
# !Insert into dep

# last_row_id = dep_obj.insert_dep(
#     name="Software Engineer", salary_range="1000-5000", description="Software Engineer"
# )
# dep_obj.get_all_departments()
# # DELETEEE
# # dep_obj.get_all_departments()
# x = ["11", "10"]
# dep_obj.delete_dep(x)


##################LEave

leave = DAO.LeaveDAO()
# x = leave.get_leave_by_id("2")
# print(x)


# Insert Leave
# Employee_emp_id
#! Insert into KWRGS

# last_row_id = leave.insert_leave(
#     Employee_emp_id=2, date="2023-02-23", status="Sick", reason="Sick"
# )
# print(last_row_id)
leave.get_all_leaves()
#! Update Leave
leaves = ["1", "2"]
x = leave.update_leave(leaves, reason="ssssssss", status="from KWRGS")
print(x)
leave.get_all_leaves()

leave.delete_leave(leaves[0])
leave.get_all_leaves()

# dep_obj.get_all_departments()
# leave.update_leave()
