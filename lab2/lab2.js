$( document ).ready(function() {
    
    function changeTabs(tab) {
        var elements = [ 
            'read',
            'create',
            'delete',
            'update',
        ]; 
        elements.forEach( elem => $( '#' + elem ).hide() );
        elements.forEach( elem => $( '.nav-' + elem ).find('a').removeClass( 'active' ) );
        $( '.nav-' + tab ).find('a').addClass( 'active' )
        $( '#' + tab ).show();
    }

    window.onhashchange = function () {
        changeTabs( location.hash.substring(1) );
    }

    location.hash = 'create';

    changeTabs( 'create' );

});