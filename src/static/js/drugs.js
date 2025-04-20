document.addEventListener('DOMContentLoaded', function() {
    const addDrugBtn = document.getElementById('addDrugBtn');
    const drugModal = document.getElementById('drugModal');
    const drugForm = document.getElementById('drugForm');
    const drugsTable = document.getElementById('drugsTable').getElementsByTagName('tbody')[0];
    const manufacturerSelect = document.getElementById('manufacturer');

    // Load manufacturers (this would typically come from an API)
    function loadManufacturers() {
        // TODO: Replace with actual API call
        const manufacturers = [
            { id: 1, name: 'Pfizer' },
            { id: 2, name: 'Johnson & Johnson' },
            { id: 3, name: 'Novartis' }
        ];

        manufacturerSelect.innerHTML = '<option value="">Select Manufacturer</option>';
        manufacturers.forEach(manufacturer => {
            const option = document.createElement('option');
            option.value = manufacturer.id;
            option.textContent = manufacturer.name;
            manufacturerSelect.appendChild(option);
        });
    }

    // Handle Add Drug button click
    addDrugBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Drug';
        drugForm.reset();
        drugModal.style.display = 'block';
    });

    // Handle form submission
    drugForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            name: document.getElementById('drugName').value,
            manufacturer: manufacturerSelect.value,
            category: document.getElementById('category').value,
            price: document.getElementById('price').value,
            stock: document.getElementById('stock').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        drugsTable.innerHTML = '<tr><td colspan="6">Loading drug data...</td></tr>';
        
        // Close modal
        drugModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    drugsTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const drugId = row.getAttribute('data-drug-id');
            
            // TODO: Fetch drug data from server using drugId
            console.log('Editing drug:', drugId);
            
            document.getElementById('modalTitle').textContent = 'Edit Drug';
            drugModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const drugId = row.getAttribute('data-drug-id');
            
            if (confirm('Are you sure you want to delete this drug?')) {
                // TODO: Send delete request to server
                console.log('Deleting drug:', drugId);
            }
        }
    });

    // Load initial data
    loadManufacturers();
}); 