var three_dots = document.querySelector('.three-dots')

var sliding_info = document.querySelectorAll('.info1')

sliding_info.forEach((slide, index) => {
    let boolean = false;
    three_dots.addEventListener('mouseup', ()=>{
    if (!boolean) {
        sliding_info[index].style.position = 'absolute';
        sliding_info[index].style.left = 0;
        boolean = true;
    } else {
        sliding_info[index].style.left = '100%';
        boolean = false;
    }
})

})

console.log(sliding_info)