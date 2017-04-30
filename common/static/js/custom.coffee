$ ->
    init_datepickers()
    prevent_close_window()

init_datepickers = ->
    $(".datepicker").datepicker
        changeMonth: true,
        changeYear: true,
        yearRange: "1960:2015"

prevent_close_window = ->
    window.onbeforeunload = ->
        if prevent_exit
            return "You have attempted to leave this page. Are you sure?"
