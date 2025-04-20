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
            # Use stored procedure instead of direct SQL query
            pharmacies_list = execute_procedure('get_pharmacies')
            
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

@app.route('/update_pharmacy', methods=['POST'])
def update_pharmacy():
    if request.method == 'POST':
        try:
            old_ph_name = request.form['old_ph_name']
            ph_name = request.form['ph_name']
            ph_add = request.form['ph_add']
            ph_contact = request.form['ph_contact']
            
            # The update_ph procedure expects only the ph_name to update (not the old name)
            # and then the new values for address and contact
            result = execute_procedure('update_ph', [ph_name, ph_add, ph_contact])
            if result is not None:
                flash('Pharmacy updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating pharmacy', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('pharmacies'))

# Pharmaceutical Company routes
@app.route('/companies')
def companies():
    if is_ajax():
        try:
            # Use stored procedure instead of direct SQL query
            companies_list = execute_procedure('get_companies')
            
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

@app.route('/update_company', methods=['POST'])
def update_company():
    if request.method == 'POST':
        try:
            old_pc_name = request.form['old_pc_name']
            pc_name = request.form['pc_name']
            pc_contact = request.form['pc_contact']
            
            # The stored procedure expects pc_name and pc_contact only
            result = execute_procedure('update_pc', [pc_name, pc_contact])
            if result is not None:
                flash('Company updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating company', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('companies'))

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
            years_of_exp = int(request.form['years_of_exp'])
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
        except ValueError:
            flash('Years of experience must be a number greater than 0', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': 'Years of experience must be a number'}), 400
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

@app.route('/update_doctor', methods=['POST'])
def update_doctor():
    if request.method == 'POST':
        try:
            d_aadhar = request.form['d_aadhar']
            d_name = request.form['d_name']
            spec = request.form['spec']
            years_of_exp = int(request.form['years_of_exp'])
            
            # The stored procedure expects name, specialization, years of experience, and then aadhar
            result = execute_procedure('update_doc', [d_name, spec, years_of_exp, d_aadhar])
            if result is not None:
                flash('Doctor updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating doctor', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except ValueError:
            flash('Years of experience must be a number greater than 0', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': 'Years of experience must be a number'}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('doctors'))

# Patient routes
@app.route('/patients')
def patients():
    if is_ajax():
        try:
            # Use stored procedure to get full patient information
            patients_list = execute_procedure('get_patients_full')
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

@app.route('/update_patient', methods=['POST'])
def update_patient():
    if request.method == 'POST':
        try:
            p_aadhar = request.form['p_aadhar']
            p_name = request.form['p_name']
            p_add = request.form['p_add']
            p_age = request.form['p_age']
            p_doc_aid = request.form['p_doc_aid']
            
            # The procedure expects name, address, age, aadhar, doctor's aadhar
            result = execute_procedure('update_pat', [p_name, p_add, p_age, p_aadhar, p_doc_aid])
            if result is not None:
                flash('Patient updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating patient', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('patients'))

# Prescription routes
@app.route('/prescriptions')
def prescriptions():
    if is_ajax():
        try:
            # Use stored procedure to get prescription list
            prescriptions_list = execute_procedure('get_prescriptions')
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
        # Convert pr_id to integer
        result = execute_procedure('del_presc', [int(pr_id)])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting prescription: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/update_prescription', methods=['POST'])
def update_prescription():
    if request.method == 'POST':
        try:
            pr_id = request.form['pr_id']
            pr_date = request.form['pr_date']
            p_id = request.form['p_id']
            d_id = request.form['d_id']
            
            result = execute_procedure('update_presc', [int(pr_id), pr_date, p_id, d_id])
            if result is not None:
                flash('Prescription updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating prescription', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('prescriptions'))

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

@app.route('/patient_prescriptions/<p_aadhar>')
def patient_prescriptions(p_aadhar):
    try:
        prescriptions = execute_procedure('get_patient_prescriptions', [p_aadhar])
        return jsonify(prescriptions if prescriptions else [])
    except Exception as e:
        app.logger.error(f"Error fetching patient prescriptions: {str(e)}")
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
        # Use stored procedure to get prescription drugs
        medications = execute_procedure('get_prescription_drugs', [int(pr_no)])
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

@app.route('/update_prescription_drug', methods=['POST'])
def update_prescription_drug():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            trade_name = request.form['trade_name']
            pr_no = request.form['pr_no']
            quantity = request.form['quantity']
            
            result = execute_procedure('update_presc_drug', [pc_name, trade_name, int(pr_no), quantity])
            if result is not None:
                flash('Medication updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating medication', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('prescriptions'))

# Contract routes
@app.route('/contracts')
def contracts():
    if is_ajax():
        try:
            contracts_list = execute_procedure('get_contracts')
            if contracts_list is None:
                contracts_list = []
            return jsonify(contracts_list)
        except Exception as e:
            app.logger.error(f"Error fetching contracts: {str(e)}")
            return jsonify([]), 500
    return render_template('contracts.html')

@app.route('/add_contract', methods=['POST'])
def add_contract():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            ph_name = request.form['ph_name']
            supervisor = request.form['supervisor']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            
            result = execute_procedure('add_contract', [pc_name, ph_name, supervisor, start_date, end_date])
            if result is not None:
                flash('Contract added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding contract', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('contracts'))

@app.route('/update_contract', methods=['POST'])
def update_contract():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            ph_name = request.form['ph_name']
            supervisor = request.form['supervisor']
            start_date = request.form['start_date']
            end_date = request.form['end_date']
            
            # The procedure expects pc_name, start_date, end_date, content (empty), supervisor, ph_name
            # From the SQL: update_contr(IN pc_nam VARCHAR(50), start_dat DATE, end_dat DATE, conten VARCHAR(500), superviso VARCHAR(50), ph_nam VARCHAR(50))
            result = execute_procedure('update_contr', [pc_name, start_date, end_date, "", supervisor, ph_name])
            if result is not None:
                flash('Contract updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating contract', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('contracts'))

@app.route('/delete_contract/<pc_name>/<ph_name>', methods=['DELETE'])
def delete_contract(pc_name, ph_name):
    try:
        result = execute_procedure('del_contract', [pc_name, ph_name])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting contract: {str(e)}")
        return jsonify({'success': False, 'error': str(e)}), 500

# Drug routes
@app.route('/drugs')
def drugs():
    if is_ajax():
        try:
            drugs_list = execute_procedure('get_drugs')
            if drugs_list is None:
                drugs_list = []
            return jsonify(drugs_list)
        except Exception as e:
            app.logger.error(f"Error fetching drugs: {str(e)}")
            return jsonify([]), 500
    return render_template('drugs.html')

@app.route('/add_drug', methods=['POST'])
def add_drug():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            trade_name = request.form['trade_name']
            formula = request.form['formula']
            
            result = execute_procedure('add_drug', [pc_name, trade_name, formula])
            if result is not None:
                flash('Drug added successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error adding drug', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('drugs'))

@app.route('/update_drug', methods=['POST'])
def update_drug():
    if request.method == 'POST':
        try:
            pc_name = request.form['pc_name']
            trade_name = request.form['trade_name']
            formula = request.form['formula']
            
            # The stored procedure expects company name, trade name, formula
            # From SQL: update_drug(IN pc_nam VARCHAR(50), trade_nam VARCHAR(50), formul VARCHAR(50))
            result = execute_procedure('update_drug', [pc_name, trade_name, formula])
            if result is not None:
                flash('Drug updated successfully!', 'success')
                if is_ajax():
                    return jsonify({'success': True})
            else:
                flash('Error updating drug', 'error')
                if is_ajax():
                    return jsonify({'success': False}), 400
        except Exception as e:
            flash(f'Error: {str(e)}', 'error')
            if is_ajax():
                return jsonify({'success': False, 'error': str(e)}), 400
    
    if is_ajax():
        return jsonify({'success': False}), 400
    return redirect(url_for('drugs'))

@app.route('/delete_drug/<pc_name>/<trade_name>', methods=['DELETE'])
def delete_drug(pc_name, trade_name):
    try:
        result = execute_procedure('del_drug', [pc_name, trade_name])
        if result is not None:
            return jsonify({'success': True})
        return jsonify({'success': False}), 400
    except Exception as e:
        app.logger.error(f"Error deleting drug: {str(e)}")
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
