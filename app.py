from flask import Flask, render_template, url_for

from flask_mysqldb import MySQL

import DAO

# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, we are telling Flask to use the current module as the starting
# point for the application.
app = Flask(__name__)


#!Employees
@app.route("/employee")
def get_employyes():
    EmployeeDAO = DAO.EmployeeDAO()

    records2, column_names = EmployeeDAO.get_all_employees()
    return render_template(
        "employee_grid.html", records=records2, column_names=column_names
    )


#!Departments
@app.route("/department")
def get_departments():
    department = DAO.DepartmentDAO()
    records2, column_names = department.get_all_departments()
    return render_template(
        "deaprtment.html", records=records2, column_names=column_names
    )


#!Leave
@app.route("/leave")
def get_leaves():
    leave = DAO.LeaveDAO()
    records2, column_names = leave.get_all_leaves()
    return render_template("leave.html", records=records2, column_names=column_names)


#!Salary
@app.route("/salary")
def get_salaries():
    salary = DAO.SalaryDAO()
    records2, column_names = salary.get_all_salary()
    return render_template("salary.html", records=records2, column_names=column_names)


#!Payroll
@app.route("/payroll")
def get_payrolls():
    payroll = DAO.PayrollDAO()
    records2, column_names = payroll.get_all_payroll()
    return render_template("payroll.html", records=records2, column_names=column_names)


# The `if __name__ == '__main__':` block is used to ensure that the code inside it is only executed
# when the script is run directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    app.run(debug=True)
