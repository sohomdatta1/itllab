$( document ).ready( () => {
    var i = 0;
    var flag = true;
    $( 'tr > td' ).each( function ( index ) {
        if ( i % 2 == 0 ) {
            $( this ).css( 'background', 'red' )
        }
        i++;
    });
    $( '.move' ).click( function () {
        if ( flag ) {
            $( 'table' ).css( 'float', 'right' );
            $( 'img' ).css( 'float', 'right' );
            flag = false;
        } else {
            $( 'table' ).css( 'float', 'left' );
            $( 'img' ).css( 'float', 'left' );
            flag = true;
        }
    } );
} );