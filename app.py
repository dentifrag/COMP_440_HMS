from flask import Flask, redirect
from db import init_app
from modules.appointments import appointments_bp
from modules.doctors import doctors_bp
from modules.patients import patients_bp
from modules.billing import billing_bp
from modules.search import search_bp

app = Flask(__name__)

# Initialize MySQL with app configuration
init_app(app)

app.register_blueprint(appointments_bp, url_prefix='/appointments')
app.register_blueprint(doctors_bp, url_prefix='/doctors')
app.register_blueprint(patients_bp, url_prefix='/patients')
app.register_blueprint(billing_bp, url_prefix='/billing')
app.register_blueprint(search_bp, url_prefix='/search')


@app.route('/')
def index():
    return redirect('/patients')


if __name__ == "__main__":
    app.run(debug=True)
