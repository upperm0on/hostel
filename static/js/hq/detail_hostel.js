document.addEventListener("DOMContentLoaded", () => {
  var view_room_btn = document.querySelectorAll(".room_info_btn");

  view_room_btn.forEach((room) => {
    // Create overlay (for dark background effect)
    let overlay = document.createElement("div");
    overlay.style.position = "fixed";
    overlay.style.top = "0";
    overlay.style.left = "0";
    overlay.style.width = "100vw";
    overlay.style.height = "100vh";
    overlay.style.backgroundColor = "rgba(0, 0, 0, 0.6)";
    overlay.style.zIndex = "999";
    overlay.style.display = "none"; // Hidden by default

    // Append the overlay to the body
    document.body.appendChild(overlay);

    // Create the modal (dialogue box)
    let dialogue = document.createElement("div");
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

    // Create a close button
    let closeButton = document.createElement("button");
    closeButton.innerHTML = "&times;";
    closeButton.style.position = "absolute";
    closeButton.style.top = "10px";
    closeButton.style.right = "10px";
    closeButton.style.backgroundColor = "transparent";
    closeButton.style.border = "none";
    closeButton.style.fontSize = "20px";
    closeButton.style.cursor = "pointer";
    closeButton.style.color = "#333";

    // Add click event to close the modal and remove overlay
    const closeModal = () => {
      dialogue.style.display = "none";
      overlay.style.display = "none";
      document.body.style.overflow = "auto"; // Enable background scroll again
    };

    closeButton.addEventListener("click", closeModal);

    // Set the content for the modal (image and room details)
    let roomImage = document.createElement("img");
    roomImage.src = `/media/room_images/${room.dataset.hostelName}/${room.dataset.roomInfo}/${room.dataset.roomImage}`;
    roomImage.alt = "Room Image";
    roomImage.style.width = "60%"; // Occupies 60% of the modal
    roomImage.style.height = "450px";
    roomImage.style.objectFit = "cover";
    roomImage.style.float = "left";

    // Create a content section for the text (room details)
    let contentSection = document.createElement("div");
    contentSection.style.padding = "20px";
    contentSection.style.width = "40%"; // The rest of the modal
    contentSection.style.float = "right";

    contentSection.innerHTML = `
            <h3>Room Information</h3>
            <p><strong>Price:</strong> ${room.dataset.price} GHC</p>
            <p><strong>Amenities:</strong> ${room.dataset.amenities}</p> 
            <p><strong>Rules:</strong> ${room.dataset.rules}</p>
        `;

    // Append the image, content section, and close button to the modal
    dialogue.appendChild(roomImage);
    dialogue.appendChild(contentSection);
    dialogue.appendChild(closeButton);

    // Append the modal to the body
    document.body.appendChild(dialogue);

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
