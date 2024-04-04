from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'hospitalmanagementsystem'

mysql = MySQL(app)

from modules.appointments import appointments_bp
from modules.doctors import doctors_bp
from modules.patients import patients_bp
from modules.billing import billing_bp

app.register_blueprint(appointments_bp, url_prefix='/appointments')
app.register_blueprint(doctors_bp, url_prefix='/doctors')
app.register_blueprint(patients_bp, url_prefix='/patients')
app.register_blueprint(billing_bp, url_prefix='/billing')

if __name__ == "__main__":
    app.run(debug=True)
