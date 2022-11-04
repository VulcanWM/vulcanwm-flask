window.onscroll = function() {myFunction()};

var navbar = document.getElementById("navbar");
var sticky = navbar.offsetTop;

function myFunction() {
  if (window.pageYOffset >= sticky) {
    navbar.classList.add("sticky")
  } else {
    navbar.classList.remove("sticky");
  }
}

var Script1 = document.createElement("script");
Script1.setAttribute("async", null);
Script1.src = 
"https://www.googletagmanager.com/gtag/js?id=G-YG5GQ7P5J0";
document.head.appendChild(Script1);


var Script2 = document.createElement("script");
Script2.innerText = 
"window.dataLayer = window.dataLayer || [];function gtag(){dataLayer.push(arguments);}gtag('js', new Date());gtag('config', 'G-YG5GQ7P5J0');";
document.head.appendChild(Script2);