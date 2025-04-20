from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, send_from_directory
from database import execute_procedure, get_db_connection
from datetime import datetime
import os
import json

# Get the absolute path of the current directory
basedir = os.path.abspath(os.path.dirname(__file__))

# Initialize Flask app with explicit template and static folders
app = Flask(__name__,
           template_folder=os.path.join(basedir, 'templates'),
           static_folder=os.path.join(basedir, 'static'))

app.secret_key = 'your_secret_key_here'  # Change this to a secure secret key

# Helper function to determine if the request is AJAX
def is_ajax():
    return request.headers.get('X-Requested-With') == 'XMLHttpRequest'

# Home route
@app.route('/')
def home():
    # Test database connection
    conn = get_db_connection()
    if conn is None:
        flash('Database connection failed!', 'error')
    else:
        conn.close()
    return render_template('index.html')

# Pharmacy routes
@app.route('/pharmacies')
def pharmacies():
    if is_ajax():
        try:
            # Direct SQL query instead of stored procedure since get_pharmacies doesn't exist
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT ph_name, ph_add, ph_contact FROM Pharmacy")
            pharmacies_list = cursor.fetchall()
            cursor.close()
            conn.close()
            
            if pharmacies_list is None:
                pharmacies_list = []
            return jsonify(pharmacies_list)
        except Exception as e:
            app.logger.error(f"Error fetching pharmacies: {str(e)}")
            return jsonify([]), 500
    return render_template('pharmacies.html')

@app.route('/add_pharmacy', methods=['POST'])
def add_pharmacy():
    if request.method == 'POST':
        try:
            ph_name = request.form['ph_name']
            ph_add = request.form['ph_add']
            ph_contact = request.form['ph_contact']
            
            result = execute_procedure('add_ph', [ph_name, ph_add, ph_contact])
            if result is not None:
                flash('Pharmacy added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding pharmacy', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('pharmacies'))

@app.route('/delete_pharmacy/<ph_name>', methods=['DELETE'])
def delete_pharmacy(ph_name):
    try:
        result = execute_procedure('del_ph', [ph_name])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting pharmacy: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Pharmaceutical Company routes
@app.route('/companies')
def companies():
    if is_ajax():
        try:
            # Direct SQL query since get_pharma_companies doesn't exist
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT pc_name, pc_contact FROM PharmaCompany")
            companies_list = cursor.fetchall()
            cursor.close()
            conn.close()
            
            if companies_list is None:
                companies_list = []
            return jsonify(companies_list)
        except Exception as e:
            app.logger.error(f"Error fetching companies: {str(e)}")
            return jsonify([]), 500
    return render_template('companies.html')

@app.route('/add_company', methods=['POST'])
def add_company():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            pc_contact = request.form['pc_contact']
            
            result = execute_procedure('add_pc', [pc_name, pc_contact])
            if result is not None:
                flash('Company added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding company', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('companies'))

@app.route('/delete_company/<pc_name>', methods=['DELETE'])
def delete_company(pc_name):
    try:
        result = execute_procedure('del_pc', [pc_name])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting company: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Doctor routes
@app.route('/doctors')
def doctors():
    if is_ajax():
        try:
            doctors_list = execute_procedure('d_view')
            if doctors_list is None:
                doctors_list = []
            return jsonify(doctors_list)
        except Exception as e:
            app.logger.error(f"Error fetching doctors: {str(e)}")
            return jsonify([]), 500
    return render_template('doctors.html')

@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    if request.method == 'POST':
        try:
            d_name = request.form['d_name']
            spec = request.form['spec']
            years_of_exp = request.form['years_of_exp']
            d_aadhar = request.form['d_aadhar']
            
            result = execute_procedure('add_doc', [d_name, spec, years_of_exp, d_aadhar])
            if result is not None:
                flash('Doctor added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding doctor', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('doctors'))

@app.route('/delete_doctor/<d_aadhar>', methods=['DELETE'])
def delete_doctor(d_aadhar):
    try:
        result = execute_procedure('del_doc', [d_aadhar])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting doctor: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Patient routes
@app.route('/patients')
def patients():
    if is_ajax():
        try:
            # p_view only returns p_name and p_aadhar, we need more fields
            # So join with doctor table to get more information
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT p.p_name, p.p_add, p.p_age, p.p_aadhar, p.p_doc_aid, d.d_name
                FROM Patient p
                LEFT JOIN Doctor d ON p.p_doc_aid = d.d_aadhar
            """)
            patients_list = cursor.fetchall()
            cursor.close()
            conn.close()
            if patients_list is None:
                patients_list = []
            return jsonify(patients_list)
        except Exception as e:
            app.logger.error(f"Error fetching patients: {str(e)}")
            return jsonify([]), 500
    return render_template('patients.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        try:
            p_name = request.form['p_name']
            p_add = request.form['p_add']
            p_age = request.form['p_age']
            p_aadhar = request.form['p_aadhar']
            p_doc_aid = request.form['p_doc_aid']
            
            result = execute_procedure('add_pat', [p_name, p_add, p_age, p_aadhar, p_doc_aid])
            if result is not None:
                flash('Patient added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding patient', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('patients'))

@app.route('/delete_patient/<p_aadhar>', methods=['DELETE'])
def delete_patient(p_aadhar):
    try:
        result = execute_procedure('del_pat', [p_aadhar])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting patient: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Prescription routes
@app.route('/prescriptions')
def prescriptions():
    if is_ajax():
        try:
            # pr_details requires parameters, so we'll use a direct query
            conn = get_db_connection()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("""
                SELECT pr.pr_no, pr.pr_date, p.p_name, d.d_name,
                       p.p_aadhar as p_id, d.d_aadhar as d_id
                FROM Prescription pr
                JOIN Patient p ON pr.p_id = p.p_aadhar
                JOIN Doctor d ON pr.d_id = d.d_aadhar
                ORDER BY pr.pr_date DESC
            """)
            prescriptions_list = cursor.fetchall()
            cursor.close()
            conn.close()
            if prescriptions_list is None:
                prescriptions_list = []
            return jsonify(prescriptions_list)
        except Exception as e:
            app.logger.error(f"Error fetching prescriptions: {str(e)}")
            return jsonify([]), 500
    return render_template('prescriptions.html')

@app.route('/add_prescription', methods=['POST'])
def add_prescription():
    if request.method == 'POST':
        try:
            pr_date = request.form['pr_date']
            p_id = request.form['p_id']
            d_id = request.form['d_id']
            
            result = execute_procedure('add_presc', [pr_date, p_id, d_id])
            if result is not None:
                flash('Prescription added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding prescription', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('prescriptions'))

@app.route('/delete_prescription/<pr_id>', methods=['DELETE'])
def delete_prescription(pr_id):
    try:
        result = execute_procedure('del_presc', [pr_id])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting prescription: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Report generation routes
@app.route('/patient_report', methods=['GET', 'POST'])
def patient_report():
    if request.method == 'POST':
        try:
            p_aadhar = request.form['p_aadhar']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            
            # p_report needs exact parameters
            report = execute_procedure('p_report', [p_aadhar, start_date, end_date])
            if is_ajax():
                return jsonify(report if report else [])
            return render_template('patient_report.html', report=report)
        except Exception as e:
            app.logger.error(f"Error generating patient report: {str(e)}")
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 500
            flash(f'Error: {str(e)}', 'error')
    return render_template('patient_report.html')

@app.route('/prescription_details', methods=['GET', 'POST'])
def prescription_details():
    if request.method == 'POST':
        try:
            p_aadhar = request.form['p_aadhar']
            pr_date = request.form['pr_date']
            
            # pr_details needs exact parameters
            details = execute_procedure('pr_details', [p_aadhar, pr_date])
            if is_ajax():
                return jsonify(details if details else [])
            return render_template('prescription_details.html', details=details)
        except Exception as e:
            app.logger.error(f"Error fetching prescription details: {str(e)}")
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 500
            flash(f'Error: {str(e)}', 'error')
    return render_template('prescription_details.html')

@app.route('/company_drugs/<pc_name>')
def company_drugs(pc_name):
    try:
        drugs = execute_procedure('pc_production', [pc_name])
        return jsonify(drugs if drugs else [])
    except Exception as e:
        app.logger.error(f"Error fetching company drugs: {str(e)}")
        return jsonify([]), 500

@app.route('/pharmacy_stock/<ph_name>')
def pharmacy_stock(ph_name):
    try:
        stock = execute_procedure('ph_stock', [ph_name])
        return jsonify(stock if stock else [])
    except Exception as e:
        app.logger.error(f"Error fetching pharmacy stock: {str(e)}")
        return jsonify([]), 500

@app.route('/doctor_patients/<d_aadhar>')
def doctor_patients(d_aadhar):
    try:
        patients = execute_procedure('d_patient', [d_aadhar])
        return jsonify(patients if patients else [])
    except Exception as e:
        app.logger.error(f"Error fetching doctor's patients: {str(e)}")
        return jsonify([]), 500

@app.route('/test_db')
def test_db():
    try:
        # Test database connection
        conn = get_db_connection()
        if conn is None:
            return "Database connection failed!", 500
        
        # Test if we can execute a simple procedure
        result = execute_procedure('get_pharmacies')
        if result is None:
            return "Could not execute procedure!", 500
            
        return jsonify({
            "status": "success",
            "message": "Database connection successful",
            "data": result
        })
    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500

@app.route('/test')
def test():
    return "Flask is working!"

@app.route('/add_prescription_drug', methods=['POST'])
def add_prescription_drug():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            trade_name = request.form['trade_name']
            pr_no = request.form['pr_no']
            quantity = request.form['quantity']
            
            result = execute_procedure('add_presc_drug', [pc_name, trade_name, pr_no, quantity])
            if result is not None:
                flash('Medication added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding medication', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('prescriptions'))

@app.route('/prescription_drugs/<pr_no>')
def prescription_drugs(pr_no):
    try:
        # Get medications for a prescription
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT pd.pc_name, pd.trade_name, pd.quantity
            FROM Prescription_Drugs pd
            WHERE pd.pr_no = %s
        """, (pr_no,))
        medications = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify(medications if medications else [])
    except Exception as e:
        app.logger.error(f"Error fetching prescription drugs: {str(e)}")
        return jsonify([]), 500

@app.route('/delete_prescription_drug/<pc_name>/<trade_name>/<pr_no>', methods=['DELETE'])
def delete_prescription_drug(pc_name, trade_name, pr_no):
    try:
        # Convert pr_no to integer
        result = execute_procedure('del_pres_drug', [pc_name, trade_name, int(pr_no)])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting prescription drug: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    # Print some debug information
    print(f"Current directory: {os.getcwd()}")
    print(f"Template folder: {os.path.join(basedir, 'templates')}")
    print(f"Static folder: {os.path.join(basedir, 'static')}")
    
    try:
        app.run(debug=True, port=2025)  # Using port 2025 directly
    except OSError as e:
        print(f"Error: {e}")
        print("Please manually specify an available port.")
