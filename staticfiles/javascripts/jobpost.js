function focus_on_element(element, req) {
    console.log(element)
    console.log(element.childNodes)
    element.childNodes.map(())

    btn = document.createElement('button')
    // btn css
    btn.style.backgroundColor = 'white';
    btn.innerText = 'Apply'
    btn.style.margin = '10px'
    btn.style.border = 'solid 5px black'
    btn.style.borderRadius = '10px'
    
    btn.addEventListener("click", () => open_link(link));
    btn.id = 'dlt-this'

    req_p = document.createElement('p')
    req_p.innerText = req
    element.childNodes[1].appendChild(btn)
}
function unfocus_on_element(element) {
    console.log(element)
    console.log(element.childNodes[1].childNodes[1].hidden = false)
    element.childNodes[1].removeChild(document.getElementById('dlt-this'))
}
