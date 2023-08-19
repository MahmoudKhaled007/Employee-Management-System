from flask import Flask, render_template, url_for, request

from flask_mysqldb import MySQL

import DAO

# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, we are telling Flask to use the current module as the starting
# point for the application.
app = Flask(__name__)


#!Employees
@app.route("/employee")
def get_employees():
    EmployeeDAO = DAO.EmployeeDAO()

    records2, column_names = EmployeeDAO.get_all_employees()
    return render_template("employee.html", records=records2, column_names=column_names)


@app.route("/employee/", methods=["POST", "GET"])
def get_emp_by_id():
    """
    The function `get_emp_by_id` retrieves employee records by their ID and returns them as a list.
    :return: either the result of calling the `get_employees()` function or the result of rendering the
    "employee.html" template with the appropriate data.
    """
    if request.method == "POST":
        records_list = []
        EmployeeDAO = DAO.EmployeeDAO()
        emp_id = request.form.get("input_pr_id")
        records, column_names = EmployeeDAO.get_emp_by_id(str(emp_id))
        print("before if", records)
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)
        else:
            # Handle the case when record is not found
            return render_template(
                "employee.html", column_names=column_names, records=[], len_rec=0
            )
        return render_template(
            "employee.html",
            column_names=column_names,
            records=records_list,
            len_rec=len_rec,
        )
    else:
        return get_employees()


@app.route("/insert_employee", methods=["GET", "POST"])
def insert_employee():
    if request.method == "POST":
        # Retrieve form data
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        location = request.form.get("location")
        phone1 = request.form.get("phone1")
        sex = request.form.get("sex")
        email = request.form.get("email")
        password = request.form.get("password")

        # Create an Employee object

        # Create an instance of the DepartmentDAO and insert the employee
        employee = DAO.EmployeeDAO()

        last_inserted_id = employee.insert_emp(
            fname=fname,
            lname=lname,
            location=location,
            phone1=phone1,
            sex=sex,
            email=email,
            password=password,
        )

        return f"Employee inserted. Last inserted ID: {last_inserted_id}"

    return render_template("insert_employee.html")


#!Departments
@app.route("/department")
def get_departments():
    """
    The function `get_departments` retrieves all departments from the database and renders them in a
    template called "department.html".
    :return: a rendered HTML template called "department.html" with the variables "records" and
    "column_names" passed as arguments.
    """
    department = DAO.DepartmentDAO()
    records2, column_names = department.get_all_departments()
    return render_template(
        "department.html", records=records2, column_names=column_names
    )


@app.route("/department/", methods=["POST", "GET"])
def get_dep_by_id():
    """
    The function `get_dep_by_id` retrieves a department record by its ID and returns it as a list of
    records along with the column names.
    :return: either the result of calling the `get_departments()` function or rendering a template with
    the column names, records, and length of records.
    """
    if request.method == "POST":
        records_list = []
        department = DAO.DepartmentDAO()
        dep_id = request.form.get("input_pr_id")
        records, column_names = department.get_dep_by_id(str(dep_id))
        print("before if", records)
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)
            print("len", records_list)
            for rec in records:
                print(rec)
        else:
            # Handle the case when record is not found
            return render_template(
                "department.html", column_names=column_names, records=[], len_rec=0
            )
        return render_template(
            "department.html",
            column_names=column_names,
            records=records_list,
            len_rec=len_rec,
        )
    else:
        return get_departments()


#!Leave
@app.route("/leave")
def get_leaves():
    """
    The function `get_leaves` retrieves all leave records from the LeaveDAO and renders them in a
    leave.html template.
    :return: a rendered HTML template called "leave.html" with the variables "records" and
    "column_names" passed as arguments.
    """
    leave = DAO.LeaveDAO()
    records2, column_names = leave.get_all_leaves()
    return render_template("leave.html", records=records2, column_names=column_names)


@app.route("/leave/", methods=["POST", "GET"])
def get_leave_by_id():
    """
    The function `get_leave_by_id` retrieves leave records by their ID and returns them as a list.
    :return: a rendered template with the column names, records, and length of records.
    """
    if request.method == "POST":
        records_list = []
        leave = DAO.LeaveDAO()
        leave_id = request.form.get("input_pr_id")
        records, column_names = leave.get_leave_by_id(str(leave_id))
        print("before if", records)
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)
            print("len", records_list)
            for rec in records:
                print(rec)
        else:
            # Handle the case when record is not found
            return render_template(
                "leave.html", column_names=column_names, records=[], len_rec=0
            )
        return render_template(
            "leave.html",
            column_names=column_names,
            records=records_list,
            len_rec=len_rec,
        )
    else:
        return get_leaves()


#!Salary
@app.route("/salary")
def get_salaries():
    """
    The function `get_salaries` retrieves all salary records from the SalaryDAO and renders them in a
    template called "salary.html".
    :return: a rendered template called "salary.html" with the variables "records" and "column_names"
    passed as arguments.
    """
    salary = DAO.SalaryDAO()
    records2, column_names = salary.get_all_salary()
    return render_template("salary.html", records=records2, column_names=column_names)


@app.route("/salary/", methods=["POST", "GET"])
def get_salary_by_id():
    """
    The function `get_salary_by_id` retrieves salary records by ID and returns them as a list, along
    with the column names and the length of the records.
    :return: either the result of calling the "get_salaries" function or the result of rendering the
    "salary.html" template with the appropriate data.
    """
    if request.method == "POST":
        records_list = []
        salary = DAO.SalaryDAO()
        salary_id = request.form.get("input_pr_id")
        records, column_names = salary.get_salary_by_id(str(salary_id))
        print("before if", records)
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)
            print("len", records_list)
            for rec in records:
                print(rec)
        else:
            # Handle the case when record is not found
            return render_template(
                "salary.html", column_names=column_names, records=[], len_rec=0
            )
        return render_template(
            "salary.html",
            column_names=column_names,
            records=records_list,
            len_rec=len_rec,
        )
    else:
        return get_salaries()


#!Payroll
@app.route("/payroll")
def get_payrolls():
    """
    The function `get_payrolls` retrieves all payroll records from the database and renders them in a
    payroll template.
    :return: a rendered template called "payroll.html" with the variables "records" and "column_names"
    passed as arguments.
    """
    payroll = DAO.PayrollDAO()
    records2, column_names = payroll.get_all_payroll()
    return render_template("payroll.html", records=records2, column_names=column_names)


@app.route("/payroll/", methods=["POST", "GET"])
def get_payroll_by_id():
    """
    The function `get_payroll_by_id` retrieves payroll records by their ID and returns them as a list.
    :return: either the result of the `get_payrolls()` function or the result of rendering a template
    with the `column_names`, `records_list`, and `len_rec` variables.
    """
    if request.method == "POST":
        records_list = []
        payroll = DAO.PayrollDAO()
        payroll_id = request.form.get("input_pr_id")
        records, column_names = payroll.get_payroll_by_id(str(payroll_id))
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)
            print("len", records_list)
            for rec in records:
                print(rec)
        else:
            # Handle the case when record is not found
            return render_template(
                "payroll.html", column_names=column_names, records=[], len_rec=0
            )
        return render_template(
            "payroll.html",
            column_names=column_names,
            records=records_list,
            len_rec=len_rec,
        )
    else:
        return get_payrolls()


# The `if __name__ == '__main__':` block is used to ensure that the code inside it is only executed
# when the script is run directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    app.run(debug=True)
