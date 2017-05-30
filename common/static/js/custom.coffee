$ ->
    init_datepickers()
    $("#new_application").on("click", new_application)

init_datepickers = ->
    $(".datepicker").datepicker
        changeMonth: true,
        changeYear: true,
        yearRange: "1960:2015"

new_application = (event) ->
    btn = $(this)
    if btn.attr("href") == "#"
        event.preventDefault()
        $(this).html("Perderá todos los datos!<br>Pulse de nuevo si quiere continuar")
        $(this).attr("href", "/")
    else
        window.location.href = "/"
