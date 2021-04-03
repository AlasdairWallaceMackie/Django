$(document).ready(function(){

    console.log('Script is linked');
    
    $('.delete_button').click(function(){
        // Create warning window

        var form_data = $(this).parent().serialize(); //Used later to identify which X was clicked

        console.log("Showing delete confirmation")
        $('#wrapper').css({"filter": "blur(6px)", "pointer-events": "none"})

        $('#wrapper').after(`
            <div id="delete_warning">
                <h1>Are you sure you want to delete this class?</h1>
                <button id="warning_yes">YES</button>
                <button id="warning_no">NO</button>
            </div>
            `)

        //If user presses escape, undo changes and return false
        $(document).keydown(function(e){
            // console.log("Key: " + e.which)
            if( e.which == 27){ //Escape Key
                console.log("Escape pressed")
                warningClosed();

            }
        });
        $('#warning_no').click(function(){ //User clicks NO
            console.log("User clicked 'NO'");
            warningClosed();
        });
        $('#delete_warning').click(function(e){ //User clicks warning box, gets ignored
            e.stopPropagation();
        });
        $(document).click(function(){ //User clicks outside of box
            console.log("Document clicked, cancelling warning")
            warningClosed();
        });

        //USER CLICKS YES
        $('#warning_yes').click(function(){
            console.log(form_data);
            $.post('/delete', form_data);
            warningClosed();
            location.reload()
        });

        return false;
    });

    function warningClosed(){
        $('#delete_warning').remove();
        $('#wrapper').css({"filter": "none", "pointer-events": "initial"})
        $(document).off("click")
    }
    
});