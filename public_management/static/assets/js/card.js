
$(document).ready(function(){
    $('.btn-submit-pay').click(function(){
      var number = $('.number').val();
      var cvv = $('.cvv').val();
      var d = $('.d').val();
      var flag = true;
      if(number.length != 16){
          flag = false    
          alert("invalid card number");   
      }
      if(cvv.length != 3){
        flag = false    
        alert("invalid cvv number");   
        }
      if(d.length != 5){
            flag = false    
            alert("invalid validity date");   
        }
        if(!flag) 
        {
          return false;
        }
    })
  }); 