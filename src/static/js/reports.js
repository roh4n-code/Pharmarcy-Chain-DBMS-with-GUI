document.addEventListener('DOMContentLoaded', function() {
    const reportForm = document.getElementById('reportForm');
    const reportTypeSelect = document.getElementById('reportType');
    const dateRangeSelect = document.getElementById('dateRange');
    const customDateRange = document.querySelector('.custom-date-range');
    const pharmacySelect = document.getElementById('pharmacy');
    const reportResults = document.querySelector('.report-results');
    const reportTable = document.getElementById('reportTable');
    const reportTitle = document.getElementById('reportTitle');
    const exportPDFBtn = document.getElementById('exportPDF');
    const exportCSVBtn = document.getElementById('exportCSV');

    // Load pharmacies
    function loadPharmacies() {
        // TODO: Replace with actual API call
        const pharmacies = [
            { id: 1, name: 'Main Street Pharmacy' },
            { id: 2, name: 'Downtown Pharmacy' },
            { id: 3, name: 'Westside Pharmacy' }
        ];

        pharmacies.forEach(pharmacy => {
            const option = document.createElement('option');
            option.value = pharmacy.id;
            option.textContent = pharmacy.name;
            pharmacySelect.appendChild(option);
        });
    }

    // Handle date range selection
    dateRangeSelect.addEventListener('change', function() {
        if (this.value === 'custom') {
            customDateRange.style.display = 'block';
        } else {
            customDateRange.style.display = 'none';
        }
    });

    // Handle form submission
    reportForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const formData = {
            reportType: reportTypeSelect.value,
            dateRange: dateRangeSelect.value,
            startDate: document.getElementById('startDate').value,
            endDate: document.getElementById('endDate').value,
            pharmacy: pharmacySelect.value
        };

        // TODO: Send data to server and get report data
        console.log('Form submitted:', formData);
        
        // Show loading state
        reportResults.style.display = 'block';
        reportTable.innerHTML = '<tr><td colspan="5">Loading report data...</td></tr>';
    });

    // Handle export buttons
    exportPDFBtn.addEventListener('click', function() {
        // TODO: Implement PDF export through server
        alert('PDF export will be implemented soon');
    });

    exportCSVBtn.addEventListener('click', function() {
        // TODO: Implement CSV export through server
        alert('CSV export will be implemented soon');
    });

    // Load initial data
    loadPharmacies();
}); 