var roundLength = document.getElementById("round-length-input").value
var skipAmount = document.getElementById("skip-amount-input").value
var errorPenalty = document.getElementById("error-penalty-input").checked

document.getElementById("round-length-input").addEventListener("input", () => {
    roundLength = document.getElementById("round-length-input").value
    document.getElementById("round-length").innerText = roundLength + " secondi"
})

document.getElementById("skip-amount-input").addEventListener("input", () => {
    roundLength = document.getElementById("round-length-input").value
    document.getElementById("round-length").innerText = roundLength + " secondi"
})

document.getElementById("error-penalty-input").addEventListener("input", () => {
    errorPenalty = document.getElementById("error-penalty-input").checked
    alert(errorPenalty)
})

document.getElementById("confirm-button").addEventListener("click", () => {
    location.href="game.html?roundLength=" + roundLength + "&skipAmount=" + skipAmount + "&errorPenalty=" + errorPenalty
})