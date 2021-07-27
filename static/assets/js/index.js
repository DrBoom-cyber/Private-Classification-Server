document.addEventListener('keydown', function (event) {
  if (event.key == 'a') {
    $.ajax({
      type : "POST",
      url : "classify",
      data : {
        label : 'letter_a',
        hash : 'fake_hash'
      }
    });
  }
});