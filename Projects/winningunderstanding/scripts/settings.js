var roundLength = document.getElementById("round-length-input").value
var skipAmount = document.getElementById("skip-amount-input").value

document.getElementById("round-length-input").addEventListener("input", () => {
    roundLength = document.getElementById("round-length-input").value
    document.getElementById("round-length").innerText = roundLength + " secondi"
})

document.getElementById("skip-amount-input").addEventListener("input", () => {
    skipAmount = document.getElementById("skip-amount-input").value
    document.getElementById("skip-amount").innerText = skipAmount + " passo"
})

document.getElementById("confirm-button").addEventListener("click", () => {
    location.href="game.html?roundLength=" + roundLength + "&skipAmount=" + skipAmount
})