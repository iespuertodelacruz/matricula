var init_datepickers, new_application;

$(function() {
  init_datepickers();
  return $("#new_application").on("click", new_application);
});

init_datepickers = function() {
  var current_year, max_year, min_year;
  current_year = new Date().getFullYear();
  min_year = current_year - 75;
  max_year = current_year - 10;
  return $(".datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: min_year + ":" + max_year
  });
};

new_application = function(event) {
  var btn;
  btn = $(this);
  if (btn.attr("href") === "#") {
    event.preventDefault();
    $(this).html("¡Perderá todos los datos!<br>Pulse de nuevo si quiere continuar");
    return $(this).attr("href", "/");
  } else {
    return window.location.href = "/";
  }
};
