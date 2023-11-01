$(document).ready(function () {
  let url = 'https://hellosalut.stefanbohacek.dev/?lang=';
  $('#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    url = url + lang;
    $.get(url, function (data, textStatus, jqXHR) {
      $('DIV#hello').text(data.hello);
    });
  });

  $('#language_code').keyup(function (event) {
    if (event.keyCode === 13) {
      const lang = $('INPUT#language_code').val();
      url = url + lang;
      $.get(url, function (data, textStatus, jqXHR) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
