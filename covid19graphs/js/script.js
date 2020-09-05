function change_theme(btn_elem) {
    icon_string = btn_elem.innerText
    body = document.getElementsByTagName('body')[0]
    page_content = document.getElementsByClassName('page-content')[0]
    page_table = document.getElementById('page_table')
    images = document.getElementsByClassName('images')
    if (icon_string == "🌙") {
        btn_elem.innerText = "☀️"
        body.setAttribute("style", "color:#000000;background-color:#FFFFFF")
        for (item of images) {
            item.setAttribute("style", "filter: invert(100%)")  
        }

    }
    else {
        btn_elem.innerText = "🌙"
        body.setAttribute("style", "color:#FFFFFF;background-color:#000000")
        for (item of images) {
            item.setAttribute("style", "filter: invert(0%)")  
        }
    }
}