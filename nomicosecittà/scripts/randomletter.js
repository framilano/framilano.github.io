function ranlet() {
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    var x = Math.ceil((Math.random() * 1000) % 25)

    alert ("La lettera trovata è " +characters[x]);
}

function updatetotal() {
    var total = 0
    points = document.getElementsByName('point')
    points.forEach(element => {
        total += parseFloat(element.value);
    });

    document.getElementById('total').innerHTML = "Punteggio totale " + total;
}


function appendRow() {
    const newRow = document.createElement('tr')
    let td, input;
    
    for(let i=0; i<4; i++){
      td = document.createElement('td')
      input = document.createElement('input')
      input.setAttribute('type','text')
      td.appendChild(input)
      newRow.appendChild(td)
    }
    
    
    td = document.createElement('td')
    input = document.createElement('input')
    input.setAttribute('type','range')
    input.setAttribute('min',0)
    input.setAttribute('max',4)
    input.setAttribute('step',0.5)
    input.setAttribute('name', 'point')
    input.setAttribute('onchange', 'updatetotal()')
    td.appendChild(input)
    newRow.appendChild(td)
    
    document.getElementById('gametable').appendChild(newRow);
}