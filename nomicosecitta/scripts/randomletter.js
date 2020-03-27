function ranlet() {
    var x = parseInt((Math.random() * 100) % characters.length)
    if (characters.length > 0) alert("Ho trovato una " + characters[x]);
    else alert("Sono finite le lettere, GG");
    characters.splice(x,1)
}

function updatetotal() {
    var total = 0.0
    points = document.getElementsByName('point')
    points.forEach(element => {
        total += parseFloat(element.value);
    });
    total = total.toFixed(1)
    document.getElementById('total').innerHTML = "👑 Punteggio totale: " + total + " 👑";
}

function setvolume() {
    var audio = document.getElementById("backgroundmusic");
    audio.volume = 0.2;
}


function appendRow() {
    counter++;
    const newRow0 = document.createElement('tr')
    ids = ['nomi', 'cose', 'città', 'animali', 'cibo', 'vip', 'mestieri', 'punteggio']
    names = ['Nomi 👨👩', 'Cose 🔍', 'Citta\' 🏙️', 'Animali 🐻', 'Cibo 🍔', 'Vip 🎥', 'Mestieri 👔', 'Punteggio 📈']
    //Creazione riga con intestazione nomi
    for (let i = 0; i < 8; i++) {
        th = document.createElement('th')
        th.innerHTML = names[i]
        th.setAttribute('id', ids[i])
        newRow0.append(th)
    }

    const newRow = document.createElement('tr')
    let td, input;

    for (let i = 0; i < 7; i++) {
        td = document.createElement('td')
        input = document.createElement('input')
        input.setAttribute('type', 'text')
        input.setAttribute('placeholder', 'Scrivi qui')
        td.appendChild(input)
        newRow.appendChild(td)
    }


    td = document.createElement('td')
    input = document.createElement('input')
    input.setAttribute('type', 'range')
    input.setAttribute('min', 0)
    input.setAttribute('max', 7)
    input.setAttribute('step', 0.5)
    input.setAttribute('name', 'point')
    input.setAttribute('oninput', 'updatetotal();document.getElementById(\'' + counter + '\').innerHTML = parseFloat(this.value).toFixed(1)')
    input.defaultValue = 0
    td.appendChild(input)
    //div è dedicato al punteggio live ottenuto sotto un input type range
    div = document.createElement('div')
    div.setAttribute('id', counter)
    div.setAttribute('style', 'font-size:150%;color:#9b0000')
    div.innerHTML = 0.0
    td.appendChild(div)
    newRow.appendChild(td)

    //Creazione linea vuota per separare i vari round
    emptyline = document.createElement('tr')
    empytbox = document.createElement('td')
    empytbox.setAttribute('colspan', 8)
    if (counter != 1) empytbox.innerHTML = '<hr style=\"width:100%;border:transparent; height:4px; background-color:#181818\">'
    emptyline.appendChild(empytbox)

    document.getElementById('gametable').appendChild(emptyline)
    document.getElementById('gametable').appendChild(newRow0)
    document.getElementById('gametable').appendChild(newRow);
}

function choosebackground() {
    var walls = ["images/background.png", "images/moon.png"]
    choice = parseInt(Math.random() *100) % 2
    bodyground = document.getElementById('background')
    bodyground.setAttribute('style', 'background-image: url(\''+walls[choice]+'\')')
}

//Randomizzatore di sfondi
choosebackground()

//Caratteri di scelta per il dado
var characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
// Variabile che conta quante righe sono state inserite
var counter = 0