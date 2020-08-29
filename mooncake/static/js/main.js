$( document ).ready(function() {

  $('.input-wrapper input').each(function() {
    var $hint = $(this).closest('.input-wrapper').find('.input-hint');
    if ($(this).val() === '') {
      $hint.removeClass('active');
    } else {
      $hint.addClass('active');
    }
  });

  $('.input-wrapper').on('focus', 'input', function() {
    $(this).prev('.input-hint').addClass('active');
  });

  $('.input-wrapper').on('click', function() {
    var $wrapper = $(this);

    $wrapper.find('input').focus();
  });

  $('.input-wrapper').on('blur', 'input', function(e) {
    var $wrapper = $(this).parent();

    if ($wrapper.find('input').val() !== '') {
      $wrapper.find('.input-hint').addClass('active');
    }

  });

  $('form').on('submit', function(e) {
    var $button = $(this).find('button.confirm');
    var $buttonText = $button.find('.text');

    if ($buttonText.hasClass('hide')) {
      e.preventDefault();
    } else {
      $buttonText.addClass('hide');
      $button.find('i').removeClass('hide');
    }
  });

});
