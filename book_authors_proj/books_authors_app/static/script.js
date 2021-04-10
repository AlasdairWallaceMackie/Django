
$(document).ready(function(){

    console.log("Script Linked")


    $('.add-object').click(function(){
        console.log("Attach clicked")
        var form_data = $(this).parent().serialize();
        console.log("Form data: " + form_data);
        
        if(form_data == undefined){
            console.log("FORM DATA UNDEFINED");
            return false;
        }
        else{
            $.post('/add_object', form_data);
        }
        location.reload();
        return false;
    });

    $('.delete-object').click(function(){
        console.log("Deleting object");
        form_data = $(this).parent().serialize();
        $.post('/delete_object', form_data)

        location.reload();
        return false;
    });

    $('.attach-object').click(function(){
        console.log("Attaching object");
        form_data = $(this).parent().serialize();

        if(form_data == undefined){
            console.log("FORM DATA UNDEFINED")
            return false;
        }
        else{
            $.post('/attach_object', form_data)
            location.reload();
        }

        location.reload();
        return false;
    });

});