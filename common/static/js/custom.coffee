$ ->
    init_datepickers()

init_datepickers = ->
    $(".datepicker").datepicker
        changeMonth: true,
        changeYear: true,
        yearRange: "1960:2015"
