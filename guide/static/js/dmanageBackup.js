$(document).ready(function() {
    
    $("#submit").attr('disabled', 'disabled');

    
    // calculate distance by DRIVING MODE
    $('#id_delivery_adrs').change(calcDistance);
    $('#id_pickup_adrs').change(function(){ 
        if($("#id_delivery_adrs").val() != ""){
            console.log("pickup executed");
            calcDistance();
        }
    
    });
    //$( "#id_delivery_adrs" ).unbind();
    var calcStatus = false;
    var distance_in_mile = 0.0;
    console.log("start "+distance_in_mile);
    var duration_value = 0;
    
    function calcDistance(){
        var pickup_adrs = $('#id_pickup_adrs option:selected').text();
        var delivery_adrs = $('#id_delivery_adrs option:selected').text();

        if (!(pickup_adrs == "---------" || delivery_adrs == "---------" ||  pickup_adrs==delivery_adrs )) {
            
            console.log("called calcDistance");
            // calculate distance by DRIVING MODE
            distance(pickup_adrs, delivery_adrs, "DRIVING", "IMPERIAL");
            distance(pickup_adrs, delivery_adrs, "BICYCLING", "IMPERIAL");
    
            var transit_duration = $("#id_transit_duration").val();
            distance(pickup_adrs, delivery_adrs, "TRANSIT", "IMPERIAL");

        } else{
            console.log("Please provide both and different addresses!");
            alert("Please provide both and different addresses!");
            $('#id_pickup_adrs').prop('selectedIndex','0');
            $('#id_delivery_adrs').prop('selectedIndex','0');
            //$( "#id_delivery_adrs" ).unbind("change");

            return;
        } //else check

        
    } // calcDistance

    //Calculations Blueprint distance

    //var origin_val = $('#id_pickup_adrs').val();
    //var destination_val = $('#id_delivery_adrs').val();
    
    function distance (origin, destination, mode, unit) {
            var service = new google.maps.DistanceMatrixService();
            tmode = "google.maps.TravelMode."+mode;
            usystem = "google.maps.UnitSystem."+unit;
            service.getDistanceMatrix(
                {
                    origins: [origin],
                    destinations: [destination],
                    travelMode: mode,
                    unitSystem: google.maps.UnitSystem.IMPERIAL, // miles and feet.
                    // unitSystem: google.maps.UnitSystem.metric, // kilometers and meters.
                    avoidHighways: false,
                    avoidTolls: false
                }, function(response, status) {callback(response, status, mode)});
        
            } // function distance

    function callback (response, status, mode) {
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
                    //console.log(response.rows[0].elements[0].distance);
                    var distance_in_kilo = distance.value / 1000; // the kilom
                    distance_in_mile = distance.value / 1609.34; // the mile
                    var duration_text = duration.text;
                    duration_value = (duration.value/(60*60));
                
                    if (mode == "DRIVING") {
                    console.log(distance_in_mile+" callabck "+duration_value);
                    $("#id_driving_distance").val(distance_in_mile.toFixed(3));
                    $("#id_driving_duration").val(duration_value);

                    if(distance_in_mile>50 && duration_value>4.0 && duration_value<24.0){
                        console.log("4 to 24 hours");
                        $("#id_delivery_timeline option[value='Within 2 Hours']").remove();
                        $("#id_delivery_timeline option[value='Within 4 Hours']").remove();
        
                    } else if (distance_in_mile>50.0 || duration_value>24.0 ){
                        console.log("more than 24 hours");
                        $("#id_delivery_timeline option[value='Within 2 Hours']").remove();
                        $("#id_delivery_timeline option[value='Within 4 Hours']").remove();
                        $("#id_delivery_timeline option[value='Same day Delivery(24x1)']").remove();
                            
                    } else{
                        console.log("option add")
                        var option2hour = ($("#id_delivery_timeline option[value='Within 2 Hours']").length > 0);
                        var option4hour = ($("#id_delivery_timeline option[value='Within 4 Hours']").length > 0);
                        var optionday = ($("#id_delivery_timeline option[value='Same day Delivery(24x1)']").length > 0);
                        if(!option2hour && duration_value<2.0)
                        {
                            $('#id_delivery_timeline').prepend("<option value='Within 2 Hours'>Within 2 Hours</option>");
                        }
                        if(!option4hour && duration_value<4.0)
                        {
                            $('#id_delivery_timeline').prepend("<option value='Within 4 Hours'>Within 4 Hours</option>");
                        }
                        if(!optionday && duration_value<24.0)
                        {
                            $('#id_delivery_timeline').prepend("<option value='Same day Delivery(24x1)'>Same day Delivery(24x1)</option>");
                        }
                    } 
                  }  else if(mode == "BICYCLING"){
                    console.log(distance_in_mile+" callabck "+duration_value);
                    $("#id_bicycling_distance").val(distance_in_mile.toFixed(3));
                    $("#id_bicycling_duration").val(duration_value);
                    
                  }   else{
                    console.log(distance_in_mile+" callabck "+duration_value);
                    $("#id_transit_distance").val(distance_in_mile.toFixed(3));
                    $("#id_transit_duration").val(duration_value);
                  }           
                }
            
            }
       
       
        }; // function callback


    $("form").change(function() {
        // To Disable Submit Button
        $("#submit").attr('disabled', 'disabled');
        // Validating Fields
        var package_type = $("#id_package_type").val();
        console.log("package_type 1"+package_type);
        var package_description = $("#id_package_description").val();
        var package_weight = $("#id_package_weight").val();
        var package_dimensions = $("#id_package_dimensions").val();
        var package_value = $("#id_package_value").val();
        var delivery_timeline = $("#id_delivery_timeline").val();
        var driving_distance = $("#id_driving_distance").val();
        var driving_duration = $("#id_driving_duration").val();
        var bicycling_dist = $("#id_bicycling_distance").val();
        var bicycling_duration = $("#id_bicycling_duration").val();
        var transit_dist = $("#id_transit_distance").val();
        var transit_duration = $("#id_transit_duration").val();

        // var filter = /^[w-.+]+@[a-zA-Z0-9.-]+.[a-zA-z0-9]{2,4}$/;
        //console.log("Driving 1"+distance_in_mile+" "+driving_duration);        
        if (!(driving_distance == 0.0 || bicycling_dist == 0.0 || transit_dist == 0.0 || driving_duration == 0 || bicycling_duration == 0 || transit_duration == 0)) {
            calcStatus = true;
        }//if approximations null check
    
        if (!(package_type == "" || 
        package_description == "" || package_weight == "" || package_dimensions == "" || package_value == ""
        || delivery_timeline == "" )) {            
            
            if (calcStatus) {
                //var rate_message = "Proceed and pay approx. USD " + charge+"?";
                //$("#submit").text(rate_message);
                // To Enable Submit Button
                console.log("enabled")
                $("#submit").removeAttr('disabled');
                $("#submit").css({
                "cursor": "pointer",
                "box-shadow": "1px 0px 6px #333"
                });
         }//if approximations null check
        }//if null check
    }); //keyup
});//ready
