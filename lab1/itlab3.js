$( document ).ready(function () {
    $( '.update' ).click(function () {
        let $card = $( '.card' )
        let $card_text = $( '.card > .text' )
        $card.css( 'background', $( '#color' ).val());
        $card_text.css( 'font-family', $( '#font' ).val());
        $card_text.css( 'font-size', $( '#font_size' ).val());
        $card.css( 'border', $('input[name="border_style"]:checked').val())
        if ( $( '#add_picture:checked' ).val() ) {
            $( '.card > .picture' ).css( 'display', 'block' );
        } else {
            $( '.card > .picture' ).css( 'display', 'none' );
        }
        $card_text.text($( '#text' ).val());
    });
});