

    function init() {

        // To Disable Submit Button By Default
        $("#submit").attr('disabled', 'disabled');
        //$("label[for='id_shipping_distance']").text("");
        //$("label[for='id_shipping_charge']").text("");
        //$("#id_shipping_distance").attr('disabled', 'disabled');
        //$("#id_shipping_charge").attr('disabled', 'disabled');
        //$("form").keyup(function() {
        // To Disable Submit Button
        //$("#submit").attr('disabled', 'disabled');
            // Validating Fields
          //  var shipping_distance = $("#id_shipping_distance").val();
           // var shipping_charge = $("#id_shipping_charge").val();
           // if (!(shipping_distance == "" || shipping_charge == "")) {
            // To Enable Submit Button
            //$("#submit").text('disabled');
           // $("#submit").removeAttr('disabled');
            //}
        //});
    
        var distance_in_mile = 0.0;
        var duration_value = 0;
        // calculate distance
        $('#id_delivery_adrs').change(calculateDistance);
        $('#id_pickup_adrs').change(calculateDistance);
        //document.getElementById("id_delivery_adrs").onchange=calculateDistance();
        //document.getElementById("id_pickup_adrs").onchange=calculateDistance();
        function calculateDistance() {
            if ($('#id_pickup_adrs').val() == "" || $('#id_delivery_adrs').val() == "") return;
            if ($('#id_pickup_adrs').val() == $('#id_delivery_adrs').val())
            {
                alert("Please provide different addresses!");
                return;
            } 
            var origin = $('#id_pickup_adrs option:selected').text();
            var destination = $('#id_delivery_adrs option:selected').text();
            console.log(origin);
            console.log(destination);
            var service = new google.maps.DistanceMatrixService();
            service.getDistanceMatrix(
                {
                    origins: [origin],
                    destinations: [destination],
                    travelMode: google.maps.TravelMode.DRIVING,
                    unitSystem: google.maps.UnitSystem.IMPERIAL, // miles and feet.
                    // unitSystem: google.maps.UnitSystem.metric, // kilometers and meters.
                    avoidHighways: false,
                    avoidTolls: false
                }, callback);
        }
        // get distance results
        function callback(response, status) {
            if (status != google.maps.DistanceMatrixStatus.OK) {
                $('#result').html(err);
            } else {
                var origin = response.originAddresses[0];
                var destination = response.destinationAddresses[0];
                if (response.rows[0].elements[0].status === "ZERO_RESULTS") {
                    $('#result').html("Better get on a plane. There are no roads between "  + origin + " and " + destination);
                } else {
                    var distance = response.rows[0].elements[0].distance;
                    var duration = response.rows[0].elements[0].duration;
                    console.log(response.rows[0].elements[0].distance);
                    var distance_in_kilo = distance.value / 1000; // the kilom
                    distance_in_mile = distance.value / 1609.34; // the mile
                    var duration_text = duration.text;
                    duration_value = (duration.value/(60*60));
                    $('#id_shipping_distance').val(distance_in_mile.toFixed(3));
                    //$("label[for*='test']").html("others");
                    //$('#id_shipping_distance').css('background-color', '#3CBC8D');
                    // $('#in_mile').text(distance_in_mile.toFixed(2));
                    // $('#in_kilo').text(distance_in_kilo.toFixed(2));
                    // $('#duration_text').text(duration_text);
                    // $('#duration_value').text(duration_value);
                    // $('#from').text(origin);
                    // $('#to').text(destination);
                }
            }
        }

        $('#id_delivery_timeline').change(calculateCharges);
        $('#id_package_dimensions').change(calculateCharges);
        function calculateCharges() {
            if ($('#id_package_dimensions').val() == "" || $('#id_delivery_timeline').val() == "") return;
            var charge = 5.0;
            var package_size = document.getElementById("id_package_dimensions").value;
            var delivery_timeline = document.getElementById("id_delivery_timeline").value;
            if(distance_in_mile>50.0 || duration_value>4.0 ){
                var x0 = document.getElementById("id_delivery_timeline").options[0].disabled = true;
                var x1 = document.getElementById("id_delivery_timeline").options[1].disabled = true;
              
                if(delivery_timeline== "Same day Delivery(24x1)"){
                    
                    charge += 10;

                }
            
            
            } else if (distance_in_mile>50.0 || duration_value>24.0 ){
                var x0 = document.getElementById("id_delivery_timeline").options[0].disabled = true;
                var x1 = document.getElementById("id_delivery_timeline").options[1].disabled = true;                    
                var x2 = document.getElementById("id_delivery_timeline").options[2].disabled = true;                    
            
                charge += 5;
            
            } else{
                if((package_size == "Small (Under 15 x 12 x 1)" || package_size == "Medium (Under 15 x 12 x 6)") && (delivery_timeline== "Within 2 Hours" || delivery_timeline== "Within 4 Hours")){

                    charge += 10;

                }  else if(package_size == "Large (Under 24 x 12 x 6)" && (delivery_timeline== "Within 2 Hours" || delivery_timeline== "Within 4 Hours")){

                    charge += 12;

                }else if(delivery_timeline== "Same day Delivery(24x1)"){
                    
                    charge += 8;

                }

            }
            $('#id_shipping_charge').val(charge.toFixed(3));
            var shipping_distance = $("#id_shipping_distance").val();
            var shipping_charge = $("#id_shipping_charge").val();
            if (!(shipping_distance == "" || shipping_charge == "")) {
            // To Enable Submit Button
            //$("#submit").text('disabled');
            $("#submit").removeAttr('disabled');
            }
            //$('#id_shipping_charge').css('background-color', '#3CBC8D');
           // $('#id_procees').val(charge.toFixed(3));
        }

    }

