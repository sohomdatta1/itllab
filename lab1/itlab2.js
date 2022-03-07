$( document ).ready(function () {
    let $output = $( '.output' );
    $( 'tr > td > button' ).each( function() {
        $( this ).click(function () {
            let className = $( this ).attr('class');
            if  ( className === "AC" ) {
                $output.val("");
            } else if ( className === "backspace" ) {
                $output.val( $output.val().slice( 0, -1 ) );
            } else if ( className === "equal_to" ) {
                $output.val( eval( $output.val() ) );
            } else {
                $output.val( $output.val() + className );
            }
        });
    } )
})