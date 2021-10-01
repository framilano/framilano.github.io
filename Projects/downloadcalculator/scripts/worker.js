//Variabili globali di dimensione dei dati e velocità
var datasize = 0
var dwlspeed = 0

/*
* Gestisce l'input della dimensione dei dati e aggiorna la variabile globale datasize
* @params : none
* @returns: none
*/
function go2dwlspeed() {
    var inputdim = document.getElementById('datadim').value
    var chosen = null
    radios = document.getElementsByName('chooser')
    radios.forEach(element => {
        if (element.checked) chosen = element
    });
    if (chosen == null) {
        alert("You must select the download size dimension unit")
        return
    }
    
    switch (chosen.id) {
        case 'kb':
            datasize = document.getElementById('datadim').value / 1000
        break;
        case 'mb':
            datasize = document.getElementById('datadim').value
        break;
        case 'gb':
            datasize = document.getElementById('datadim').value * 1000
        break;
    }
    if (inputdim.length == 0) datasize = 0
    if (parseInt(inputdim) < 0) {
        alert("You cannot insert negative values")
        return
    } 
        
    document.getElementById('choosedimension').hidden = 1
    document.getElementById('choosedwlspeed').hidden = 0
}

/*
* Calculate hours, minutes and seconds to download a file
* @params : none
* @returns: none
*/
function final() {
    var inputspeed = document.getElementById('dataspeed').value
    var chosen = null
    radios = document.getElementsByName('speedchooser')
    radios.forEach(element => {
        if (element.checked) chosen = element
    });
    if (chosen == null) {
        alert("You must select the download speed dimension unit")
        return
    }
    
    switch (chosen.id) {
        case 'kbit/s':
            dwlspeed = document.getElementById('dataspeed').value / 1000
        break;
        case 'mbit/s':
            dwlspeed = document.getElementById('dataspeed').value
        break;
        case 'gbit/s':
            dwlspeed = document.getElementById('dataspeed').value * 1000
        break;
    }
    // gestisco il caso di input velocità pari a 0 o nullo
    if (inputspeed.length == 0 || Math.round(inputspeed) == 0) {
        document.getElementById('choosedwlspeed').hidden = 1
        document.getElementById('result').hidden = 0
        document.getElementById('answer').innerHTML = " a long time with such a download speed D:"
        return
    }

    //Gestisco e mi riprendo dal caso di input velocità negativo
    if (Math.round(inputspeed) < 0) {
        alert("You cannot insert negative values")
        return
    }

    //Eseguo conversione della velocità da megabit/s a megabyte/s
    inmb = dwlspeed*0.125
    totalseconds = Math.floor(datasize / inmb)
    days = Math.floor(totalseconds / 86400)
    hours = Math.floor((totalseconds - days*86400) / 3600)
    minutes = Math.floor((totalseconds - days*86400 - hours*3600) / 60)
    seconds = Math.floor(totalseconds - days*86400 - hours*3600 - minutes*60)
    //Gestisco il caso di dimensione dei dati nulla
    if (datasize == 0) {
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
    }

    //Mostro l'ultima pagina con la stringa risultante
    document.getElementById('choosedwlspeed').hidden = 1
    document.getElementById('result').hidden = 0
    document.getElementById('answer').innerHTML = days + " days " + hours + " hours " + minutes + " minutes and " + seconds + " seconds "
}

//Bottone che torna alla pagina iniziale
function backtomenu() {
    document.getElementById('choosedimension').hidden = 0
    document.getElementById('choosedwlspeed').hidden = 1
    document.getElementById('result').hidden = 1
}