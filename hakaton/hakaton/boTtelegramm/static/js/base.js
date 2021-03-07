var menu = document.getElementsByClassName('hidden_menu');
var body = document.getElementsByClassName('base');
document.onmousemove = function(event) {
    var x = event.pageX;
    if (x < 6) {
        
        menu[0].animate({
            left: '0px'
        
        }, 300);
        body[0].animate({
            left: '285px'
        
        }, 300);
        
        menu[0].style.left = '0px';
        body[0].style.left = '285px';



    }else if (x > 285) {
        menu[0].animate({
            left: '-285px'
        }, 300);
        menu[0].style.left = '-285px';
        body[0].animate({
            left: '0'
        }, 300);
        body[0].style.left = '0px';
    }    
    


}