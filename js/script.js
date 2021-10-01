function typewrite() {
    elem = document.getElementsByClassName("typewriter")[0]
    sen = "> Computer Science student from Milan ".split("")
    console.log(sen)
    i = 0
    setInterval(() => {
        if (sen[i] == undefined) return
        elem.innerHTML += sen[i]
        i += 1
    }, 100);
}