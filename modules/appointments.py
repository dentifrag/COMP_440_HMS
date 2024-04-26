from flask import Blueprint, render_template, request, redirect, url_for
from db import mysql

appointments_bp = Blueprint('appointments', __name__)


@appointments_bp.route('/', methods=['GET'], defaults={'appointment_id': None})
@appointments_bp.route('/<appointment_id>', methods=['GET'])
def appointments(appointment_id):
    cur = mysql.connection.cursor()
    if appointment_id is not None:
        result = cur.execute("""
            SELECT a.appointment_id, a.appointment_date, a.purpose, d.name AS doctor_name, p.name AS patient_name
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            JOIN patients p ON a.patient_id = p.patient_id
            WHERE a.appointment_id = %s
        """, (appointment_id,))
        appointment_ = []

        if result > 0:
            data = cur.fetchall()
            appointment_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('appointments/view_appointment.html', appointments=appointment_)
    else:
        result = cur.execute("""
            SELECT a.appointment_id, a.appointment_date, a.purpose, d.name AS doctor_name, p.name AS patient_name
            FROM appointments a
            JOIN doctors d ON a.doctor_id = d.doctor_id
            JOIN patients p ON a.patient_id = p.patient_id
        """)
        appointments_ = []

        if result > 0:
            data = cur.fetchall()
            appointments_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('appointments/appointments.html', appointments=appointments_)


@appointments_bp.route('/add_appointment', methods=['GET', 'POST'])
def add_appointment():
    if request.method == 'POST':
        patient_id = request.form['patient']
        doctor_id = request.form['doctor']
        date = request.form['date']
        time = request.form['time']
        datetime_str = f"{date} {time}"
        purpose = request.form['purpose']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO appointments (patient_id, doctor_id, appointment_date, purpose) VALUES (%s, %s, %s, %s)",
            (patient_id, doctor_id, datetime_str, purpose))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('appointments.appointments'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT doctor_id, name FROM doctors")
    doctors = cur.fetchall()
    doctors = [dict(zip([key[0] for key in cur.description], row)) for row in doctors]

    cur.execute("SELECT patient_id, name FROM patients")
    patients = cur.fetchall()
    patients = [dict(zip([key[0] for key in cur.description], row)) for row in patients]
    cur.close()

    return render_template('appointments/add_appointment.html', doctors=doctors, patients=patients)


@appointments_bp.route('/edit_appointment/<int:appointment_id>', methods=['GET', 'POST'])
def edit_appointment(appointment_id):
    if request.method == 'POST':
        patient_id = request.form['patient']
        doctor_id = request.form['doctor']
        date = request.form['date']
        time = request.form['time']
        datetime_str = f"{date} {time}"
        purpose = request.form['purpose']

        cur = mysql.connection.cursor()
        cur.execute(
            "UPDATE appointments SET patient_id = %s, doctor_id = %s, appointment_date = %s, purpose = %s WHERE appointment_id = %s",
            (patient_id, doctor_id, datetime_str, purpose, appointment_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('appointments.appointments'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT doctor_id, name FROM doctors")
    doctors = cur.fetchall()
    doctors = [dict(zip([key[0] for key in cur.description], row)) for row in doctors]

    cur.execute("SELECT patient_id, name FROM patients")
    patients = cur.fetchall()
    patients = [dict(zip([key[0] for key in cur.description], row)) for row in patients]

    cur.execute("SELECT * FROM appointments WHERE appointment_id = %s", (appointment_id,))
    appointment = cur.fetchall()
    appointment = [dict(zip([key[0] for key in cur.description], row)) for row in appointment]
    cur.close()

    return render_template('appointments/edit_appointment.html', doctors=doctors, patients=patients,
                           appointment=appointment[0])


@appointments_bp.route('/delete_appointment/<int:appointment_id>', methods=['GET', 'POST'])
def delete_appointment(appointment_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM appointments WHERE appointment_id = %s", (appointment_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('appointments.appointments'))
    return render_template('appointments/confirm_delete.html')


@appointments_bp.route('/patient/<patient_id>', methods=['GET'])
def patient_appointments(patient_id):
    cur = mysql.connection.cursor()
    result = cur.execute("""
        SELECT a.appointment_id, a.appointment_date, a.purpose, p.name AS patient_name, d.name AS doctor_name
        FROM appointments a
        JOIN patients p ON a.patient_id = p.patient_id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE a.patient_id = %s
    """, (patient_id,))
    appointments_ = []

    if result > 0:
        data = cur.fetchall()
        appointments_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('appointments/appointments.html', appointments=appointments_)


@appointments_bp.route('/doctor/<doctor_id>', methods=['GET'])
def doctor_appointments(doctor_id):
    cur = mysql.connection.cursor()
    result = cur.execute("""
            SELECT a.appointment_id, a.appointment_date, a.purpose, p.name AS patient_name, d.name AS doctor_name
            FROM appointments a
            JOIN patients p ON a.patient_id = p.patient_id
            JOIN doctors d ON a.doctor_id = d.doctor_id
            WHERE a.doctor_id = %s
        """, (doctor_id,))
    appointments_ = []

    if result > 0:
        data = cur.fetchall()
        appointments_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('appointments/appointments.html', appointments=appointments_)