
# Employee Management System

An Employee Management System is a Full-Stack web application for managing
the staff data within a small company or organization. The system as such as it has been
developed is called the Employee Management System. It consists of functionally related
GUI (application program) and database.

## Project Dependencies
*  Python
- Flask
- HTML
- CSS
- Javascript
- Bootstrap
- MySql
- Jinja2

## Getting Started

1. Clone the repository:
2.  Open the terminal in the project directory 
3. Run  pip install -r requirements.txt
4. Activate virtual environment: env\Scripts\activate
5. After activating virtual env run: python app.py
6. Open your web browser and visit `http://localhost:5000/`

## How it Works
The user logs in as admin after validating the inputs with the database the user will be able to see all the tables to do any operation he wants.
When he clicks on any button to make any CRUD operation it will redirect him to another page to do the operation or the same page, then FLASK server will call class DAO the interface between the database and the server to separate the business layer from the database layer. after the request is successful it will return the data from the database to DAO then to FLASK server then to the website to generate the new table for the response.
All functions in DAO classes are dynamically created and take any number of parameters to make it easier to use and to save memory. All the pages are generated dynamically based on the input from flask using Jinja2


![Flow Diagram](https://github.com/MahmoudKhaled007/Employee-Managment-System/raw/master/Flow.png)


Contributions are welcome! If you have any suggestions or improvements, please create a pull request.

## Authors

- [@MahmoudKhaled007](https://www.github.com/MahmoudKhaled007)


## License

[GNU](https://www.gnu.org/licenses/gpl-3.0.en.html)

