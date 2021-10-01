document.getElementById('pomodorobtn').className="selectedbutton"
document.getElementById('pomodorobtn').addEventListener("click", spawnPomodoroTimer);
document.getElementById('shortbreakbtn').addEventListener("click", spawnShortBreakTimer);
document.getElementById('startbtn').addEventListener("click", startTimer);

intervalID = 0
audio = new Audio('assets/alarm.mp3');
audio1 = new Audio('assets/start.mp3')
current_timer = "pomodoro"

function spawnPomodoroTimer() {
    document.getElementById('startbtn').innerHTML ="START"
    document.getElementById('pomodorobtn').className="selectedbutton"
    document.getElementById('shortbreakbtn').className=""
    clearInterval(intervalID)
    current_timer="pomodoro"
    timer = document.getElementById('timer')
    timer.value ="pomodoro"
    timer.innerHTML = "25:00"
}

function spawnShortBreakTimer() {
    document.getElementById('startbtn').innerHTML ="START"
    document.getElementById('shortbreakbtn').className="selectedbutton"
    document.getElementById('pomodorobtn').className=""
    clearInterval(intervalID)
    current_timer = "shortbreak"
    timer = document.getElementById('timer')
    timer.value ="shortbreak"
    timer.innerHTML = "05:00"
}

function alarm() {
    document.getElementById('startbtn').innerHTML ="START"
    clearInterval(intervalID)
    audio.play();
    if (current_timer=="pomodoro") document.getElementById('shortbreakbtn').click()
    else document.getElementById('pomodorobtn').click()
}

function updateTimer() {
    res = timer.innerHTML.split(":")
    minutes = res[0]
    seconds = res[1]
    seconds = parseInt(seconds)
    minutes = parseInt(minutes)
    seconds = (60 + (seconds - 1)) % 60
    if (seconds == 59) minutes = minutes - 1
    if (seconds < 10) seconds = "0" + seconds
    if (minutes < 10) minutes = "0"+ minutes
    timer.innerHTML = minutes+":"+seconds
    if (minutes === "00" && seconds === "00") {
        alarm()
    }
}

function startTimer() {
    audio1.play()
    if (document.getElementById('startbtn').innerHTML == "PAUSE") {
        clearInterval(intervalID)
        document.getElementById('startbtn').innerHTML ="RESUME"
    } else {
        document.getElementById('startbtn').innerHTML ="PAUSE"
        timer = document.getElementById('timer')
        intervalID = setInterval(updateTimer, 1000)
    }
}
