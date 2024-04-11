$(document).ready(function () {
  var modal = $("#large-image-modal");
  var slider = $("#slider");
  var images = slider.find("img");
  var picWidth = 200;
  var poz = 0;
  $("li").each(function () {
    poz += picWidth;
    $(this).css("left", poz);
  });

  function slide() {
    $("li").animate({ left: "+=10px" }, 100, again);
  }

  function notslide() {
    $("li").stop(true, false);
  }

  function again() {
    var left = $(this).parent().offset().left + $(this).offset().left;
    console.log("left=" + left);
    if (left >= 1200) {
      $(this).css("left", left - 1200);
    }
    slide();
  }

  slide();

  images.on("click", function (event) {
    event.preventDefault();
    var imageSrc = $(this).attr("src");
    modal.find("img").attr("src", imageSrc);
    notslide();
    modal.show();
  });

  modal.on("click", function (event) {
    event.preventDefault();
    modal.hide();
    slide();
  });
});
