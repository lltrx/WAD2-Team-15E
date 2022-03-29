window.addEventListener("load", () => {
    document.getElementById("destination-title").classList.toggle("destination-title-animation");
    const cards = document.getElementsByClassName("card")
    if (cards.length>0) {
        console.log(cards);
        for (let i = 0; i<cards.length; i++) {
            cards[i].classList.toggle("destination-title-animation")
           
        }
    }
})