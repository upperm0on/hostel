// Select elements for adding additional information and room details
var add_btn = document.querySelector(".add_info");
var add_info = document.querySelector(".add_info_center");
var room_info = document.querySelector(".add_room_detail");
var add_room_info = document.querySelector(".add_room_details_center");
var submit_btn = document.querySelector(".submit");
var hidden_data = document.querySelector(".hidden_data");
// Select the form element correctly
var form = document.querySelector("form");

// Add event listener for the "add_info" button
add_btn.addEventListener("click", () => {
  element = document.createElement("div");
  element.classList.add("add_info_item");
  element.innerHTML =
    '<input type="text" class="add_info_item_here" placeholder="Additional Information Here" name="add_info" />';
  add_info.appendChild(element);
});

// Add event listener for the "add_room_detail" button
room_info.addEventListener("click", () => {
  const element = document.createElement("div");
  element.classList.add("add_info_item");
  element.innerHTML = `
      <input type='number' class='add_room_number' placeholder='How many in a Room?'/>
      <input type='number' class='quantity' name='quantity' placeholder='How many rooms?'/>
      <input class='price' type='number' placeholder='Price'>
      <input type='file' name='room_image' class='room_image'>
      <button type='button' class='room_amenity_btn'>Add Amenity</button>
      <input type='hidden' value='' class='room_amenities_hidden'>
  `;
  add_room_info.appendChild(element);

  const second_element = document.createElement('div');
  second_element.classList.add('room_amenity_loc');
  add_room_info.appendChild(second_element);

  const amenity_btn = element.querySelector('.room_amenity_btn');

  amenity_btn.addEventListener('click', () => {
      // Create a popup for amenities
      const dialog = document.createElement('div');
      dialog.classList.add('amenity-dialog');
      dialog.innerHTML = `
          <div class='amenity-inputs'></div>
          <button type='button' class='add_item_btn'>Add Item</button>
          <button type='button' class='done_btn'>Done</button>
      `;
      document.body.appendChild(dialog);

      const add_item_btn = dialog.querySelector('.add_item_btn');
      const done_btn = dialog.querySelector('.done_btn');
      const amenityInputsContainer = dialog.querySelector('.amenity-inputs');

      // Function to add a new input field
      function addAmenityInput() {
          const input = document.createElement('input');
          input.type = 'text';
          input.classList.add('room_amenity_item');
          input.placeholder = 'Enter Amenity';
          amenityInputsContainer.appendChild(input);
      }

      // Add the first input by default
      addAmenityInput();

      // Event listener for adding more input fields
      add_item_btn.addEventListener('click', addAmenityInput);

      // Event listener for the done button
      done_btn.addEventListener('click', () => {
          const hiddenInput = document.querySelector('.room_amenities_hidden');
          hiddenInput.value = ''; // Clear previous values

          // Collect all amenities
          const amenities = Array.from(amenityInputsContainer.querySelectorAll('.room_amenity_item'))
              .map(input => input.value)
              .filter(value => value) // Filter out empty values

          hiddenInput.value = amenities.join(', '); // Join values and set to hidden input

          // Close the dialog
          document.body.removeChild(dialog);
      });
  });
});


// Initialize an empty array to store room details
var rooms_details = [];


// Add event listener for the submit button
submit_btn.addEventListener("click", (e) => {
  e.preventDefault();

  // Re-select the dynamic elements each time the submit button is clicked
  var room_type = document.querySelectorAll(".add_room_number");
  var price = document.querySelectorAll(".price");
  var number_of_rooms = document.querySelectorAll(".quantity");

  var infos = document.querySelectorAll(".add_info_item_here");
  var hidden_infos_input = document.querySelector(".hidden_info_data");
  var room_images = document.querySelectorAll(".room_image");
  // Clear the previous details to avoid duplication
  rooms_details = [];
  info_details = [];

  infos.forEach((info) => {
    let information = info?.value;
    info_details.push(information);
  });

  room_type.forEach((_, index) => {
    let roomDetail = {
      number_in_room: room_type[index].value || "",
      price: price[index].value || "",
      number_of_rooms: number_of_rooms[index].value || "",
      room_image: Array.from(room_images[index].files).map((file) => file.name), // Store image file names
    };
    rooms_details.push(roomDetail);
  });

  // Convert the array to a JSON string to send via a hidden input
  let roomsDetailsJSON = JSON.stringify(rooms_details);
  let additional_info_JSON = JSON.stringify(info_details);

  hidden_infos_input.value = additional_info_JSON;

  // Append the hidden input element to the form
  hidden_data.value = roomsDetailsJSON;

  // Submit the form
  form.submit();

  // Log the structured room details
  console.log(rooms_details);
});