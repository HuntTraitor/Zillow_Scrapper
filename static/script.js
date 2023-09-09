let zipGallery;

fetch('/get_zips')
    .then(response => response.json())
    .then(zipGraphs => {
        zipGallery = zipGraphs.map(zipGraphs => zipGraphs.replace('.png', '')); // Assign zipGraphs to zipGallery
        populateDropdown();
    })
    .catch(error => console.error('Error:', error));

const populateDropdown = () => {
    const dropdown = document.getElementById("zip-dropdown");

    if (zipGallery) { // Check if zipGallery is defined
        zipGallery.forEach(zip => {
            const listItem = document.createElement("li");
            const link = document.createElement("a");
            link.href = zip;
            link.className = "dropdown-item";
            link.textContent = zip;

            listItem.appendChild(link);
            dropdown.appendChild(listItem);
        });
    } else {
        console.error('zipGallery is not defined'); // Handle the case where zipGallery is not defined
    }
};

