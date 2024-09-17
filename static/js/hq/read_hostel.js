var three_dots = document.querySelectorAll(".three-dots");
var sliding_info = document.querySelectorAll(".info1");
var rooms_info = document.querySelector(".room_info_duh");

three_dots.forEach((dot, index) => {
  let boolean = false;
  dot.addEventListener("mouseup", () => {
    if (!boolean) {
      sliding_info[index].style.position = "absolute";
      sliding_info[index].style.left = 0;
      dot.innerHTML = '<i class="fa-solid fa-times"></i>';
      dot.style.transition = "300ms ease";
      dot.style.transform = "rotate(180deg)"; // Changed dot.transform to dot.style.transform
      boolean = true;
    } else {
      dot.style.transform = "rotate(0deg)"; // Changed dot.transform to dot.style.transform
      sliding_info[index].style.position = "absolute";
      dot.style.transition = "300ms ease";
      dot.innerHTML = '<i class="fa-solid fa-bars"></i>';
      sliding_info[index].style.left = "100%";
      boolean = false;
    }
  });
});