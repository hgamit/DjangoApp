$(function () {

  $("#modal-package1").on("submit", ".js-package-search-form", function () {
    var form = $(this);
    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $("#package-table tbody").html(data.html_packages_list);  // <-- Replace the table body
           // $("#modal-package").modal("hide");  // <-- Close the modal
        }
        else {
            alert("Address Not Found!"); 
          //$("#modal-package .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  });


$("#id_search_adrs").focus(function () {
    autocomplete = new google.maps.places.Autocomplete(
      /** @type {!HTMLInputElement} */(document.getElementById('id_search_adrs')),
      {types: ['geocode']});
      //console.log("HERElat"); 
  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', fillInAddress);
  //}
  
  function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();
  var lat = place.geometry.location.lat();
  var lng = place.geometry.location.lng();
  console.log("Lat:"+lat); 
  console.log("Lng:"+lng); 
  $("#id_search_adrs_lat").val(lat.toFixed(6));
  $("#id_search_adrs_lng").val(lng.toFixed(6));
  }
});

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
  

    $( "#get-mylocation" ).click( function(e) {
        e.preventDefault();
 
        /* Chrome need SSL! */
        var is_chrome = /chrom(e|ium)/.test( navigator.userAgent.toLowerCase() );
        var is_ssl    = 'https:' == document.location.protocol;
        if( is_chrome && ! is_ssl ){
            return false;
        }
 
        /* HTML5 Geolocation */
        navigator.geolocation.getCurrentPosition(
            function( position ){ // success cb
 
                /* Current Coordinate */
                var lat = position.coords.latitude;
                var lng = position.coords.longitude;
                var google_map_pos = new google.maps.LatLng( lat, lng );
 
                /* Use Geocoder to get address */
                var google_maps_geocoder = new google.maps.Geocoder();
                google_maps_geocoder.geocode(
                    { 'latLng': google_map_pos },
                    function( results, status ) {
                        if ( status == google.maps.GeocoderStatus.OK && results[0] ) {
                            console.log( results[0].formatted_address );
                        }
                    }
                );
            },
            function(){ // fail cb
            }
        );
    });

});
