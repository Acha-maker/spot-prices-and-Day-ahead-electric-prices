// Function to load electricity prices from the Python backend API
async function loadPrices() {
    try {
        // Make an API call to the Flask backend (assuming the Flask server is running)
       
       
       
        const response = await fetch('http://127.0.0.1:5000/api/prices');  // API endpoint from the Flask server
        const data = await response.json();  // Parse the response as JSON

        const tableBody = document.querySelector('#prices-table tbody');
        tableBody.innerHTML = '';  // Clear existing rows

        // Loop through the prices and append rows to the table
        data.prices.forEach(price => {
            const row = document.createElement('tr');
            const timeCell = document.createElement('td');
            const priceCell = document.createElement('td');

            timeCell.textContent = price.time;
            priceCell.textContent = price.price;

            row.appendChild(timeCell);
            row.appendChild(priceCell);

            tableBody.appendChild(row);
        });
    } catch (error) {
        console.error('Error fetching prices:', error);
    }
}

// Load prices when the page is loaded
window.onload = loadPrices;
