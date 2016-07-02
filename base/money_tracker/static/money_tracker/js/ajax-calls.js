  $(function() {
    $("#send-daily").click(
      function () {
      event.preventDefault();
      var to_send = '{';
      var otArr = [];
      var flag = true;
      var tbl2 = $('.daily-table tr').each(function(i) {
        var itArr = [];
        if(i > 0){
          x = ($(this).children());
            x.each(function() {
              switch($(this).attr('class')) {
                case 'company':
                  if($(this).text().length == 0){
                    flag = false;
                    return;
                  }
                  break;
                case 'amount-in':
                  if($(this).text().length == 0 && flag){
                    $(this).text("0");
                  }
                  break;
                case 'amount-out':
                  if($(this).text().length == 0 && flag){
                    $(this).text("0");
                  }
                  break;
              }
              if(flag && $(this).attr('class') != 'unnecessary'){
                itArr.push('"' + $(this).text() + '"');
              }else if(flag && $(this).attr('class') === 'unnecessary'){
                console.log($(this).children('input').is(":checked"));
                itArr.push('"' + $(this).children('input').is(":checked") + '"');
              } else {
                return;
              }
          });
          if(flag){
            otArr.push('"' + i + '": [' + itArr.join(',') + ']');
          }else{
            flag = true;
          }
        }
      });
      to_send += otArr.join(",") + '}'
      send_json(to_send);
    });
  });

  function send_json(json_string) {
    $.ajax({
      url : "get_data/", // the endpoint
     type : "POST", // http method
     data : { json_string : json_string }, // data sent with the post request

        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
  };
