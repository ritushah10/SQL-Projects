# Some set up for the application 

from flask import Flask
from flaskext.mysql import MySQL

# create a MySQL object that we will use in other parts of the API
db = MySQL()

def create_fairway():
    app = Flask(__name__)

    # secret key that will be used for securely signing the session 
    # cookie and can be used for any other security related needs by 
    # extensions or your application
    app.config['SECRET_KEY'] = 'abc123'

    # these are for the DB object to be able to connect to MySQL. 
    app.config['MYSQL_DATABASE_USER'] = 'CEO'
    app.config['MYSQL_DATABASE_PASSWORD'] = open('/secrets/db_password.txt').readline()
    app.config['MYSQL_DATABASE_HOST'] = 'db'
    app.config['MYSQL_DATABASE_PORT'] = 3306
    app.config['MYSQL_DATABASE_DB'] = 'FairWayProtoType'  # my DB name

    # Initialize the database object with the settings above. 
    db.init_app(app)

    # Import the various routes
    from src.views import views
    from src.customer_api.customers import customers
    from src.employee_api.employees import employees
    from src.manufacturer_api.manufacturers import manufacturers

    # Register the routes that we just imported so they can be properly handled
    app.register_blueprint(views,       url_prefix='/home')
    app.register_blueprint(customers,   url_prefix='/home')
    app.register_blueprint(employees,    url_prefix='/home')
    app.register_blueprint(manufacturers,    url_prefix='/home')

    return app