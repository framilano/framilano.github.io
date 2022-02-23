function typewrite() {
    elem = document.getElementsByClassName("typewriter")[0]
    sen = "> Computer Scientist from Milan".split("")
    i = 0
    setInterval(() => {
        if (sen[i] == undefined) return;
        elem.innerHTML += sen[i]
        i += 1
    }, 100);
}