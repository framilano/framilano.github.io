var queryString = window.location.search.replace('?', '');


var roundLength = queryString.split('&')[0].replace("roundLength=", '')
var skipAmount = queryString.split('&')[1].replace("skipAmount=", '')

var playButtonElement = document.getElementById("play-button")
var wordScreen = document.getElementById("word-display")
var skipButton = document.getElementById("skip-button")
var pointsCounter = document.getElementById("points-counter")
var skipCounter = document.getElementById("skip-counter")
var timeLeft = document.getElementById("time-left")
var plusButton = document.getElementById("plus-button")
var minusButton = document.getElementById("minus-button")

var intervalId = 0

timeLeft.innerText = roundLength
skipCounter.innerText = skipAmount

playButtonElement.addEventListener("click", () => {
    if (intervalId == 0) {
        intervalId = startTimer()
        playButtonElement.innerText = "Pausa"
    }
    else {
        clearInterval(intervalId)
        playButtonElement.innerText = "Gioca"
        intervalId = 0
    }
})

plusButton.addEventListener("click", () => {
    scoreInteger = parseInt(pointsCounter.innerText) + 1
    pointsCounter.innerText = scoreInteger
})
minusButton.addEventListener("click", () => {
    scoreInteger = parseInt(pointsCounter.innerText) - 1
    if (scoreInteger < 0) return
    pointsCounter.innerText = scoreInteger
})

skipButton.addEventListener("click", () => {
    skipCounterInteger = parseInt(skipCounter.innerText) - 1
    if (skipCounterInteger < 0) return
    skipCounter.innerText =  skipCounterInteger
})

function startTimer() {
    return setInterval(() => {
        timeLeft.innerText -= 1
        if (timeLeft.innerText == 0) {
            clearInterval(intervalId)
            playButtonElement.innerText = "Gioca"
            timeLeft.innerText = queryString.split('&')[0].replace("roundLength=", '')
            intervalId = 0
        }
    }, 1000)
}