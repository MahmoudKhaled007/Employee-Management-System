from flask import Flask, render_template, url_for, request, flash

from flask_mysqldb import MySQL

import DAO

# `app = Flask(__name__)` creates an instance of the Flask class and assigns it to the variable `app`.
# The `__name__` argument is a special Python variable that represents the name of the current module.
# By passing `__name__` as an argument, we are telling Flask to use the current module as the starting
# point for the application.
app = Flask(__name__)


#!Sign Up
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # Retrieve form data
        username = request.form["username"]
        password = request.form["password"]
        # Perform sign-up logic
        # ...

        # Redirect to a success page
        return redirect("/success")

    # Render the sign-up form template
    return render_template("signup.html")


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
    """
    The function `insert_employee` inserts employee data into a database and returns a list of all
    employees.
    :return: the result of the `get_employees()` function.
    """
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

        # Create an instance of the EmployeeDAO and insert the employee
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
        return get_employees()
    return render_template("insert_employee.html")


@app.route("/update_emp", methods=["GET", "POST"])
def update_employee():
    if request.method == "POST":
        # Retrieve form data
        emp_id = []
        emp_id.append(request.form.get("emp_id"))
        fname = request.form.get("fname")
        lname = request.form.get("lname")
        location = request.form.get("location")
        phone1 = request.form.get("phone1")
        sex = request.form.get("sex")
        email = request.form.get("email")
        password = request.form.get("password")
        # Create an instance of the DepartmentDAO and insert the department
        employee = DAO.EmployeeDAO()
        # * Validation to use Kwargs correct based on the input we will pass to the fucntio

        if emp_id:
            existing_emp = employee.get_emp_by_id(emp_id[0])
            if existing_emp:
                kwargs = {
                    "fname": fname if fname else existing_emp[0][1],
                    "lname": lname if lname else existing_emp[0][2],
                    "location": location if location else existing_emp[0][3],
                    "phone1": phone1 if phone1 else existing_emp[0][4],
                    "sex": sex if sex else existing_emp[0][5],
                    "email": email if email else existing_emp[0][6],
                    "password": password if password else existing_emp[0][7],
                }
        employee.update_emp(employees=emp_id, **kwargs)
        return get_employees()
    return render_template("update_emp.html")


@app.route("/employee/delete", methods=["POST", "GET"])
def delete_emp():
    """
    The function `delete_emp()` deletes an employee from the database if the request method is POST,
    otherwise it returns the list of employees.
    :return: the result of calling the `get_employees()` function.
    """
    if request.method == "POST":
        employee = DAO.EmployeeDAO()
        emp_id = []
        emp_id.append(request.form.get("input_pr_id2"))
        employee.delete_emp(emp_id)
        return get_employees()
    else:
        return get_employees()


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
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)

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


@app.route("/insert_dep", methods=["GET", "POST"])
def insert_department():
    """
    The function `insert_department` inserts a new department into a database using form data and
    returns a list of all departments.
    :return: the result of the "get_departments()" function.
    """
    if request.method == "POST":
        # Retrieve form data
        name = request.form.get("name")
        salary_range = request.form.get("salary_range")
        description = request.form.get("description")

        # Create an instance of the DepartmentDAO and insert the department
        department = DAO.DepartmentDAO()
        kwargs = {
            "name": name if name else None,
            "salary_range": salary_range if salary_range else None,
            "description": description if description else None,
        }
        department.insert_dep(**kwargs)

        return get_departments()
    return render_template("insert_dep.html")


@app.route("/update_dep", methods=["GET", "POST"])
def update_department():
    """
    The function `update_department` updates a department based on the form data received, with optional
    fields for name, salary range, and description.
    :return: the result of the `get_departments()` function call.
    """
    if request.method == "POST":
        # Retrieve form data
        dep_id = []
        dep_id.append(request.form.get("dep_id"))
        name = request.form.get("name")
        salary_range = request.form.get("salary_range")
        description = request.form.get("description")
        # Create an instance of the DepartmentDAO and insert the department
        department = DAO.DepartmentDAO()
        # * Validation to use Kwargs correct based on the input we will pass to the fucntion
        if dep_id:
            existing_dep = department.get_dep_by_id(dep_id[0])
            if existing_dep:
                kwargs = {
                    "name": name if name else existing_dep[0][1],
                    "salary_range": salary_range
                    if salary_range
                    else existing_dep[0][2],
                    "description": description if description else existing_dep[0][3],
                }

            # Assuming there's a method to fetch employee details by ID

        department.update_dep(departments=dep_id, **kwargs)
        return get_departments()
    return render_template("update_dep.html")


@app.route("/department/delete", methods=["POST", "GET"])
def delete_dep():
    """
    The function `delete_dep()` deletes a department based on the department ID received in a POST
    request, and then returns the updated list of departments.
    :return: the result of the `get_departments()` function.
    """
    if request.method == "POST":
        department = DAO.DepartmentDAO()
        dep_id = []
        dep_id.append(request.form.get("input_pr_id2"))
        department.delete_dep(dep_id)
        return get_departments()

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
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)

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


@app.route("/insert_leave", methods=["GET", "POST"])
def insert_leave():
    """
    The function `insert_leave` inserts a leave record into a database table based on form data and
    returns a page displaying all leave records.
    :return: the result of calling the `get_leaves()` function.
    """
    if request.method == "POST":
        # Retrieve form data
        employee_emp_id = request.form.get("employee_emp_id")
        date = request.form.get("date")
        reason = request.form.get("reason")
        status = request.form.get("status")
        kwargs = {
            "employee_emp_id": employee_emp_id if employee_emp_id else None,
            "date": date if date else None,
            "reason": reason if reason else None,
            "status": status if status else None,
        }
        leave = DAO.LeaveDAO()
        leave.insert_leave(**kwargs)
        # Create an instance of the DepartmentDAO and insert the department

        return get_leaves()
    return render_template("insert_leave.html")


@app.route("/update_leave", methods=["GET", "POST"])
def update_leave():
    if request.method == "POST":
        # Retrieve form data
        leave_id = []
        leave_id.append(request.form.get("leave_id"))
        employee_emp_id = request.form.get("employee_emp_id")
        date = request.form.get("date")
        reason = request.form.get("reason")
        status = request.form.get("status")
        leave = DAO.LeaveDAO()

        if leave_id:
            existing_leave = leave.get_leave_by_id(leave_id[0])
            if existing_leave:
                kwargs = {
                    "employee_emp_id": employee_emp_id
                    if employee_emp_id
                    else existing_leave[0][1],
                    "date": date if date else existing_leave[0][2],
                    "status": status if status else existing_leave[0][3],
                    "reason": reason if reason else existing_leave[0][4],
                }

        leave.update_leave(leave_id, **kwargs)
        return get_leaves()
    return render_template("update_leave.html")


@app.route("/leave/delete", methods=["POST", "GET"])
def delete_leave():
    """
    The function `delete_leave` deletes a leave entry from a database if the request method is POST,
    otherwise it returns a list of leaves.
    :return: the result of calling the `get_leaves()` function.
    """
    if request.method == "POST":
        leave = DAO.LeaveDAO()
        leave_id = []
        leave_id.append(request.form.get("input_pr_id2"))
        leave.delete_leave(leave_id)
        return get_leaves()

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
        if records:
            records = tuple([str(rec) for rec in records])
            records_list.append(records)
            len_rec = len(records)

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


@app.route("/insert_salary", methods=["POST", "GET"])
def insert_salary():
    """
    The function `insert_salary` is used to insert salary information into a database and then retrieve
    all salaries.
    :return: the result of calling the "get_salaries()" function.
    """
    if request.method == "POST":
        # Retrieve form data
        department_dep_id = request.form.get("department_dep_id")
        amount = request.form.get("amount")
        bounes = request.form.get("bounes")
        overtime = request.form.get("overtime")
        annual = request.form.get("annual")

        # Create an instance of the DepartmentDAO and insert the department
        salary = DAO.SalaryDAO()

        kwargs = {
            "department_dep_id": department_dep_id if department_dep_id else None,
            "amount": amount if amount else None,
            "bounes": bounes if bounes else None,
            "overtime": overtime if overtime else None,
            "annual": annual if annual else None,
        }
        salary.insert_salary(**kwargs)
        return get_salaries()
    return render_template("insert_salary.html")


@app.route("/update_salary", methods=["GET", "POST"])
def update_salary():
    if request.method == "POST":
        # Retrieve form data
        salary_id = []
        salary_id.append(request.form.get("salary_id"))
        department_dep_id = request.form.get("department_dep_id")
        amount = request.form.get("amount")
        bounes = request.form.get("bounes")
        overtime = request.form.get("overtime")
        annual = request.form.get("annual")
        salary = DAO.SalaryDAO()
        if salary_id:
            existing_salary = salary.get_salary_by_id(salary_id[0])
            if existing_salary:
                kwargs = {
                    "department_dep_id": department_dep_id
                    if department_dep_id
                    else existing_salary[0][-1],
                    "amount": amount if amount else existing_salary[0][1],
                    "bounes": bounes if bounes else existing_salary[0][2],
                    "annual": annual if annual else existing_salary[0][3],
                    "overtime": overtime if overtime else existing_salary[0][4],
                }

        salary.update_salary(salary_id, **kwargs)
        return get_salaries()
    return render_template("update_salary.html")


@app.route("/salary/delete", methods=["POST", "GET"])
def delete_salary():
    """
    The function `delete_salary` deletes a salary record from the database if the request method is
    POST, otherwise it returns the list of salaries.
    :return: the result of the function call `get_salaries()`.
    """
    if request.method == "POST":
        salary = DAO.SalaryDAO()
        salary_id = []
        salary_id.append(request.form.get("input_pr_id2"))
        salary.delete_salary(salary_id)
        return get_salaries()

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


@app.route("/insert_payroll", methods=["POST", "GET"])
def insert_payroll():
    """
    The function `insert_payroll` inserts payroll data into the database and redirects to the page
    displaying all payrolls.
    :return: the result of the `get_payrolls()` function or rendering the "insert_payroll.html"
    template.
    """
    if request.method == "POST":
        # Retrieve form data
        department_dep_id = request.form.get("department_dep_id")
        employee_emp_id = request.form.get("employee_emp_id")
        date = request.form.get("date")
        leave_leave_id = request.form.get("leave_leave_id")
        total_amount = request.form.get("total_amount")
        report = request.form.get("report")
        salary_salary_id = request.form.get("salary_salary_id")

        # Create an instance of the DepartmentDAO and insert the department
        payroll = DAO.PayrollDAO()

        kwargs = {
            "department_dep_id": department_dep_id if department_dep_id else None,
            "employee_emp_id": employee_emp_id if employee_emp_id else None,
            "leave_leave_id": leave_leave_id if leave_leave_id else None,
            "salary_salary_id": salary_salary_id if salary_salary_id else None,
            "total_amount": total_amount if total_amount else None,
            "report": report if report else None,
            "date": date if date else None,
        }
        payroll.insert_payroll(**kwargs)
        return get_payrolls()
    return render_template("insert_payroll.html")


@app.route("/update_payroll", methods=["GET", "POST"])
def update_payroll():
    if request.method == "POST":
        # Retrieve form data
        payroll_id = []
        payroll_id.append(request.form.get("payroll_id"))
        department_dep_id = request.form.get("department_dep_id")
        employee_emp_id = request.form.get("employee_emp_id")
        date = request.form.get("date")
        leave_leave_id = request.form.get("leave_leave_id")
        total_amount = request.form.get("total_amount")
        report = request.form.get("report")
        salary_salary_id = request.form.get("salary_salary_id")
        payroll = DAO.PayrollDAO()

        if payroll_id:
            existing_payroll = payroll.get_payroll_by_id(payroll_id[0])
            if existing_payroll:
                kwargs = {
                    "date": date if date else existing_payroll[0][1],
                    "report": report if report else existing_payroll[0][2],
                    "total_amount": total_amount
                    if total_amount
                    else existing_payroll[0][3],
                    "employee_emp_id": employee_emp_id
                    if employee_emp_id
                    else existing_payroll[0][4],
                    "leave_leave_id": leave_leave_id
                    if leave_leave_id
                    else existing_payroll[0][5],
                    "salary_salary_id": salary_salary_id
                    if salary_salary_id
                    else existing_payroll[0][6],
                    "department_dep_id": department_dep_id
                    if department_dep_id
                    else existing_payroll[0][-1],
                }

        payroll.update_payroll(payroll_id, **kwargs)
        return get_payrolls()
    return render_template("update_payroll.html")


@app.route("/payroll/delete", methods=["POST", "GET"])
def delete_payroll():
    if request.method == "POST":
        payroll = DAO.PayrollDAO()
        payroll_id = []
        payroll_id.append(request.form.get("input_pr_id2"))
        payroll.delete_payroll(payroll_id)
        return get_payrolls()

    else:
        return get_payrolls()


# The `if __name__ == '__main__':` block is used to ensure that the code inside it is only executed
# when the script is run directly, and not when it is imported as a module in another script.
if __name__ == "__main__":
    app.run(debug=True)
