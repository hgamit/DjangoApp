$(function () {

  $(".js-search-package").click(function () {
    $.ajax({
      url: '/dpickup/packages_search/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-package").modal("show");
      },
      success: function (data) {
        $("#modal-package .modal-content").html(data.html_form);
      }
    });
  });

});


function initialize() {
    autocomplete = new google.maps.places.Autocomplete(
      /** @type {!HTMLInputElement} */(document.getElementById('id_search_adrs')),
      {types: ['geocode']});
  
  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', fillInAddress);
  //}
  
  function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  var lat = place.geometry.location.lat();
  var lng = place.geometry.location.lng();
  console.log(lat); 
  console.log(lng); 
  $("#id_search_adrs_lat").val(lat.toFixed(6));
  $("#id_search_adrs_lng").val(lng.toFixed(6));
  }
  
  // Bias the autocomplete object to the user's geographical location,
  // as supplied by the browser's 'navigator.geolocation' object.
  $("#id_search_adrs").focus(function () {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds(circle.getBounds());
    });
  }
  }); //keyup
  
  
  }


