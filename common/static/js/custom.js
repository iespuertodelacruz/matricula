var init_datepickers, new_application;

$(function() {
    init_datepickers();
    $("#new_application").on("click", new_application);
    $("#multienroll_level").on("change", multienroll_level_change)
});

init_datepickers = function() {
    var current_year, max_year, min_year;
    current_year = new Date().getFullYear();
    min_year = current_year - 75;
    max_year = current_year - 10;
    return $(".datepicker").datepicker({
        changeMonth: true,
        changeYear: true,
        yearRange: `${min_year}:${max_year}`
    });
};

new_application = function(event) {
    var btn;
    btn = $(this);
    if (btn.attr("href") === "#") {
        event.preventDefault();
        $(this).html("<i class='fa fa-warning'></i> ¡Perderá todos los datos!<br>Pulse de nuevo si quiere borrar<br>la matrícula actual y empezar una nueva");
        return $(this).attr("href", "/");
    } else {
        return window.location.href = "/";
    }
};

multienroll_level_change = function() {
    var select = $(this);
    if (select.val() === "0")
        $("#multienroll_btn").prop("disabled", true);
    else
        $("#multienroll_btn").prop("disabled", false);
};
