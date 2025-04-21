document.addEventListener('DOMContentLoaded', function() {
    // Initialize DataTable with proper configuration
    const drugsTable = $('#drugsTable').DataTable({
        processing: true,
        serverSide: false,
        ajax: {
            url: '/drugs',
            dataSrc: function(json) {
                return json || [];
            }
        },
        columns: [
            { data: 'trade_name' },
            { data: 'pc_name' },
            { data: 'formula' },
            {
                data: null,
                orderable: false,
                render: function(data, type, row) {
                    return `
                        <div class="btn-group" role="group">
                            <button type="button" class="btn btn-sm btn-outline-primary edit-btn" 
                                    data-pc-name="${row.pc_name}" data-trade-name="${row.trade_name}">
                                <i class="fas fa-edit"></i>
                            </button>
                            <button type="button" class="btn btn-sm btn-outline-danger delete-btn" 
                                    data-pc-name="${row.pc_name}" data-trade-name="${row.trade_name}">
                                <i class="fas fa-trash"></i>
                            </button>
                        </div>
                    `;
                }
            }
        ],
        language: {
            search: "",
            searchPlaceholder: "Search drugs...",
            emptyTable: "No drugs available",
            info: "Showing _START_ to _END_ of _TOTAL_ drugs",
            lengthMenu: "Show _MENU_ drugs per page"
        },
        dom: '<"row"<"col-sm-12 col-md-6"l><"col-sm-12 col-md-6"f>>rtip',
        responsive: true
    });

    // Add Drug button click handler
    $('#addDrugBtn').on('click', function() {
        $('#modalTitle').text('Add New Drug');
        $('#drugForm').trigger('reset');
        $('#drugForm').removeData('edit-pc-name').removeData('edit-trade-name');
        
        // Load companies for dropdown
        loadCompanies();
        
        const drugModal = new bootstrap.Modal(document.getElementById('drugModal'));
        drugModal.show();
    });
    
    // Save button click handler
    $('#saveButton').on('click', function() {
        // Validate form
        if (!$('#drugForm')[0].checkValidity()) {
            $('#drugForm')[0].reportValidity();
            return;
        }
        
        // Collect form data
        const formData = new FormData();
        formData.append('pc_name', $('#manufacturer').val());
        formData.append('trade_name', $('#drugName').val());
        formData.append('formula', $('#category').val() || '');
        
        // Determine if this is an add or edit operation
        const isEdit = $('#drugForm').data('edit-pc-name') && $('#drugForm').data('edit-trade-name');
        const url = isEdit ? '/update_drug' : '/add_drug';
        
        // Send data to server
        fetch(url, {
            method: 'POST',
            body: formData
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Server error');
            }
            return response.json();
        })
        .then(data => {
            if (data.success) {
                // Close modal
                bootstrap.Modal.getInstance(document.getElementById('drugModal')).hide();
                
                // Show success message
                showAlert(`Drug ${isEdit ? 'updated' : 'added'} successfully!`, 'success');
                
                // Reload table data
                drugsTable.ajax.reload();
            } else {
                throw new Error(data.error || 'Operation failed');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            showAlert(`Error: ${error.message}`, 'danger');
        });
    });
    
    // Handle edit button clicks
    $('#drugsTable').on('click', '.edit-btn', function() {
        const pcName = $(this).data('pc-name');
        const tradeName = $(this).data('trade-name');
        
        // Store drug info in the form for later use
        $('#drugForm').data('edit-pc-name', pcName);
        $('#drugForm').data('edit-trade-name', tradeName);
        
        // Load companies first
        loadCompanies().then(() => {
            // Then populate form with drug data from the row
            const row = drugsTable.row($(this).closest('tr')).data();
            $('#drugName').val(row.trade_name);
            $('#manufacturer').val(row.pc_name);
            $('#category').val(row.formula || '');
            
            // Set form to edit mode
            $('#modalTitle').text('Edit Drug');
            
            // Show modal
            const drugModal = new bootstrap.Modal(document.getElementById('drugModal'));
            drugModal.show();
        });
    });
    
    // Handle delete button clicks
    $('#drugsTable').on('click', '.delete-btn', function() {
        const pcName = $(this).data('pc-name');
        const tradeName = $(this).data('trade-name');
        
        if (confirm(`Are you sure you want to delete drug "${tradeName}" from "${pcName}"?`)) {
            fetch(`/delete_drug/${pcName}/${tradeName}`, {
                method: 'DELETE'
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Server error');
                }
                return response.json();
            })
            .then(data => {
                if (data.success) {
                    showAlert('Drug deleted successfully!', 'success');
                    drugsTable.ajax.reload();
                } else {
                    throw new Error(data.error || 'Delete failed');
                }
            })
            .catch(error => {
                console.error('Error:', error);
                showAlert(`Failed to delete drug: ${error.message}`, 'danger');
            });
        }
    });
    
    // Function to load pharmaceutical companies for the dropdown
    function loadCompanies() {
        return fetch('/companies')
            .then(response => response.json())
            .then(data => {
                const select = document.getElementById('manufacturer');
                select.innerHTML = '<option value="">Select Company</option>';
                data.forEach(company => {
                    const option = document.createElement('option');
                    option.value = company.pc_name;
                    option.textContent = company.pc_name;
                    select.appendChild(option);
                });
                return data;
            })
            .catch(error => {
                console.error('Error loading companies:', error);
                showAlert('Failed to load companies. Please refresh the page.', 'danger');
            });
    }
}); 