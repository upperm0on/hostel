var view_room_btn = document.querySelectorAll('.room_info_btn')
var dialogue = document.querySelectorAll('.display_room_details')


view_room_btn.forEach((room, index) => {   
    element = dialogue[index]
    element.style.position = 'absolute';
    element.style.left = '50%';
    element.style.top = '40%';
    element.style.transform = 'translate(-50%, -50%)';
    element.style.height = '100px';
    element.style.width = '100px';
    element.style.border = '3px solid black';
    element.style.display = "none"
    let boolean = false
    room.addEventListener('mousedown', ()=>{
        if (!boolean) {
            element.style.display = "block"
            boolean = true
        } else {
            element.style.display = "none"
            boolean = false
        }
    })
})