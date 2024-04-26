from flask import Blueprint, render_template
from db import mysql

doctors_bp = Blueprint('doctors', __name__)


@doctors_bp.route('/', methods=['GET'], defaults={'doctor_id': None})
@doctors_bp.route('/<doctor_id>', methods=['GET'])
def doctors(doctor_id):
    cur = mysql.connection.cursor()
    if doctor_id is not None:
        result = cur.execute("SELECT * FROM doctors WHERE doctor_id = %s", (doctor_id,))
        doctor_ = []

        if result > 0:
            data = cur.fetchall()
            doctor_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('doctors/view_doctor.html', doctors=doctor_)
    else:
        result = cur.execute("SELECT * FROM doctors")
        doctors_ = []

        if result > 0:
            data = cur.fetchall()
            doctors_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('doctors/doctors.html', doctors=doctors_)


