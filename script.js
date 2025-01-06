document.getElementById("ai").addEventListener("click", (event) => toggleShow(event));
document.getElementById("utilities").addEventListener("click", (event) => toggleShow(event));
document.getElementById("games").addEventListener("click", (event) => toggleShow(event));


function toggleShow(event) {
    triggerId = event.target.id
    list = document.getElementById(triggerId + "-list")
    if (list.style.display == "block") list.style.display = "none"
    else list.style.display = "block"
}