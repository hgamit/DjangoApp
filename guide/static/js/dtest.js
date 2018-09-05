$(document).ready(function() {
    
    $("#submit").attr('disabled', 'disabled');

    
    // calculate distance by DRIVING MODE
    $('#id_package_description').change(calcDistance);

    //$( "#id_delivery_adrs" ).unbind();
    
    function calcDistance(){
        var package_description = $('#id_package_description').val();
       
        if (!(package_description == "")) {
            $('#id_package_descriptionhid').val(package_description+" hidden");
        } else{
            console.log("Please provide desc!");
            alert("Please provide desc!");
            return;
        } //else check

        
    } // calcDistance


    $("form").change(function() {
        // To Disable Submit Button
        $("#submit").attr('disabled', 'disabled');
        // Validating Fields
        var package_description = $("#id_package_description").val();
        var package_descriptionhid = $("#id_package_descriptionhid").val();

        console.log("package_description 1"+package_description+" "+package_descriptionhid);
       
        if (!( package_description == "" || package_descriptionhid == "")) {            
            
                // To Enable Submit Button
                console.log("enabled")
                $("#submit").removeAttr('disabled');
                $("#submit").css({
                "cursor": "pointer",
                "box-shadow": "1px 0px 6px #333"
                });
        
        }//if null check
    }); //keyup
});//ready
