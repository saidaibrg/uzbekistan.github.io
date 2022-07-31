window.addEventListener('load', function() {
    baguetteBox.run('.gallery',{
      async: true      
    })
  });
window.scroll(function() {
  if ($(document).scrollTop() > 200) { 
      $('.navbar__menu').addClass('menu-scroll'); 
    } 
  else {
        $('.navbar__menu').removeClass('menu-scroll');
    }
});