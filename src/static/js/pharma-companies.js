document.addEventListener('DOMContentLoaded', function() {
    const addCompanyBtn = document.getElementById('addCompanyBtn');
    const companyModal = document.getElementById('companyModal');
    const companyForm = document.getElementById('companyForm');
    const companiesTable = document.getElementById('companiesTable').getElementsByTagName('tbody')[0];

    // Handle Add Company button click
    addCompanyBtn.addEventListener('click', function() {
        document.getElementById('modalTitle').textContent = 'Add New Company';
        companyForm.reset();
        companyModal.style.display = 'block';
    });

    // Handle form submission
    companyForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        // Get form data
        const formData = {
            name: document.getElementById('compName').value,
            address: document.getElementById('compAddress').value,
            contact: document.getElementById('compContact').value,
            email: document.getElementById('compEmail').value
        };

        // TODO: Send data to server
        console.log('Form submitted:', formData);

        // For now, just add to table
        const newRow = companiesTable.insertRow();
        newRow.innerHTML = `
            <td>${formData.name}</td>
            <td>${formData.address}</td>
            <td>${formData.contact}</td>
            <td>${formData.email}</td>
            <td>
                <button class="btn-primary edit-btn">Edit</button>
                <button class="btn-secondary delete-btn">Delete</button>
            </td>
        `;

        // Close modal
        companyModal.style.display = 'none';
    });

    // Handle edit and delete buttons
    companiesTable.addEventListener('click', function(e) {
        if (e.target.classList.contains('edit-btn')) {
            const row = e.target.closest('tr');
            const cells = row.cells;
            
            document.getElementById('compName').value = cells[0].textContent;
            document.getElementById('compAddress').value = cells[1].textContent;
            document.getElementById('compContact').value = cells[2].textContent;
            document.getElementById('compEmail').value = cells[3].textContent;
            
            document.getElementById('modalTitle').textContent = 'Edit Company';
            companyModal.style.display = 'block';
        } else if (e.target.classList.contains('delete-btn')) {
            if (confirm('Are you sure you want to delete this company?')) {
                e.target.closest('tr').remove();
            }
        }
    });
}); 