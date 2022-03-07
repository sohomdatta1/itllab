window.prices = {
    "HP": {
        "Laptop": 8000,
        "Mobile": 4000
    },
    "Nokia": {
        "Laptop": 9000,
        "Mobile": 3000
    },
    "Samsung": {
        "Laptop": 10000,
        "Mobile": 2000
    },
    "Motorola": {
        "Laptop": 1500,
        "Mobile": 25000
    },
    "Apple": {
        "Laptop": 90000,
        "Mobile": 20000
    }
}

window.total_bill = 0;

$( document ).ready(function () {
    $( '.produce_bill' ).click(function () {
        total_bill =  prices[$( '#brand' ).val()][$( 'input[name="type"]:checked' ).val()] * $( '#qty' ).val();
        alert(total_bill)
    });
});