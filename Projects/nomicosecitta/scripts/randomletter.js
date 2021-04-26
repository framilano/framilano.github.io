//Genera una lettera casualmente, non ripete mai due volte la stessa lettera
function ranlet() {
    var x = parseInt((Math.random() * 100) % characters.length)
    if (characters.length > 0) alert("Ho trovato una " + characters[x]);
    else alert("Sono finite le lettere, GG");
    characters.splice(x,1)
}

//Aggiorna il punteggio totale mantenuto in basso, viene chiamato ad ogni spostamento del punteggio su ogni riga
function updatetotal() {
    var total = 0.0
    points = document.getElementsByName('point')
    points.forEach(element => {
        total += parseFloat(element.value);
    });
    total = total.toFixed(1)
    document.getElementById('total').innerHTML = "👑 Punteggio totale: " + total + " 👑";
}

//funzione dedicata all'aggiustamento del voliume del sottofondo
function setvolume() {
    var audio = document.getElementById("backgroundmusic");
    audio.volume = 0.1;
}

//Una funzione dedicata all'aggiunta di una nuova categoria all'array names
function addcategory(newcat) {
    if (newcat.value == "") {
        alert("Non puoi inserire categorie senza nome")
        return
    }
    if (names.length > 9) {
        alert("Non puoi inserire più di 10 categorie")
        return
    }
    names.push(newcat.value)
    //Azzero il valore dell'input inserito in modo tale da poterne mettere un altro
    newcat.value = ""
}

function appendRow() {
    //Controllo se la lista names non possiede alcun elemento, dunque inutile creare una riga
    if (names.length == 0) {
        alert("Forse prima dovresti aggiungere qualche categoria...")
        document.getElementById('gametable').hidden=1
        return
    }
    counter++;

    //Creo la riga di intestazione contenente i nomi delle categorie per ogni nuova riga di gioco creata
    const newRow0 = document.createElement('tr')

    //Creazione riga con intestazione nomi
    for (let i = 0; i < names.length; i++) {
        th = document.createElement('th')
        th.setAttribute('style', 'color:rgba(121,14,139, .7);')
        th.innerHTML = names[i]
        newRow0.append(th)
    }

    //Creo separatamente l'intestazione del punteggio per riga
    th = document.createElement('th')
    th.setAttribute("style", "color:#9b0000")
    th.innerHTML = "Punteggio"
    newRow0.append(th)

    //Creo una nuova riga per ospitare gli input per ogni categoria
    const newRow = document.createElement('tr')
    let td, input;

    for (let i = 0; i < names.length; i++) {
        td = document.createElement('td')
        input = document.createElement('input')
        input.setAttribute('type', 'text')
        input.setAttribute('placeholder', 'Scrivi qui')
        td.appendChild(input)
        newRow.appendChild(td)
    }

    //Sezione dedicata all'input per il cambio del punteggio
    td = document.createElement('td')
    input = document.createElement('input')
    input.setAttribute('type', 'range')
    input.setAttribute('min', 0)
    input.setAttribute('max', names.length*2)
    input.setAttribute('step', 0.5)
    input.setAttribute('name', 'point')
    input.setAttribute('oninput', 'updatetotal();document.getElementById(\'' + counter + '\').innerHTML = parseFloat(this.value).toFixed(1)')
    input.defaultValue = 0
    td.appendChild(input)

    //Questa sezione è dedicata all'aggiornamento live del piccolo punteggio sotto ogni input "punteggio", per ogni riga
    div = document.createElement('div')
    div.setAttribute('id', counter)
    div.setAttribute('style', 'font-size:150%;color:#9b0000')
    div.innerHTML = 0.0
    td.appendChild(div)
    newRow.appendChild(td)

    //Creazione linea vuota per separare i vari round
    emptyline = document.createElement('tr')
    empytbox = document.createElement('td')
    empytbox.setAttribute('colspan', names.length+1)
    if (counter != 1) empytbox.innerHTML = '<hr style=\"width:100%;border:transparent; height:8px; background-color:#181818\">'
    emptyline.appendChild(empytbox)

    //appendo tutti gli elementi creati alla tabella di gioco
    document.getElementById('gametable').appendChild(emptyline)
    document.getElementById('gametable').appendChild(newRow0)
    document.getElementById('gametable').appendChild(newRow);
}

//Caratteri di scelta per il dado
var characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];

// Variabile che conta quante righe sono state inserite
var counter = 0

//Lista contenente i nomi delle categorie inserite
var names = []