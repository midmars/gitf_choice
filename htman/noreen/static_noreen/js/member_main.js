//答題
$(document).on('click', '#check_submit', function(){

var url="/noreen/check/";



json_data=$('#answer_form').serialize();



  get_ajax_data_json(url,json_data,function(data) 
  {   
    
    switch (data.state) {
    case 0:
      //未完成
    　url2 = "/noreen/home/"
      window.location.replace(url2);
      break;

    case 1:
      
    　url3 = "/noreen/"
      window.location.replace(url3);

    　break;

    default:
    　break;
    }


  });


});








