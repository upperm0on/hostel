document.addEventListener("DOMContentLoaded", () => {
  const view_room_btns = document.querySelectorAll(".room_info_btn");

  view_room_btns.forEach((room) => {
    // Create overlay for the dark background effect
    const overlay = document.createElement("div");
    Object.assign(overlay.style, {
      position: "fixed", top: "0", left: "0", width: "100vw", height: "100vh",
      backgroundColor: "rgba(0, 0, 0, 0.6)", zIndex: "999", display: "none"
    });
    document.body.appendChild(overlay);

    // Create the modal (dialogue box)
    const dialogue = document.createElement("div");
    Object.assign(dialogue.style, {
      position: "fixed", left: "50vw", top: "50vh", transform: "translate(-50%, -50%)",
      height: "450px", width: "600px", borderRadius: "8px",
      boxShadow: "0 4px 20px rgba(0, 0, 0, 0.1)", backgroundColor: "#fff",
      overflowY: "auto", zIndex: "1000", display: "none"
    });
    document.body.appendChild(dialogue);

    // Create a close button
    const closeButton = document.createElement("button");
    closeButton.innerHTML = "&times;";
    Object.assign(closeButton.style, {
      position: "absolute", top: "10px", right: "10px", backgroundColor: "transparent",
      border: "none", fontSize: "20px", cursor: "pointer", color: "#333"
    });
    closeButton.addEventListener("click", () => {
      dialogue.style.display = "none";
      overlay.style.display = "none";
      document.body.style.overflow = "auto";
    });

    // Room image
    const roomImage = document.createElement("img");
    roomImage.src = `/media/room_images/${room.dataset.hostelName}/${room.dataset.roomInfo}/${room.dataset.roomImage}`;
    roomImage.alt = "Room Image";
    Object.assign(roomImage.style, {
      width: "60%", height: "450px", objectFit: "cover", float: "left"
    });

    // Room details section
    const contentSection = document.createElement("div");
    Object.assign(contentSection.style, { padding: "20px", width: "40%", float: "right" });

    const roomAmenities = JSON.parse(room.dataset.amenities);
    const amenityList = document.createElement("ul");
    roomAmenities.forEach((amenity) => {
      const listItem = document.createElement("li");
      listItem.textContent = amenity;
      amenityList.appendChild(listItem);
    });

    contentSection.innerHTML = `<h3>Room Information</h3>
      <p><strong>Price:</strong> ${room.dataset.price} GHC</p>
      <p><strong>Amenities:</strong></p>`;
    contentSection.appendChild(amenityList);

    // Confirm Purchase button
    const confirmButton = document.createElement("button");
    confirmButton.type = "button";
    confirmButton.classList.add("confirm_purchase", "btn", "btn-warning", "m-3");
    confirmButton.textContent = "Confirm Purchase";

    // Paystack Payment Function
    function payWithPaystack() {
      const paystack = new PaystackPop();
      paystack.newTransaction({
        key: document.querySelector(".paystack_secret_key").value, // Paystack Public Key
        email: "customer@example.com", // Replace with actual customer email
        amount: parseFloat(room.dataset.price) * 100, // Amount in kobo
        currency: "GHS",
        label: "Hostel Booking Payment",
        onSuccess: function (transaction) {
          console.log("🚀 Paystack Success Response:", transaction);
          const paystackReference = transaction.reference;
          console.log("✅ Using Reference:", paystackReference);
          sendPaymentDetails(paystackReference);
        },
        onCancel: function () {
          alert("Payment cancelled!");
        }
      });
    }

    // Send Payment Details to Backend
    function sendPaymentDetails(reference) {
      fetch(`/hq/confirm_payment/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
          confirm: true,
          hostel_id: room.dataset.hostelId,
          room_id: room.dataset.roomInfo,
          reference: reference,
          amount: (room.dataset.price)
        })
      })
        .then(response => response.json())
        .then(data => {
          if (data.success) {
            alert("Payment verified successfully!");
            window.location.href = "/dashboard/";
          } else {
            alert("Payment verification failed.");
          }
        })
        .catch(error => console.error("❌ Fetch Error:", error));
    }

    confirmButton.addEventListener("click", payWithPaystack);
    contentSection.appendChild(confirmButton);
    dialogue.appendChild(roomImage);
    dialogue.appendChild(contentSection);
    dialogue.appendChild(closeButton);
    
    room.addEventListener("mouseup", () => {
      dialogue.style.display = "block";
      overlay.style.display = "block";
      document.body.style.overflow = "hidden";
    });
    overlay.addEventListener("click", () => {
      dialogue.style.display = "none";
      overlay.style.display = "none";
      document.body.style.overflow = "auto";
    });
  });
});

// Helper function to get CSRF token
function getCookie(name) {
  return document.cookie.split("; ").find(row => row.startsWith(name + "="))?.split("=")[1];
}
