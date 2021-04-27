document.getElementById("btn").addEventListener("click", loadxmlpage)

function loadxmlpage() {
    gameid = document.getElementById('gameid').value
    urlxml = "https://a0.ww.np.dl.playstation.net/tpl/np/"+gameid+"/"+gameid+"-ver.xml"
    newlink = document.createElement('a')
    newlink.href=urlxml
    newlink.id="xmllink"
    newlink.title= "Download link!"
    newlink.innerHTML = "Open XML Link"
    if (document.getElementById('xmllink') != null) document.getElementById('xmllink').remove()
    document.getElementById('result').appendChild(newlink)
}