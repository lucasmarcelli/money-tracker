

  $('#example').click( function(event){
      event.preventDefault();
      var to_send = 'The quick brown fox jumps over the lazy dog.';

    $.ajax({
      url : "get_data/", // the endpoint
     type : "POST", // http method
     data : { text : to_send }, // data sent with the post request

        success : function(json) {
            console.log(json); // log the returned json to the console
            console.log("success"); // another sanity check
        },

        // handle a non-successful response
        error : function(xhr,errmsg,err) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
});
