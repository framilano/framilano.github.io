var intervalID;

onmessage (comand => {
    if (comand == "clear") {
        clearInterval(intervalID)
        postMessage()
        return
    } else intervalID = setInterval(postMessage(), 1000)
});