window.onload = function(){
  document.getElementById('hamburgerIcon').addEventListener("click", function(){
    var x = document.getElementById("myTopNav");
    if (x.className === "row topnav") {
      x.className += " responsive";
      } else {
      x.className = "row topnav";
      }
    });
  }
