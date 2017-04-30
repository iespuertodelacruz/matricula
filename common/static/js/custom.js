// Generated by CoffeeScript 1.10.0
var init_datepickers, prevent_close_window;

$(function() {
  init_datepickers();
  return prevent_close_window();
});

init_datepickers = function() {
  return $(".datepicker").datepicker({
    changeMonth: true,
    changeYear: true,
    yearRange: "1960:2015"
  });
};

prevent_close_window = function() {
  return window.onbeforeunload = function() {
    if (prevent_exit) {
      return "You have attempted to leave this page. Are you sure?";
    }
  };
};
