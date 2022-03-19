$( document ).ready(function() {
    window.onhashchange = function () {
        var elements = [ 
            'read',
            'create',
            'delete',
            'update',
        ];

        
    
        elements.forEach( elem => $( '#' + elem ).hide() );
        elements.forEach( elem => $( '.nav-' + elem ).find('a').removeClass( 'active' ) );
        $( '.nav-' + location.hash.slice(1) ).find('a').addClass( 'active' )
        $( location.hash ).show();
    }

    location.hash ='#create';

});