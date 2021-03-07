
if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    // код для мобильных устройств
    var menu = document.getElementsByClassName('hidden_menu');
    var body = document.getElementsByClassName('base');
    var knopka = document.getElementsByClassName('knopka');
    var btm = document.getElementsByClassName('click');
    knopka.style.display == 'block';
    btm.onclick = function(){
        if(menu.style.left == '-285'){
            menu[0].animate({
                left: '0px'
            
            }, 300);
            body[0].animate({
                left: '285px'
            
            }, 300);
            menu[0].style.left = '0px';
            body[0].style.left = '285px';

        }else {
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
  } else {
    // код для обычных устройств
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
}
