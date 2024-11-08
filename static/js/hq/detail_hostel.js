document.addEventListener("DOMContentLoaded", () => {
  const view_room_btn = document.querySelectorAll(".room_info_btn");

  view_room_btn.forEach((room) => {
    // Create overlay for the dark background effect
    const overlay = document.createElement("div");
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100vw";
    overlay.style.height = "100vh";
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.6)";
    overlay.style.zIndex = "999";
    overlay.style.display = "none"; // Hidden by default
    document.body.appendChild(overlay);

    // Create the modal (dialogue box)
    const dialogue = document.createElement("div");
    dialogue.style.position = "fixed";
    dialogue.style.left = "50vw";
    dialogue.style.top = "50vh";
    dialogue.style.transform = "translate(-50%, -50%)";
    dialogue.style.height = "450px";
    dialogue.style.width = "600px";
    dialogue.style.borderRadius = "8px";
    dialogue.style.boxShadow = "0 4px 20px rgba(0, 0, 0, 0.1)";
    dialogue.style.backgroundColor = "#fff";
    dialogue.style.overflowY = "auto"; // Enable vertical scroll for the modal
    dialogue.style.zIndex = "1000";
    dialogue.style.display = "none"; // Hidden by default
    document.body.appendChild(dialogue);

    // Create a close button
    const closeButton = document.createElement("button");
    closeButton.innerHTML = "&times;";
    closeButton.style.position = "absolute";
    closeButton.style.top = "10px";
    closeButton.style.right = "10px";
    closeButton.style.backgroundColor = "transparent";
    closeButton.style.border = "none";
    closeButton.style.fontSize = "20px";
    closeButton.style.cursor = "pointer";
    closeButton.style.color = "#333";

    const closeModal = () => {
      dialogue.style.display = "none";
      overlay.style.display = "none";
      document.body.style.overflow = "auto"; // Enable background scroll again
    };

    closeButton.addEventListener("click", closeModal);

    // Set the content for the modal (image and room details)
    const roomImage = document.createElement("img");
    roomImage.src = `/media/room_images/${room.dataset.hostelName}/${room.dataset.roomInfo}/${room.dataset.roomImage}`;
    roomImage.alt = "Room Image";
    roomImage.style.width = "60%"; // Occupies 60% of the modal
    roomImage.style.height = "450px";
    roomImage.style.objectFit = "cover";
    roomImage.style.float = "left";

    // Create a content section for the text (room details)
    const contentSection = document.createElement("div");
    contentSection.style.padding = "20px";
    contentSection.style.width = "40%"; // The rest of the modal
    contentSection.style.float = "right";

    // Parse amenities from the dataset
    const roomAmenities = JSON.parse(room.dataset.amenities);
    
    // Create amenities list and populate it
    const amenityList = document.createElement("ul");
    roomAmenities.forEach((amenity) => {
      const listItem = document.createElement("li");
      listItem.textContent = amenity;
      amenityList.appendChild(listItem);
    });

    // Add room details to the content section, including amenities list
    contentSection.innerHTML = `
      <h3>Room Information</h3>
      <p><strong>Price:</strong> ${room.dataset.price} GHC</p>
      <p><strong>Amenities:</strong></p>
    `;
    contentSection.appendChild(amenityList); // Append the amenities list below the "Amenities" label

    // Create the confirm purchase button
    const confirmButton = document.createElement("button");
    confirmButton.type = "button";
    confirmButton.classList.add("confirm_purchase", "btn", "btn-warning", "m-3");
    confirmButton.textContent = "Confirm Purchase";

    // Event listener for the confirm button
    confirmButton.addEventListener("click", () => {
      const hostelId = room.dataset.hostelName; // Retrieve hostel_id from data attribute
      const room_id = room.dataset.roomInfo

      // Send a POST request with hostel_id to set session variable
      fetch(`/hq/confirm_payment/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken"),  // CSRF token is necessary for secure requests
        },
        body: JSON.stringify({ confirm: true, hostel_id: hostelId, room_id: room_id })  // Include hostel_id in the payload
      })
      .then(response => response.json())
      .then(data => {
        if (data.message) {
          alert(data.message);  // Alert success message
          closeModal();  // Close the modal after confirmation
        } else {
          alert("An error occurred.");
        }
      })
      .catch(error => console.error("Error:", error));
      window.location.href = '/dashboard/'
    });

    // Append elements to contentSection and dialogue
    contentSection.appendChild(confirmButton);
    dialogue.appendChild(roomImage);
    dialogue.appendChild(contentSection);
    dialogue.appendChild(closeButton);

    // Show the modal and overlay when the button is clicked
    room.addEventListener("mouseup", () => {
      dialogue.style.display = "block";
      overlay.style.display = "block";
      document.body.style.overflow = "hidden"; // Disable background scroll
    });

    // Close modal when clicking on the overlay
    overlay.addEventListener("click", closeModal);
  });
});

// Helper function to get the CSRF token from cookies
function getCookie(name) {
  const cookieValue = document.cookie
    .split("; ")
    .find(row => row.startsWith(name + "="))
    ?.split("=")[1];
  return cookieValue;
}