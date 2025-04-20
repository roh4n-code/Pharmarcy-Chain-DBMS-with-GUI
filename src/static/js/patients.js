document.addEventListener('DOMContentLoaded', function() {
    const addPatientBtn = document.getElementById('addPatientBtn');
    const patientModal = document.getElementById('patientModal');
    const patientForm = document.getElementById('patientForm');
    const patientsTable = document.getElementById('patientsTable').getElementsByTagName('tbody')[0];

    // Handle Add Patient button click
    addPatientBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Patient';
        patientForm.reset();
        patientModal.style.display = 'block';
    });

    // Handle form submission
    patientForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('patName').value,
            dob: document.getElementById('dob').value,
            contact: document.getElementById('patContact').value,
            email: document.getElementById('patEmail').value,
            address: document.getElementById('patAddress').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        patientsTable.innerHTML = '<tr><td colspan="6">Loading patient data...</td></tr>';
        
        // Close modal
        patientModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    patientsTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const patientId = row.getAttribute('data-patient-id');
            
            // TODO: Fetch patient data from server using patientId
            console.log('Editing patient:', patientId);
            
            document.getElementById('modalTitle').textContent = 'Edit Patient';
            patientModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const patientId = row.getAttribute('data-patient-id');
            
            if (confirm('Are you sure you want to delete this patient?')) {
                // TODO: Send delete request to server
                console.log('Deleting patient:', patientId);
            }
        }
    });
}); 