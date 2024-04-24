from flask import request, render_template, Flask, Blueprint
from db import mysql

search_bp = Blueprint('Search', __name__)


@search_bp.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '')
    if query:
        cur = mysql.connection.cursor()
        search_query = f"""
            SELECT name, 'Patient' as type, patient_id FROM patients 
            WHERE MATCH(name) AGAINST (%s IN NATURAL LANGUAGE MODE) 
            UNION 
            SELECT name, 'Doctor' as type, doctor_id FROM doctors 
            WHERE MATCH(name) AGAINST (%s IN NATURAL LANGUAGE MODE)
        """
        cur.execute(search_query, (query, query))
        results = cur.fetchall()
        cur.close()
        return render_template('search/search_results.html', results=results, query=query)
    return render_template('search/search_results.html', results=None, query=query)

