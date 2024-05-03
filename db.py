from flask_mysqldb import MySQL

mysql = MySQL()


def init_app(app):
    app.config['MYSQL_HOST'] = 'db'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = 'root'
    app.config['MYSQL_DB'] = 'hospitalmanagementsystem'
    mysql.init_app(app)
