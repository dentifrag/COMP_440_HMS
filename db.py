from flask_mysqldb import MySQL


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='your_host',
            database='your_database',
            user='your_user',
            password='your_password'
        )
        return connection
    except Error as e:
        print(f"Error: {e}")
        return None
