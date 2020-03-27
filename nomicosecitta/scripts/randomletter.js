
var characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
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

function showtable() {
   document.getElementById('gametable').hidden=0
    
}

var counter = 0

function appendRow() {
    counter++;
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
    input.setAttribute('max', 4)
    input.setAttribute('step', 0.5)
    input.setAttribute('name', 'point')
    input.setAttribute('oninput', 'updatetotal();document.getElementById(\'' + counter + '\').innerHTML = parseFloat(this.value).toFixed(1)')
    input.defaultValue = 0
    td.appendChild(input)
    //div è dedicato al punteggio live ottenuto sotto un input type range
    div = document.createElement('div')
    div.setAttribute('id', counter)
    div.innerHTML = 0.0
    td.appendChild(div)
    newRow.appendChild(td)

    document.getElementById('gametable').appendChild(newRow);
}