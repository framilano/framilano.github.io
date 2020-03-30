var datasize = 0
var dwlspeed = 0

function go2dwlspeed() {
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
            datasize = parseInt(document.getElementById('datadim').value) / 1000
        break;
        case 'mb':
            datasize = parseInt(document.getElementById('datadim').value)
        break;
        case 'gb':
            datasize = parseInt(document.getElementById('datadim').value) * 1000
        break;
    }
    if (document.getElementById('datadim').value.length == 0) datasize = 0
    document.getElementById('choosedimension').hidden = 1
    document.getElementById('choosedwlspeed').hidden = 0
}

/*
* Calculate hours, minutes and seconds to download a file
* params : none
* returns: none
*/
function final() {
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
            dwlspeed = parseInt(document.getElementById('dataspeed').value) / 1000
        break;
        case 'mbit/s':
            dwlspeed = parseInt(document.getElementById('dataspeed').value)
            
        break;
        case 'gbit/s':
            dwlspeed = parseInt(document.getElementById('dataspeed').value) * 1000
        break;
    }

    if (document.getElementById('dataspeed').value.length == 0) dwlspeed = 0
    inmb = dwlspeed*0.125
    totalseconds = parseInt(datasize / inmb)
    days = parseInt(totalseconds / 86400)
    hours = parseInt((totalseconds - days*86400) / 3600)
    minutes = parseInt((totalseconds - days*86400 - hours*3600) / 60)
    seconds = parseInt(totalseconds - days*86400 - hours*3600 - minutes*60)
    if (datasize == 0 || dwlspeed == 0) {
        days = 0
        hours = 0
        minutes = 0
        seconds = 0
    }
    document.getElementById('choosedwlspeed').hidden = 1
    document.getElementById('result').hidden = 0
    document.getElementById('answer').innerHTML = days + " days " + hours + " hours " + minutes + " minutes and " + seconds + " seconds "
}

function backtomenu() {
    document.getElementById('choosedimension').hidden = 0
    document.getElementById('choosedwlspeed').hidden = 1
    document.getElementById('result').hidden = 1
}