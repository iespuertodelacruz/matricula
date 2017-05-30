var init_datepickers, new_application;

$(function() {
  init_datepickers();
  return $("#new_application").on("click", new_application);
});

init_datepickers = function() {
  return $(".datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: "1960:2015"
  });
};

new_application = function(event) {
  var btn;
  btn = $(this);
  if (btn.attr("href") === "#") {
    event.preventDefault();
    $(this).html("Perderá todos los datos!<br>Pulse de nuevo si quiere continuar");
    return $(this).attr("href", "/");
  } else {
    return window.location.href = "/";
  }
};
