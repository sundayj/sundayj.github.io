//Hambuger animation
function navToggle(x) {
    x.classList.toggle("change");
}

function maindropdown() {
    var respNav = document.getElementById("myMainNav");
    if (respNav.className === "mainnav") {
        respNav.className += "responsive";
    } else {
        respNav.className = "mainnav";
    }   
}

document.getElementById("hamburger").addEventListener("click", maindropdown);