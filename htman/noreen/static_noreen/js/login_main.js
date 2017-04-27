//新使用者
$(document).on('click', '#member_submit', function(){
var url="/noreen/login_member/";



json_data=$('#login_form').serialize();



  get_ajax_data_json(url,json_data,function(data) 
  {   
    
    if(data.state == 0){  

        alert(data.errors);


        }
    if(data.state == 1 ){
      url2 = "/noreen/home/"
      window.location.replace(url2);

      
    }  

  });


});


//#inputTarget是你input的ID
//讓 input 按下Enter 就送出
$("#kkk").keypress(function(e){
  code = (e.keyCode ? e.keyCode : e.which);
  if (code == 13)
  {
      var url="/noreen/login_member/";



      json_data=$('#login_form').serialize();

      get_ajax_data_json(url,json_data,function(data) 
      {   
        
        if(data.state == 0){  

            alert(data.errors);


            }
        if(data.state == 1 ){
          url2 = "/noreen/home/"
          window.location.replace(url2);

          
        }  

      });
      alert("!@3");
      
      return false;
  }
});



