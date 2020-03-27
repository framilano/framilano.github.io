
var characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
function ranlet() {
    var x = parseInt((Math.random() * 100) % characters.length)
    if (characters.length > 0) alert("Ho trovato una " + characters[x]);
    else alert("Sono finite le lettere, GG");
    characters.splice(x,1)
}

function updatetotal() {
    var total = 0
    points = document.getElementsByName('point')
    points.forEach(element => {
        total += parseFloat(element.value);
    });

    document.getElementById('total').innerHTML = "Punteggio totale: " + total;
}

function showtable() {
   document.getElementById('gametable').hidden=0
    
}

function showvalue(newelement, newvalue) {
    if (newvalue <= 2) newelement.innerHTML = newvalue + " " +'😭'
    else newelement.innerHTML = newvalue + " " + '🤓'
    if (newvalue == 4) newelement.innerHTML = newvalue + " " +'💥'
}

var counter = 0

function appendRow() {
    counter++;
    const newRow = document.createElement('tr')
    let td, input;

    for (let i = 0; i < 4; i++) {
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
    input.setAttribute('onchange', 'updatetotal();showvalue(document.getElementById(\'' + counter + '\'),this.value)')
    input.defaultValue = 0
    td.appendChild(input)
    newRow.appendChild(td)

    td = document.createElement('td')
    td.setAttribute('id', counter)
    td.innerHTML = '0.0'
    newRow.appendChild(td)

    document.getElementById('gametable').appendChild(newRow);
}