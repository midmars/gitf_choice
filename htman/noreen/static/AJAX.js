function post_ajax_data(url, encodedata, success)
{
   $.ajax({
      type:"POST",
      url:url,
      data:encodedata,
      dataType:"json",
      restful:true,
      cache:false,
      timeout:20000,
      async:true,
      success:function(data){
         success.call(this, data);
      },
      error:function(data){
         alert("connect failed");
      }
   });
}

function get_ajax_data(url, success)
{
   $.ajax({
      type:"GET",
      url:url,
      dataType:"json",
      restful:true,
      cache:false,
      timeout:20000,
      async:true,
      success:function(data){
         success.call(this, data);
      },
      error:function(data){
         alert("connect failed");
      }
   });
}
function get_ajax_data_html(url,encodedata,success)
{
   $.ajax({
      type:"GET",
      url:url,
      data:encodedata,
      dataType:"html",
      restful:true,
      cache:false,
      timeout:20000,
      async:true,
      success:function(data){
         success.call(this, data);
      },
      error:function(data){
         alert("connect failed");
      }
   });
}

function get_ajax_data_json(url,encodedata,success)
{
   $.ajax({
      type:"GET",
      url:url,
      data:encodedata,
      dataType:"json",
      restful:true,
      cache:false,
      timeout:20000,
      async:true,
      success:function(data){
         success.call(this, data);
      },
      error:function(data){
         alert("connect failed");
      }
   });
}

function ajax_data(type, url, success)
{
   $.ajax({
      type:type,
      url:url,
      dataType:"json",
      restful:true,
      cache:false,
      timeout:20000,
      async:true,
      success:function(data){
         success.call(this, data);
      },
      error:function(data){
         alert("connect failed");
      }
   });
}
