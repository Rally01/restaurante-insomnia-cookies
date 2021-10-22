function openPage(pageName, elmnt, color) 
{
  // Hide all elements with class="tabcontent" by default */
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) 
  {
    tabcontent[i].style.display = "none";
  }

  // Remove the background color of all tablinks/buttons
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) 
  {
    tablinks[i].style.backgroundColor = "";
  }

  // Show the specific tab content
  document.getElementById(pageName).style.display = "block";

  // Add the specific color to the button used to open the tab content
  elmnt.style.backgroundColor = color;
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();

var myCarousel_1 = document.querySelector('#carouselExampleCaptions1')
var carousel_1 = new bootstrap.Carousel(myCarousel_1)

var myCarousel_2 = document.querySelector('#carouselExampleCaptions2')
var carousel_2 = new bootstrap.Carousel(myCarousel_2)

var myCarousel_3 = document.querySelector('#carouselExampleCaptions3')
var carousel_3 = new bootstrap.Carousel(myCarousel_3)

var myCarousel_4 = document.querySelector('#carouselExampleCaptions4')
var carousel_4 = new bootstrap.Carousel(myCarousel_4)


var exampleEl = document.getElementById('example')
var popover = new bootstrap.Popover(exampleEl, options)


