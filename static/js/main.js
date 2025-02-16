document.addEventListener('DOMContentLoaded', function() {
    console.log("Initializing map...");
    // Initialize the Leaflet map centered on Metro Manila, Philippines
    var map = L.map('map').setView([14.5995, 120.9842], 13);
  
    // Add OpenStreetMap tiles
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);
  
    // Fetch tracker data from the Flask endpoint
    fetch('/trackers/')
      .then(response => response.json())
      .then(data => {
        console.log("Tracker data fetched:", data);
        // Update the textual tracker info section (optional)
        const trackerDiv = document.getElementById('tracker-info');
        trackerDiv.innerHTML = '<h2>Tracker Information</h2>';
        
        data.forEach(tracker => {
          // Append textual tracker info for debugging/display purposes
          trackerDiv.innerHTML += `
            <div class="tracker">
              <p><strong>Pet ID:</strong> ${tracker.pet_id}</p>
              <p><strong>Last Seen Location:</strong> ${tracker.last_seen_location}</p>
              <p><strong>Last Seen Time:</strong> ${tracker.last_seen_time}</p>
              <p><strong>Status:</strong> ${tracker.status}</p>
            </div>
            <hr/>
          `;
  
          // Parse the coordinate string "lat, lon"
          let coords = tracker.last_seen_location.split(',');
          if (coords.length === 2) {
            let lat = parseFloat(coords[0].trim());
            let lon = parseFloat(coords[1].trim());
            if (!isNaN(lat) && !isNaN(lon)) {
              // Create the popup content with a placeholder image and pet details
              let popupContent = `
                <div style="text-align:center;">
                  <img src="https://via.placeholder.com/100" alt="Pet Image" style="width:100px; height:100px; border-radius:50%; margin-bottom:10px;">
                  <h3>${tracker.pet_name}</h3>
                  <p><strong>Type:</strong> ${tracker.pet_type}</p>
                  <p><strong>Breed:</strong> ${tracker.pet_breed}</p>
                  <p><strong>Gender:</strong> ${tracker.pet_gender}, <strong>Age:</strong> ${tracker.pet_age}</p>
                  <p><strong>Status:</strong> ${tracker.status}</p>
                  <p><strong>Last Seen:</strong> ${tracker.last_seen_time}</p>
                  <p><strong>Description:</strong> ${tracker.pet_description}</p>
                </div>
              `;
              console.log("Adding marker for pet:", tracker.pet_name, "at", lat, lon);
              // Add the marker to the map with the popup
              L.marker([lat, lon]).addTo(map)
                .bindPopup(popupContent);
            } else {
              console.warn("Invalid coordinates for tracker:", tracker);
            }
          } else {
            console.warn("Invalid coordinate format for tracker:", tracker);
          }
        });
      })
      .catch(error => {
        console.error('Error fetching tracker info:', error);
      });
  });
  