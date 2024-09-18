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
  element = document.createElement("div");
  element.classList.add("add_info_item");
  element.innerHTML =
    "<input type='number' class='add_room_number' placeholder='How many in a Room?'/> <input type='number' class='quantity' name='quantity' placeholder='How many rooms?'/> price <input class='price' type='number' placeholder='Price'> <input type='file' name='room_image' class='room_image'>";
  add_room_info.appendChild(element);
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
