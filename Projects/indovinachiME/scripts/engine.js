
characters = ["1.png", "2.png", "3.png", "4.png", "5.png", "6.png", "7.png", "8.png", "9.png", "10.png", "11.png", "12.png", 
"13.png", "14.png", "15.png", "16.png", "17.png", "18.png", "19.png", "20.png", "21.png", "22.png", "23.png", "24.png"]

score = 0

function showrandomcharacter() {
    if (characters.length <= 0) {
        alert("Sono finiti i personaggi! Premi F5 per ricominciare")
        return
    }
    image = document.getElementById('chosenone')
    rdn_char = parseInt((Math.random() * 100) % characters.length)
    image.setAttribute('src', "characters/"+characters[rdn_char])
    characters.splice(rdn_char, 1)
    image.setAttribute('width', '150')
    image.setAttribute('style', "border: 10px solid red;border-radius:15px")
    image.setAttribute('height', '168')
}

function setvolume() {
    var audio = document.getElementById("backgroundmusic");
    audio.volume = 0.03;
}

function increase_score() {
    score++;
    document.getElementById('score').innerHTML = "Punteggio: "+ String(score)
}

function reset_game() {
    img_list = document.getElementsByTagName('img')
    for(i = 0; i < 24; i++) {
        img_list[i].setAttribute('class', '')
    }
}

function grey_out(image) {
    classname = image.getAttribute('class')
    if (classname == 'greyed_out') {
        image.setAttribute('class', '')
        return
    }
    image.setAttribute('class', 'greyed_out')
}

function generate_table() {
    nuovatabella = document.getElementById('gametable')
    for (i = 0; i < 4; i++) {
        tr = document.createElement('tr')
        z = i * 6
        for (j = 0; j < 6; j++) {
            td = document.createElement('td')
            img = document.createElement('img')
            img.setAttribute('src', "characters/" + characters[z])
            img.setAttribute('id', z)
            img.setAttribute('width', '150')
            img.setAttribute('height', '168')
            img.setAttribute('onclick', 'grey_out(document.getElementById('+ String(z) +'))')
            z++
            td.append(img)
            tr.append(td)
        }
        nuovatabella.append(tr)
    }
}