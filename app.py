from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configure MySQL Connection
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'hospitalmanagementsystem'

mysql = MySQL(app)


@app.route('/appointments', methods=['GET'])
def get_appointments():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM appointments")
    appointments_ = []

    if result > 0:
        data = cur.fetchall()
        appointments_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('appointments/appointments.html', appointments=appointments_)


@app.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        patient_id = request.form['patient']
        doctor_id = request.form['doctor']
        date = request.form['date']
        time = request.form['time']
        datetime_str = f"{date} {time}"
        purpose = request.form['purpose']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose) VALUES (%s, %s, "
                "%s, %s)",
                (patient_id, doctor_id, datetime_str, purpose))
    mysql.connection.commit()
    return redirect(url_for('get_appointments'))


    cur = mysql.connection.cursor()

    cur.execute("SELECT doctor_id, name FROM doctors")
    doctors = cur.fetchall()
    doctors = [dict(zip([key[0] for key in cur.description], row)) for row in doctors]

    cur.execute("SELECT patient_id, name FROM patients")
    patients = cur.fetchall()
    patients = [dict(zip([key[0] for key in cur.description], row)) for row in patients]
    return render_template('appointments/add_appointment.html', doctors=doctors, patients=patients)


@app.route('/patients', methods=['GET'])
def patients():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM patients")
    patients_ = []

    if result > 0:
        data = cur.fetchall()
        # Convert the tuples to dictionaries
        patients_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('patients/patients.html', patients=patients_)


@app.route('/add_patient', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        # Retrieve form data
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact_info = request.form.get('contact_info', '')
        address = request.form.get('address', '')
        email = request.form.get('email', '')
        emergency_contact_name = request.form.get('emergency_contact_name', '')
        emergency_contact_phone = request.form.get('emergency_contact_phone', '')

        # Insert into database
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO patients (name, date_of_birth, gender, contact_info, address, email, emergency_contact_name, emergency_contact_phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (name, dob, gender, contact_info, address, email, emergency_contact_name, emergency_contact_phone))
        mysql.connection.commit()
        return redirect(url_for('patients'))
    return render_template('patients/add_patient.html')


@app.route('/doctors', methods=['GET'])
def doctors():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM doctors")
    doctors_ = []

    if result > 0:
        data = cur.fetchall()
        doctors_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('doctors/doctors.html', doctors=doctors_)

if __name__ == "__main__":
    app.run(debug=True)
