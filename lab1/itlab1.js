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
            $( 'table' ).animate( {'left': '+=800px'} );
            $( 'img' ).animate( {'left': '+=800px'} );
            flag = false;
        } else {
            $( 'table' ).animate( {'left': '-=800px'} );
            $( 'img' ).css( {'left': '-=800px'} );
            flag = true;
        }
    } );
} );