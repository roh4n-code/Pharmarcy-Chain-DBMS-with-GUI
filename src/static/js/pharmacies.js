document.addEventListener('DOMContentLoaded', function() {
    const addPharmacyBtn = document.getElementById('addPharmacyBtn');
    const pharmacyModal = document.getElementById('pharmacyModal');
    const pharmacyForm = document.getElementById('pharmacyForm');
    const pharmaciesTable = document.getElementById('pharmaciesTable').getElementsByTagName('tbody')[0];

    // Handle Add Pharmacy button click
    addPharmacyBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Pharmacy';
        pharmacyForm.reset();
        pharmacyModal.style.display = 'block';
    });

    // Handle form submission
    pharmacyForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('phName').value,
            address: document.getElementById('phAddress').value,
            contact: document.getElementById('phContact').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        pharmaciesTable.innerHTML = '<tr><td colspan="4">Loading pharmacy data...</td></tr>';
        
        // Close modal
        pharmacyModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    pharmaciesTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const pharmacyId = row.getAttribute('data-pharmacy-id');
            
            // TODO: Fetch pharmacy data from server using pharmacyId
            console.log('Editing pharmacy:', pharmacyId);
            
            document.getElementById('modalTitle').textContent = 'Edit Pharmacy';
            pharmacyModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const pharmacyId = row.getAttribute('data-pharmacy-id');
            
            if (confirm('Are you sure you want to delete this pharmacy?')) {
                // TODO: Send delete request to server
                console.log('Deleting pharmacy:', pharmacyId);
            }
        }
    });
}); 