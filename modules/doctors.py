from flask import Blueprint, render_template, request, redirect, url_for
from app import mysql

doctors_bp = Blueprint('doctors', __name__)


@doctors_bp.route('/', methods=['GET'])
def doctors():
    cur = mysql.connection.cursor()
    result = cur.execute("SELECT * FROM doctors")
    doctors_ = []

    if result > 0:
        data = cur.fetchall()
        doctors_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

    cur.close()
    return render_template('doctors/doctors.html', doctors=doctors_)
