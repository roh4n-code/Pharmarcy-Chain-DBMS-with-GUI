document.addEventListener('DOMContentLoaded', function() {
    const addPrescriptionBtn = document.getElementById('addPrescriptionBtn');
    const prescriptionModal = document.getElementById('prescriptionModal');
    const prescriptionForm = document.getElementById('prescriptionForm');
    const prescriptionsTable = document.getElementById('prescriptionsTable').getElementsByTagName('tbody')[0];
    const patientSelect = document.getElementById('patientSelect');
    const doctorSelect = document.getElementById('doctorSelect');
    const drugSelect = document.getElementById('drugSelect');

    // Function to load select options
    function loadSelectOptions() {
        // TODO: Load these from the server
        const patients = [
            { id: 1, name: 'John Doe' },
            { id: 2, name: 'Jane Smith' },
            { id: 3, name: 'Bob Johnson' }
        ];

        const doctors = [
            { id: 1, name: 'Dr. Sarah Wilson' },
            { id: 2, name: 'Dr. Michael Brown' },
            { id: 3, name: 'Dr. Emily Davis' }
        ];

        const drugs = [
            { id: 1, name: 'Aspirin' },
            { id: 2, name: 'Ibuprofen' },
            { id: 3, name: 'Paracetamol' }
        ];

        // Populate patient select
        patients.forEach(patient => {
            const option = document.createElement('option');
            option.value = patient.id;
            option.textContent = patient.name;
            patientSelect.appendChild(option);
        });

        // Populate doctor select
        doctors.forEach(doctor => {
            const option = document.createElement('option');
            option.value = doctor.id;
            option.textContent = doctor.name;
            doctorSelect.appendChild(option);
        });

        // Populate drug select
        drugs.forEach(drug => {
            const option = document.createElement('option');
            option.value = drug.id;
            option.textContent = drug.name;
            drugSelect.appendChild(option);
        });
    }

    // Handle Add Prescription button click
    addPrescriptionBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Prescription';
        prescriptionForm.reset();
        prescriptionModal.style.display = 'block';
    });

    // Handle form submission
    prescriptionForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            patient: patientSelect.value,
            doctor: doctorSelect.value,
            drug: drugSelect.value,
            dosage: document.getElementById('dosage').value,
            frequency: document.getElementById('frequency').value,
            startDate: document.getElementById('startDate').value,
            endDate: document.getElementById('endDate').value,
            status: document.getElementById('status').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        prescriptionsTable.innerHTML = '<tr><td colspan="9">Loading prescription data...</td></tr>';
        
        // Close modal
        prescriptionModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    prescriptionsTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const prescriptionId = row.getAttribute('data-prescription-id');
            
            // TODO: Fetch prescription data from server using prescriptionId
            console.log('Editing prescription:', prescriptionId);
            
            document.getElementById('modalTitle').textContent = 'Edit Prescription';
            prescriptionModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const prescriptionId = row.getAttribute('data-prescription-id');
            
            if (confirm('Are you sure you want to delete this prescription?')) {
                // TODO: Send delete request to server
                console.log('Deleting prescription:', prescriptionId);
            }
        }
    });

    // Load select options when page loads
    loadSelectOptions();
}); 