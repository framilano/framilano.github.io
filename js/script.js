function change_theme(btn_elem) {
    icon_string = btn_elem.innerText
    body = document.getElementsByTagName('body')[0]
    page_content = document.getElementsByClassName('page-content')[0]
    page_table = document.getElementById('page_table')
    if (icon_string == "🌙") {
        btn_elem.innerText = "☀️"
        body.setAttribute("style", "color:#000000;background-color:#FFFFFF")
        page_content.setAttribute("style", "background-color:#B0B0B0")
        page_table.setAttribute("style", "background-color:#B0B0B0")
    }
    else {
        btn_elem.innerText = "🌙"
        body.setAttribute("style", "color:#FFFFFF;background-color:#181818")
        page_content.setAttribute("style", "background-color:#151515")
        page_table.setAttribute("style", "background-color:#151515")
    }
}