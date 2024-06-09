typewrite()


programmerButton = document.getElementById("programmerButton")

artistButton = document.getElementById("artistButton")


document.addEventListener('DOMContentLoaded', function () {

    new Splide('#slider1').mount();

    new Splide('#slider2', {
        type: 'slide',
    }).mount();

});



programmerButton.addEventListener("click", () => {
    document.getElementsByClassName("box3")[0].hidden = !document.getElementsByClassName("box3")[0].hidden
    document.getElementsByClassName("box4")[0].hidden = true
})


artistButton.addEventListener("click", () => {
    document.getElementsByClassName("box4")[0].hidden = !document.getElementsByClassName("box4")[0].hidden
    document.getElementsByClassName("box3")[0].hidden = true

})



