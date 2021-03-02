/* Открытие меню */
var menu = document.getElementsByClassName('menu');


document.onmousemove = function(event) {
    var x = event.pageX;
    if (x < 6) {
        
        menu[0].animate({
            left: '0px'
        
        }, 300);
        menu[0].style.left = '0px';



    }else if (x > 285) {
        menu[0].animate({
            left: '-285px'
        }, 300);
        menu[0].style.left = '-285px';
    }    
    


}




