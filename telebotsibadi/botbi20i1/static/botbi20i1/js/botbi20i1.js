/* Открытие меню */
if(/iPhone|iPad|iPod|Android/i.test(navigator.userAgent)){
    
}else{
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

    }


//<i class="far fa-arrow-alt-circle-right"></i>

var kt_block = document.getElementsByClassName('kt_check');
var KT = document.getElementsByClassName('KT');
var rating = document.getElementById('rating');
for (let i = 0; i < kt_block.length; i++){
    kt_block[i].onclick = function (){
        let labs_kt = document.getElementsByClassName('labs_kt');
        
        
        if(labs_kt[i].style.display == 'block'){
            let img = document.getElementById(i);
            console.log(img);
            labs_kt[i].style.display = null;
            img.className = 'far fa-arrow-alt-circle-right'
            if(i == 2){
                rating.style.paddingTop = '15px';
            } else {
                KT[i+1].style.paddingTop = '15px';
            }
        } else {
            let img = document.getElementById(i);
            labs_kt[i].style.display = 'block';
            if(i == 2){
                rating.style.paddingTop = labs_kt[i].scrollHeight;
            } else {
                KT[i+1].style.paddingTop = labs_kt[i].scrollHeight;
            }
            img.className = 'far fa-arrow-alt-circle-down';     
        }
    }
}




