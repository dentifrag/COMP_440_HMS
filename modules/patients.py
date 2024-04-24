from flask import Blueprint, render_template, request, redirect, url_for, flash
from db import mysql

patients_bp = Blueprint('patients', __name__)


@patients_bp.route('/', methods=['GET'], defaults={'patient_id': None})
@patients_bp.route('/<patient_id>', methods=['GET'])
def patients(patient_id):
    if patient_id is not None:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
        patient_ = []

        if result > 0:
            data = cur.fetchall()
            patient_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('patients/view_patient.html', patients=patient_)
    else:
        cur = mysql.connection.cursor()
        result = cur.execute("SELECT * FROM patients")
        patients_ = []

        if result > 0:
            data = cur.fetchall()
            patients_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]
        cur.close()
        return render_template('patients/patients.html', patients=patients_)


@patients_bp.route('/add', methods=['GET', 'POST'])
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
            "INSERT INTO patients (name, date_of_birth, gender, contact_info, address, email, emergency_contact_name, "
            "emergency_contact_phone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (name, dob, gender, contact_info, address, email, emergency_contact_name, emergency_contact_phone))
        mysql.connection.commit()
        return redirect(url_for('patients.patients'))
    return render_template('patients/add_patient.html')


# In your modules/patients.py or wherever you have defined the patients blueprint

@patients_bp.route('/edit/<int:patient_id>', methods=['GET', 'POST'])
def edit_patient(patient_id):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        # Retrieve updated form data
        name = request.form['name']
        dob = request.form['dob']
        gender = request.form['gender']
        contact_info = request.form.get('contact_info', '')
        address = request.form.get('address', '')
        email = request.form.get('email', '')
        emergency_contact_name = request.form.get('emergency_contact_name', '')
        emergency_contact_phone = request.form.get('emergency_contact_phone', '')

        # Update patient in the database
        cur.execute("""
            UPDATE patients
            SET name=%s, date_of_birth=%s, gender=%s, contact_info=%s, address=%s, email=%s, 
                emergency_contact_name=%s, emergency_contact_phone=%s
            WHERE patient_id=%s
        """, (name, dob, gender, contact_info, address, email, emergency_contact_name, emergency_contact_phone, patient_id))

        mysql.connection.commit()
        cur.close()

        return redirect(url_for('patients.patients'))

    cur.execute("SELECT * FROM patients WHERE patient_id = %s", (patient_id,))
    patient = cur.fetchone()
    patient = dict(zip([key[0] for key in cur.description], patient))
    cur.close()

    if not patient:
        return 'Patient not found', 404

    return render_template('patients/edit_patient.html', patient=patient)


@patients_bp.route('/delete/<int:patient_id>', methods=['GET', 'POST'])
def delete_patient(patient_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM patients WHERE patient_id = %s", (patient_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('patients.patients'))

    return render_template('patients/confirm_delete.html')



