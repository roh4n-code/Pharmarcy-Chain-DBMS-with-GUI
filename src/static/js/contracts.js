document.addEventListener('DOMContentLoaded', function() {
    const addContractBtn = document.getElementById('addContractBtn');
    const contractModal = document.getElementById('contractModal');
    const contractForm = document.getElementById('contractForm');
    const contractsTable = document.getElementById('contractsTable').getElementsByTagName('tbody')[0];
    const pharmacySelect = document.getElementById('pharmacy');
    const companySelect = document.getElementById('company');

    // Load pharmacies and companies (this would typically come from an API)
    function loadSelectOptions() {
        // TODO: Replace with actual API calls
        const pharmacies = [
            { id: 1, name: 'Main Street Pharmacy' },
            { id: 2, name: 'Downtown Pharmacy' },
            { id: 3, name: 'Westside Pharmacy' }
        ];

        const companies = [
            { id: 1, name: 'Pfizer' },
            { id: 2, name: 'Johnson & Johnson' },
            { id: 3, name: 'Novartis' }
        ];

        // Load pharmacies
        pharmacySelect.innerHTML = '<option value="">Select Pharmacy</option>';
        pharmacies.forEach(pharmacy => {
            const option = document.createElement('option');
            option.value = pharmacy.id;
            option.textContent = pharmacy.name;
            pharmacySelect.appendChild(option);
        });

        // Load companies
        companySelect.innerHTML = '<option value="">Select Company</option>';
        companies.forEach(company => {
            const option = document.createElement('option');
            option.value = company.id;
            option.textContent = company.name;
            companySelect.appendChild(option);
        });
    }

    // Handle Add Contract button click
    addContractBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Contract';
        contractForm.reset();
        contractModal.style.display = 'block';
    });

    // Handle form submission
    contractForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            pharmacy: pharmacySelect.value,
            company: companySelect.value,
            startDate: document.getElementById('startDate').value,
            endDate: document.getElementById('endDate').value,
            status: document.getElementById('status').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);
        
        // Show loading state
        contractsTable.innerHTML = '<tr><td colspan="6">Loading contract data...</td></tr>';
        
        // Close modal
        contractModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    contractsTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const contractId = row.getAttribute('data-contract-id');
            
            // TODO: Fetch contract data from server using contractId
            console.log('Editing contract:', contractId);
            
            document.getElementById('modalTitle').textContent = 'Edit Contract';
            contractModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            const row = e.target.closest('tr');
            const contractId = row.getAttribute('data-contract-id');
            
            if (confirm('Are you sure you want to delete this contract?')) {
                // TODO: Send delete request to server
                console.log('Deleting contract:', contractId);
            }
        }
    });

    // Load initial data
    loadSelectOptions();
}); 