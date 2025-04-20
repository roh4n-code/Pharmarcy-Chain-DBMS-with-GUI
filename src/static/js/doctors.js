document.addEventListener('DOMContentLoaded', function() {
    const addDoctorBtn = document.getElementById('addDoctorBtn');
    const doctorModal = document.getElementById('doctorModal');
    const doctorForm = document.getElementById('doctorForm');
    const doctorsTable = document.getElementById('doctorsTable').getElementsByTagName('tbody')[0];

    // Handle Add Doctor button click
    addDoctorBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Doctor';
        doctorForm.reset();
        doctorModal.style.display = 'block';
    });

    // Handle form submission
    doctorForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('docName').value,
            specialization: document.getElementById('specialization').value,
            contact: document.getElementById('docContact').value,
            email: document.getElementById('docEmail').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        doctorsTable.innerHTML = '<tr><td colspan="5">Loading doctor data...</td></tr>';
        
        // Close modal
        doctorModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    doctorsTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const doctorId = row.getAttribute('data-doctor-id');
            
            // TODO: Fetch doctor data from server using doctorId
            console.log('Editing doctor:', doctorId);
            
            document.getElementById('modalTitle').textContent = 'Edit Doctor';
            doctorModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const doctorId = row.getAttribute('data-doctor-id');
            
            if (confirm('Are you sure you want to delete this doctor?')) {
                // TODO: Send delete request to server
                console.log('Deleting doctor:', doctorId);
            }
        }
    });
}); 