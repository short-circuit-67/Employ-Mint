function open_link(link) {
    window.open(link,"_self")
}

function focus_on_element(element, link) {
    console.log(element)
    console.log(element.childNodes[1].childNodes[1].hidden = true)
    btn = document.createElement('button')
    // btn css
    btn.style.backgroundColor = '#2F4F4F';
    btn.innerText = 'Join'
    btn.style.margin = '10px'
    btn.style.border = 'solid 5px black'
    btn.style.borderRadius = '10px'
    btn.style.color = 'white'
    btn.style.width = '30%'
    btn.style.fontSize = 'larger'

    btn.addEventListener("click", () => open_link(link));
    btn.id = 'dlt-this'
    element.childNodes[1].appendChild(btn)
}
function unfocus_on_element(element) {
    console.log(element)
    console.log(element.childNodes[1].childNodes[1].hidden = false)
    element.childNodes[1].removeChild(document.getElementById('dlt-this'))
}