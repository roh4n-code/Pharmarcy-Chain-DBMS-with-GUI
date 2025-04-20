// pharma-companies.js

document.addEventListener('DOMContentLoaded', function() {
    // DOM elements
    const companiesTable = document.getElementById('companiesTable');
    const addCompanyBtn = document.getElementById('addCompanyBtn');
    const companyModal = document.getElementById('companyModal');
    const companyForm = document.getElementById('companyForm');
    const modalTitle = document.getElementById('modalTitle');
    const closeButtons = document.querySelectorAll('.close, .close-modal');
    
    // Event listeners
    addCompanyBtn.addEventListener('click', openAddCompanyModal);
    companyForm.addEventListener('submit', handleCompanySubmit);
    closeButtons.forEach(btn => btn.addEventListener('click', closeModal));
    
    // Load companies on page load
    loadCompanies();
    
    // Functions
    function openAddCompanyModal() {
        modalTitle.textContent = 'Add New Pharmaceutical Company';
        companyForm.reset();
        companyModal.style.display = 'block';
    }
    
    function openEditCompanyModal(companyName, contact) {
        modalTitle.textContent = 'Edit Pharmaceutical Company';
        document.getElementById('pcName').value = companyName;
        document.getElementById('pcName').readOnly = true; // Can't change primary key
        document.getElementById('pcContact').value = contact;
        companyModal.style.display = 'block';
    }
    
    function closeModal() {
        companyModal.style.display = 'none';
    }
    
    async function loadCompanies() {
        try {
            const response = await fetch('/api/pharma-companies');
            if (!response.ok) throw new Error('Failed to load companies');
            
            const companies = await response.json();
            renderCompaniesTable(companies);
        } catch (error) {
            console.error('Error loading companies:', error);
            alert('Error loading pharmaceutical companies. Please try again.');
        }
    }
    
    function renderCompaniesTable(companies) {
        const tbody = companiesTable.querySelector('tbody');
        tbody.innerHTML = '';
        
        companies.forEach(company => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${company.pc_name}</td>
                <td>${company.pc_contact || '-'}</td>
                <td>
                    <button class="btn-edit" data-name="${company.pc_name}" data-contact="${company.pc_contact || ''}">Edit</button>
                    <button class="btn-delete" data-name="${company.pc_name}">Delete</button>
                </td>
            `;
            
            tbody.appendChild(row);
        });
        
        // Add event listeners to edit and delete buttons
        document.querySelectorAll('.btn-edit').forEach(btn => {
            btn.addEventListener('click', function() {
                const name = this.getAttribute('data-name');
                const contact = this.getAttribute('data-contact');
                openEditCompanyModal(name, contact);
            });
        });
        
        document.querySelectorAll('.btn-delete').forEach(btn => {
            btn.addEventListener('click', async function() {
                const name = this.getAttribute('data-name');
                if (confirm(`Are you sure you want to delete ${name}?`)) {
                    await deleteCompany(name);
                }
            });
        });
    }
    
    async function handleCompanySubmit(event) {
        event.preventDefault();
        
        const formData = {
            pc_name: document.getElementById('pcName').value,
            pc_contact: document.getElementById('pcContact').value
        };
        
        const isEdit = document.getElementById('pcName').readOnly;
        
        try {
            let response;
            if (isEdit) {
                response = await fetch(`/api/pharma-companies/${formData.pc_name}`, {
                    method: 'PUT',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });
            } else {
                response = await fetch('/api/pharma-companies', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(formData)
                });
            }
            
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Operation failed');
            }
            
            closeModal();
            loadCompanies();
            alert(isEdit ? 'Company updated successfully!' : 'Company added successfully!');
        } catch (error) {
            console.error('Error:', error);
            alert(`Error: ${error.message}`);
        }
    }
    
    async function deleteCompany(companyName) {
        try {
            const response = await fetch(`/api/pharma-companies/${companyName}`, {
                method: 'DELETE'
            });
            
            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || 'Delete operation failed');
            }
            
            loadCompanies();
            alert('Company deleted successfully!');
        } catch (error) {
            console.error('Error deleting company:', error);
            alert(`Error: ${error.message}`);
        }
    }
});

// Common functionality for the application
document.addEventListener('DOMContentLoaded', function() {
    // Handle modal close buttons
    const closeButtons = document.querySelectorAll('.close, .close-modal');
    closeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const modal = this.closest('.modal');
            if (modal) {
                modal.style.display = 'none';
            }
        });
    });

    // Handle window close button
    window.addEventListener('click', function(event) {
        if (event.target.classList.contains('modal')) {
            event.target.style.display = 'none';
        }
    });

    // Handle navigation active state
    const currentPath = window.location.pathname;
    const navLinks = document.querySelectorAll('nav ul li a');
    navLinks.forEach(link => {
        if (link.getAttribute('href') === currentPath) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
});