/* check off specific todos by clicking */
var ul = $("ul");
var lis = $("li");
var spans = $("span");
var input = $("input[type='text']");
var submit = $("button[type='submit']");
var error = $("#error");
var errorBtn = $("#error button");
// when a li is clicked inside an ul
ul.on("click", "li", function() {
  $(this).toggleClass("checkOff");
});



// Ajax Call for adding todos
submit.on("click", function(event) {
  if ($.trim(input.val()) == '') {
    error.fadeIn(1000)
    errorBtn.on("click", function() {
      error.fadeOut()
    })
  } else {
    $.ajax({
      data: {
        todo: input.val()
      },
      type: 'POST',
      url: '/_post'
    }).done(function(data) {
      input.val("")
      ul.append('<li id=' + data.id + '><span><i class="fa fa-trash"></i></span>' + data.post + '</li>')
    })
  }
  event.preventDefault();
})

// Ajax Call for removing todos
ul.on("click", "span", function(event) {
  $(this).parent().fadeOut(1000, function() {
    $(this).remove();
  })
  $.ajax({
    data: {
      id: $(this).parent().attr('id'),
    },
    type: 'POST',
    url: '/' + $(this).parent().attr('id') + '/_delete'
  }).done(function(data) {
    console.log(data.message)
  })

  event.stopPropagation()
})
