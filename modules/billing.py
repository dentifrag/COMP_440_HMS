from flask import Blueprint, render_template, request, redirect, url_for
from db import mysql

billing_bp = Blueprint('billing', __name__)


@billing_bp.route('/', methods=['GET'], defaults={'bill_id': None})
@billing_bp.route('/<bill_id>', methods=['GET'])
def billing(bill_id):
    cur = mysql.connection.cursor()
    if bill_id is not None:
        # Query to get a specific bill along with patient name
        result = cur.execute("""
            SELECT b.bill_id, b.amount, b.bill_date, b.payment_status, p.name AS patient_name
            FROM billing b
            JOIN patients p ON b.patient_id = p.patient_id
            WHERE b.bill_id = %s
        """, (bill_id,))
        billing_ = []

        if result > 0:
            data = cur.fetchall()
            billing_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('billing/view_bill.html', billing=billing_)
    else:
        # Query to get all bills along with patient names
        result = cur.execute("""
            SELECT b.bill_id, b.amount, b.bill_date, b.payment_status, p.name AS patient_name
            FROM billing b
            JOIN patients p ON b.patient_id = p.patient_id
        """)
        billing_ = []

        if result > 0:
            data = cur.fetchall()
            billing_ = [dict(zip([key[0] for key in cur.description], row)) for row in data]

        cur.close()
        return render_template('billing/billing.html', billing=billing_)



@billing_bp.route('/add_bill', methods=['GET', 'POST'])
def add_bill():
    if request.method == 'POST':
        patient_id = request.form['patient']
        amount = request.form['amount']
        date = request.form['date']
        payment_status = request.form['status']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO billing (patient_id, amount, bill_date, payment_status) VALUES (%s, %s, %s, %s)",
            (patient_id, amount, date, payment_status))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('billing.billing'))

    cur = mysql.connection.cursor()
    cur.execute("SELECT patient_id, name FROM patients")
    patients = cur.fetchall()
    patients = [dict(zip([key[0] for key in cur.description], row)) for row in patients]
    cur.close()
    return render_template('billing/add_bill.html', patients=patients)


@billing_bp.route('/edit_bill/<bill_id>', methods=['GET', 'POST'])
def edit_bill(bill_id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM billing WHERE bill_id = %s", (bill_id,))
    data = cur.fetchone()
    data = dict(zip([key[0] for key in cur.description], data))

    if request.method == 'POST':
        amount = request.form['amount']
        date = request.form['date']
        payment_status = request.form['status']

        cur.execute("UPDATE billing SET amount = %s, bill_date = %s, payment_status = %s WHERE bill_id = %s",
                    (amount, date, payment_status, bill_id))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('billing.billing'))

    cur.execute("SELECT patient_id, name FROM patients WHERE patient_id = %s", (data['patient_id'],))
    patient = cur.fetchone()
    # patient = [dict(zip([key[0] for key in cur.description], row)) for row in patient]
    cur.close()
    return render_template('billing/edit_bill.html', bill=data, patient=patient)


@billing_bp.route('/delete_bill/<bill_id>', methods=['GET', 'POST'])
def delete_bill(bill_id):
    if request.method == 'POST':
        cur = mysql.connection.cursor()
        cur.execute("DELETE FROM billing WHERE bill_id = %s", (bill_id,))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('billing.billing'))
    return render_template('billing/confirm_delete.html', bill_id=bill_id)
