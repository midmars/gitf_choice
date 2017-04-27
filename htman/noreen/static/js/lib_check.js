function check_data() {
	var flag = true;

	$('#frmdata .check').each(function(){
		 if($(this).val() == ''){
			  flag = false;
			  $('#message').html($(this).attr('alt'));
		 } else if($(this).attr('type') == 'password' && $(this).val().length < 6){
	  	  flag = false;
	  	  $('#message').html('密碼長度至少為5碼以上');
	   } else if($(this).attr('id') == 'password_check' && $(this).val() != $('[name=password_bechecked]').val()){
	  	  flag = false;
	  	  $('#message').html('再次輸入之密碼不符');
	   } else if($(this).attr('id') == 'user_email'){
	      if (!validateEmail($(this).val())){
	     	   flag=false;
	     	   $('#message').html('電子郵件格式不正確');
	     	}
	   } else if($(this).attr('id') == 'user_phone'){
	      if (!validatePhone($(this).val())){
	     	   flag=false;
	     	   $('#message').html('電話格式不正確');
	     	}
	   } else if($(this).attr('id') == 'user_invoice'){
	      if (!validateNumber($(this).val())){
	     	   flag=false;
	     	   $('#message').html('統一編號格式不正確');
	     	} else if($(this).val().length != 8) {
	         flag=false;
	         $('#message').html('統一編號格式不正確');
	      }
	   }
		 
	   if (!flag) {
	   	  $(this).focus();
	      return false;
	   }
	});
	
	return flag;
}

function validateEmail(txtEmail) {
    var filter = /^([\w-\.]+)@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.)|(([\w-]+\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\]?)$/;

    if (filter.test(txtEmail)) {
        return true;
    } else {
        return false;
    }
}

function validatePhone(txtPhone) {
    var filter = /^[0-9-+]+$/;
    if (filter.test(txtPhone)) {
        return true;
    } else {
        return false;
    }
}

function validateNumber(txtNumber) {
    var filter = /^[0-9]+$/;
    if (filter.test(txtNumber)) {
        return true;
    } else {
        return false;
    }
}