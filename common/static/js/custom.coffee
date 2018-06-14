$ ->
    init_datepickers()
    $("#new_application").on("click", new_application)

init_datepickers = ->
    current_year = new Date().getFullYear()
    min_year = current_year - 75
    max_year = current_year - 10
    $(".datepicker").datepicker
        changeMonth: true,
        changeYear: true,
        yearRange: "#{min_year}:#{max_year}"

new_application = (event) ->
    btn = $(this)
    if btn.attr("href") == "#"
        event.preventDefault()
        $(this).html("<i class='fa fa-warning'></i> ¡Perderá todos los datos!<br>Pulse de nuevo si quiere borrar<br>la matrícula actual y empezar una nueva")
        $(this).attr("href", "/")
    else
        window.location.href = "/"
