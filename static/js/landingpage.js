var three_dots = document.querySelectorAll('.three-dots');
var sliding_info = document.querySelectorAll('.info1');
var cards = document.querySelectorAll(".card");
var left = document.querySelector(".left-arrow");
var reset = document.querySelector(".reset");

classnames = [];

for (var i = 0; i < cards.length; i++) { // Changed <= to < for correct iteration
    let this_var = `card${i}`;
    classnames.push(this_var);
}

// Initialize cards
cards.forEach((card, index) => {
    card.classList.add(classnames[index]);
});

// Apply initial styles
classnames.forEach((classname, index) => {
    let element = document.querySelector(`.${classname}`);
    if (element) {
        element.style.zIndex = classnames.length - index; // Adjust zIndex so top card has highest value
        element.style.position = "absolute";
        element.style.left = 15 * index + "px";
        element.style.transform = `scale(${1 - index * 0.05}) rotate(${index * 2}deg)`; // Adjust scale and rotation
        element.style.transition = "transform 200ms ease, left 200ms ease, zIndex 200ms ease"; // Smooth transitions
    }
});

let count = 0;
let previous_offset = 15;

reset.addEventListener('click', ()=>{
    classnames.forEach((classname, index) => {
        let element = document.querySelector(`.${classname}`);
        if (element) {
            element.style.zIndex = classnames.length - index; // Adjust zIndex so top card has highest value
            element.style.position = "absolute";
            element.style.left = 15 * index + "px";
            element.style.transform = `scale(${1 - index * 0.05}) rotate(${index * 2}deg)`; // Adjust scale and rotation
            element.style.transition = "transform 200ms ease, left 200ms ease, zIndex 200ms ease"; // Smooth transitions
            count = 0
        }
    });
})

// Variables for interaction


left.addEventListener("click", () => {
    if (count < classnames.length) {
        let element = document.querySelector(`.${classnames[count]}`);
        if (element) {
            element.style.position = "absolute";
            element.style.left = -(previous_offset * (classnames.length - count)) + "px";
            element.style.zIndex = count; // Adjust zIndex for current element
            element.style.transform = `scale(${1 - (classnames.length - count) * 0.05}) rotate(-${(classnames.length - (count + 1)) * 2}deg)`; // Adjust scale and rotation
            let next_element = document.querySelector(`.${classnames[count + 1]}`);
            if (next_element) {
                next_element.style.transform = "rotate(0deg)"; // Reset scale and rotation for the top element

                // Adjust the next element if necessary
                if (count == 2 && count + 1 < classnames.length) {
                    next_element.style.zIndex = classnames.length + 1; // Bring the next element to the front
                    next_element.style.transform = "scale(1) rotate(0deg)"; // Reset scale and rotation for the top element
                }
            }
            count = count + 1;
        } else {
            console.warn(`Element with class ${classnames[count]} not found.`);
        }
        console.log(element, element.offsetLeft);
    }
});

three_dots.forEach((dot, index) => {
    let boolean = false;
    dot.addEventListener('mouseup', () => {
        if (!boolean) {
            sliding_info[index].style.position = 'absolute';
            sliding_info[index].style.left = 0;
            dot.innerHTML = '<i class="fa-solid fa-minus"></i>';
            dot.style.transition = "300ms ease";
            dot.style.transform = "rotate(180deg)"; // Changed dot.transform to dot.style.transform
            boolean = true;
        } else {
            dot.style.transform = "rotate(0deg)"; // Changed dot.transform to dot.style.transform
            sliding_info[index].style.position = "absolute";
            dot.style.transition = "300ms ease";
            dot.innerHTML = '<i class="fa-solid fa-ellipsis-vertical"></i>';
            sliding_info[index].style.left = '100%';
            boolean = false;
        }
    });
});

console.log(sliding_info);
