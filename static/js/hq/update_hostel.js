// Utility functions to handle cookies
function setCookie(name, value, days) {
    let expires = "";
    if (days) {
            const date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
    }
    document.cookie = name + "=" + (value || "") + expires + "; path=/";
}

function getCookie(name) {
    const nameEQ = name + "=";
    const ca = document.cookie.split(';');
    for (let i = 0; i < ca.length; i++) {
            let c = ca[i];
            while (c.charAt(0) === ' ') c = c.substring(1, c.length);
            if (c.indexOf(nameEQ) === 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

// Function to delete a cookie by name
function deleteCookie(name) {
    document.cookie = name + '=; Max-Age=-99999999;';  
}

// Select elements for adding additional information and room details
var add_btn = document.querySelector(".add_info");
var add_info = document.querySelector(".add_info_center");
var room_info = document.querySelector(".add_room_detail");
var add_room_info = document.querySelector(".add_room_details_center");
var submit_btn = document.querySelector(".submit");
var hidden_data = document.querySelector(".hidden_data");
var form = document.querySelector("form");
let hidden_infos_input = document.querySelector(".hidden_info_data");

// Array to store room details
var rooms_details = [];

// Helper function to generate a unique ID for each room
function generateUniqueId() {
    return 'room_' + Math.random().toString(36).substr(2, 9);
}

// Add event listener for the "add_info" button
add_btn.addEventListener("click", () => {
        const element = document.createElement("div");
        element.classList.add("add_info_item");
        element.innerHTML = `
                        <input type="text" class="add_info_item_here" placeholder="Additional Information Here" name="add_info" />
                        <button type="button" class="remove_info_btn">x</button>
        `;
        add_info.appendChild(element);

        const remove_btn = element.querySelector(".remove_info_btn");
        remove_btn.addEventListener("click", () => {
                add_info.removeChild(element);
        });
});

// Event listener for "Add Room Detail" button
room_info.addEventListener("click", () => {
        const uniqueRoomId = generateUniqueId(); // Generate a unique ID for each room
        const element = document.createElement("div");
        element.classList.add("add_info_item");
        element.innerHTML = `
                        <h6 style='font-family: var(--font1);'><center>Room Information<center></h6>
                        <input type='number' class='add_room_number' placeholder='How many in a Room?'/>
                        <input type='number' class='quantity' name='quantity' placeholder='How many rooms?'/>
                        <input class='price' type='number' placeholder='Price'>
                        <input type='file' name='room_image' class='room_image'>
                        <button type='button' class='room_amenity_btn' data-room-id='${uniqueRoomId}'>
                            <i class="fas fa-plus-circle"></i> Add Amenity
                        </button>
                        <input type='hidden' value='' class='room_amenities_hidden' data-room-id='${uniqueRoomId}'>
        `;
        add_room_info.appendChild(element);

        const amenity_btn = element.querySelector('.room_amenity_btn');

        // Event listener for the amenity button to 
        
        
        function add_amen_func() {
                const roomId = amenity_btn.getAttribute('data-room-id'); // Get the room's unique ID

                        // Create a popup for amenities
                        const dialog = document.createElement('div');
                        dialog.classList.add('amenity-dialog');
                        dialog.innerHTML = `
                                        <h4 class='text-light text-center m-3'>Room Amenities</h4>
                                        <div class='amenity-inputs'></div>
                                        <button type='button' class='add_item_btn'>Add Item</button>
                                        <button type='button' class='done_btn'>Done</button>
                        `;
                        document.body.appendChild(dialog);

                        const add_item_btn = dialog.querySelector('.add_item_btn');
                        const done_btn = dialog.querySelector('.done_btn');
                        const amenityInputsContainer = dialog.querySelector('.amenity-inputs');

                        // Function to add a new input field with delete button
                        function addAmenityInput(value = '') {
                                        const inputWrapper = document.createElement('div');
                                        inputWrapper.classList.add('amenity-input-wrapper');
                                        const input = document.createElement('input');
                                        input.type = 'text';
                                        input.classList.add('room_amenity_item');
                                        input.placeholder = 'Enter Amenity';
                                        input.value = value;
                                        const deleteBtn = document.createElement('button');
                                        deleteBtn.type = 'button';
                                        deleteBtn.classList.add('delete_amenity_btn');
                                        deleteBtn.innerHTML = 'x';
                                        deleteBtn.addEventListener('click', () => {
                                                        amenityInputsContainer.removeChild(inputWrapper);
                                        });
                                        inputWrapper.appendChild(input);
                                        inputWrapper.appendChild(deleteBtn);
                                        amenityInputsContainer.appendChild(inputWrapper);
                        }

                        // Check if there are existing amenities in the cookie and pre-fill
                        const existingAmenities = getCookie(roomId); // Use unique room ID for cookie
                        if (existingAmenities) {
                                        JSON.parse(existingAmenities).forEach(addAmenityInput);
                        } else {
                                        addAmenityInput(); // Add an empty input field by default
                        }

                        // Event listener to add more input fields
                        add_item_btn.addEventListener('click', () => addAmenityInput());

                        // Event listener for the done button
                        done_btn.addEventListener('click', () => {
                                        // Collect all amenities from inputs
                                        const amenities = Array.from(amenityInputsContainer.querySelectorAll('.room_amenity_item'))
                                                        .map(input => input.value)
                                                        .filter(value => value); // Filter out empty values

                                        // Save the amenities in a cookie with unique room ID
                                        setCookie(roomId, JSON.stringify(amenities), 1); // Set for 1 day

                                        // Update the hidden input for amenities
                                        element.querySelector('.room_amenities_hidden').value = JSON.stringify(amenities);

                                        // Close the dialog
                                        document.body.removeChild(dialog);
                                });
                        }
                        
                        amenity_btn.addEventListener('click', add_amen_func);
                });
                
submit_btn.addEventListener("click", (e) => {
    e.preventDefault();

    // Clear cookies before submitting
    const allCookies = document.cookie.split(';');
    allCookies.forEach(cookie => {
            const cookieName = cookie.split('=')[0].trim();
            // Clear only room cookies (if they follow a specific pattern)
            if (cookieName.startsWith('room_')) {
                    deleteCookie(cookieName);
            }
    });

    // Re-select dynamic elements
    const room_type = document.querySelectorAll(".add_room_number");
    const price = document.querySelectorAll(".price");
    const number_of_rooms = document.querySelectorAll(".quantity");
    hidden_infos_input = document.querySelector(".hidden_info_data");
    if (!hidden_infos_input) {
        console.error("Element with class 'hidden_info_data' not found in the DOM.");
        return;
    }

    const room_images = document.querySelectorAll(".room_image");

    // Clear previous details
    rooms_details = [];
    const info_details = [];
    const infos = document.querySelectorAll(".add_info_item_here"); // Define 'infos' by selecting elements

    infos.forEach((info) => {
            let information = info?.value.trim();
            if (information) {
                    info_details.push(information);
            }
    });

    room_type.forEach((_, index) => {
            let roomDetail = {
                    number_in_room: room_type[index].value.trim() || "",
                    price: price[index].value.trim() || "",
                    number_of_rooms: number_of_rooms[index].value.trim() || "",
                    room_image: Array.from(room_images[index].files).map(file => file.name), // Store image file names
                    amenities: document.querySelectorAll('.room_amenities_hidden')[index].value || "[]"
            };

            // Filter out empty room details
            if (roomDetail.number_in_room || roomDetail.price || roomDetail.number_of_rooms || roomDetail.room_image.length || roomDetail.amenities !== "[]") {
                    rooms_details.push(roomDetail);
            }
    });

    // Convert arrays to JSON strings for the hidden inputs
    hidden_infos_input.value = JSON.stringify(info_details);

    console.log(hidden_infos_input.value);
    hidden_data.value = JSON.stringify(rooms_details);

    // Submit the form
    form.submit();

    // Log room details for debugging
    console.log(rooms_details);
});