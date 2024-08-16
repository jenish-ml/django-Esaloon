$(document).ready(function(){
  
    $('.btn-submit-reg').click(function(){
      var name = $('.name').val();
      var pass = $('.pass').val();
      var email = $('.email').val();
      var street = $('.street').val();
      var loc = $('.loc').val();
      var land = $('.land').val();
      var contact = $('.phn').val();
      var flag = true;
      var regex = /^([a-zA-Z0-9_.+-])+\@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;    
      if(name == ''){
        flag =false
        alert("username should not be null");
      }
      else if(pass == ''){
        flag =false
        alert("password should not be null");
      }
      
      else if(!regex.test(email)){
          flag = false    
          alert("invalid email id");   
      }
    
   
      else if(street == ''){
        flag =false
        alert("street name should not be null");
      }
      else if(loc == ''){
        flag =false
        alert("Location should be null");
      }
      else if(land == ''){
        flag =false
        alert("landmark should not be null");
      }
      else if(contact.length != 10){
        flag = false
        alert("invalid contact");
    }

      if(!flag) 
      {
          return false;
      }
    })
    $('.btn-bookings').on('click', function(){
      ct = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        type: 'post',
        url: '/bookings-by-date',
        data: { d: $('.bd').val(), csrfmiddlewaretoken: ct, s: '', e: '' },
        dataType: 'json',
        async: true,
        success: function(doc){
          data = $.parseJSON(doc.data);
          var htmlStr = "";
          $.each(data, function(i, v){
            htmlStr += "<tr><td>" + v.fields.booking_time + "</td><td>" + v.fields.end_time + "</td><tr>";
          })
          $('#bkgsModal .bk-content tbody').html(htmlStr);
          $('#bkgsModal').modal('show');
        },
        error: function(err) {
          console.log(JSON.stringify(err))
        }
      });
    })
    $('.btn-submit-pay').on('click', function(){
        var time = $('input[name="booking_time"]').val();
        var open = $('input[name="booking_time"]').attr('data-open');
        var close = $('input[name="booking_time"]').attr('data-close');
        var date = new Date($('input[name="booking_date"]').val());
        var weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
        if(date.getDay() == parseInt($('input[name="booking_date"]').attr('data-hd'))) {
          alert("All " + weekdays[date.getDay()] + " are holidays");
          return false;
        }
        else if(time < open) {
          alert("Shop will open @ " + open);
          return false;
        }
        else if(time > close) {
          alert("Shop will close @ " + close);
          return false;
        }
    })
    $('.btn-search-bkg').on('click', function() {
      var sd = $('.sd').val();
      var ed = $('.ed').val();
      ct = $('input[name="csrfmiddlewaretoken"]').val();
      $.ajax({
        type: 'post',
        url: '/bookings-by-date',
        data: { d: $('.bd').val(), csrfmiddlewaretoken: ct, s: sd, e:ed },
        dataType: 'json',
        async: true,
        success: function(doc){
          console.log(doc);
          data = $.parseJSON(doc.data);
          var htmlStr = "";
          $.each(data, function(i, v){
            htmlStr += "<tr><td>" + v.fields.booking_time + "</td><td>" + v.fields.end_time + "</td><tr>";
          })
          $('#bkgsModal .bk-content tbody').html(htmlStr);
          $('#bkgsModal').modal('show');
        },
        error: function(err) {
          console.log(JSON.stringify(err))
        }
      });
      return false;
    })
    function lastDate() {
        date = new Date();
        date.setDate(date.getDate() + (+4));
        var dd = date.getDate();
        var mm = date.getMonth() + 1;
        var y = date.getFullYear();
        var someFormattedDate = mm + '-' + dd + '-' + y;
        return new Date(someFormattedDate);
    }
  }); 



  $(document).ready(function() {
    $('#compareBtn').on('click', function() {
      var email = $('.email').val();
  
      // Send the email variable to the server-side for comparison
      $.ajax({
        type: 'POST',
        url: '/compare_email/',  // Replace with the URL of your Django view
        data: { email: email },
        dataType: 'json',
        success: function(response) {
          // Process the response from the server-side
          if (response.match) {
            alert('The email matches the value in the database.');
          } else {
            alert('The email does not match the value in the database.');
          }
        },
        error: function(xhr, status, error) {
          // Handle AJAX error, if any
          console.error(error);
        }
      });
    });
  });
  