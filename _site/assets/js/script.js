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

//Accordion for Experience Section
var acc = document.getElementsByClassName("position");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    }
}


//Accordion for Education Section
var acc = document.getElementsByClassName("school");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function () {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    }
}

//About Me Show and Hide
//When "Show More" is clicked, the "about me" section expands, the "show more" button disappears, and a "show less" button appears.
//When the "show less" button is clicked, the "about me" section closes, and the "show more" button reappears.
$(document).ready(function () {
    $("#show-aboutme").click(function () {
        $(".read-more-about-me").slideToggle();
        $("#show-aboutme").toggle();
    })

    $(".show-less-about-me").click(function () {
        $(".read-more-about-me").slideToggle();
        $("#show-aboutme").toggle();
    })
});
