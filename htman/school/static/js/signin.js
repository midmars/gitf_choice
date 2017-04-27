
    // Scrolls to the selected menu item on the page
    $(function() {
        $('a[href*=#]:not([href=#])').click(function() {
            if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') || location.hostname == this.hostname) {
              //^ 比對目標的開頭
                var target = $(this.hash);
                //hash is a property that can be found on elements that contain an href attribute/property.
                target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
                //?比對前一項0次 OR 1次
                if (target.length) {
                    $('html,body').animate({
                        scrollTop: target.offset().top
                    }, 1000);
                    return false;
                }
            }
        });
    });

  
    //     $(".id_btn").click(function(){
    //     var status= $(this).attr("id");
    //     $("p").append(status); //測試抓值
    //     $.get("/login/",{'status':status})

    //     // url="#Data";
    //     // $( location ).attr("href", url);

    // });


//身份
$(document).on('click', '#s1', function(){

var url="/school/id_s/";

var $button_just_clicked_on = $(this);
var status = $button_just_clicked_on.data('status');

var sendInfo = {
           status: status,
       };
// alert("123");

  get_ajax_data_json(url,sendInfo,function(data) 
  {   

    window.location.replace("#Data");
    
   


  });


});


//註冊
$(document).on('click', '#submit_member', function(){
var url="/school/new_member/";



json_data=$('#form_member').serialize();



  get_ajax_data_html(url,json_data,function(data) 
  {   
    
    $('#list').html(data);
    window.location.replace("#TableSeat");



  });


});
//刪除
$(document).on('click', '#delete_member', function(){
var url="/school/delete_member/";

var $button_just_clicked_on = $(this);
var name = $button_just_clicked_on.data('name');

var sendInfo = {
           name: name,
       };


  get_ajax_data_html(url,sendInfo,function(data) 
  {   
    
    $('#list').html(data);
    

  });


});










