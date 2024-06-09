
elem = document.getElementsByClassName("typewriter")[0]

const sleep = ms => new Promise(r => setTimeout(r, ms));

async function typewrite() {
    index = 0
    sentences = [" hello internet surfer!", " welcome to my site", " enjoy your stay"]

    while (index < sentences.length) {
        await write(sentences[index])
        await sleep(2000)
        if (index != sentences.length - 1) await deleteSen()
        await sleep(2000)
        index += 1
    }
}


async function write(sen) {
    i = 0

    while (sen[i] != undefined) {
        elem.innerHTML += sen[i]
        i += 1
        await sleep(100)
    }
}

async function deleteSen() {
    j = elem.innerText.length - 1
    while(elem.innerText[j] != '$') {
        elem.innerText = elem.innerText.substring(0, j);
        j -= 1
        await sleep(100)
    }
}