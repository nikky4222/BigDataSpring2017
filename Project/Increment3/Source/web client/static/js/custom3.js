$(function () {

  // sorce: http://stackoverflow.com/a/22172860
  function getBase64Image(img) {
    var canvas = document.createElement("canvas");
    canvas.width = img.width;
    canvas.height = img.height;
    var ctx = canvas.getContext("2d");
    ctx.drawImage(img, 0, 0);
    var dataURL = canvas.toDataURL("image/jpeg");
//    console.log(dataURL)
    return dataURL.replace(/^data:image\/(png|jpg|jpeg);base64,/, "");
  }

  $('.thumbnail img')
    .click(function () {
      var btm_img = $(this).attr('src');
      $('#img_plc').attr('src', btm_img);
    });
var i=-1
  $("#clk").on('click', function (event) {
    $('#txt_area').hide();
        $('#txt').hide();

    $('#meow').show();
      $('#ans').show();

    var tmp_img = document.createElement("img");
    tmp_img.src = 'http://'+location.host+$('#img_plc').attr('src');
     var tmp_img = document.createElement("abc");
    tmp_img.src = 'http://'+location.host+$('#img1').attr('src');
    var base64 = getBase64Image(tmp_img);

    i=i+1
    $.ajax({
      type: "POST",
      url: "http://localhost:5000/api/predict",
      data: { imageBase64: i },
      success: function (result) {
        var res = result.results[0];
        $('#meow').hide();


      }
    });
  });
});
