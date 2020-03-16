$(document).ready(function() {
    let statement = new Glide('.statement');
    let elSlideWrapper = $('.glide-wrapper');
    let elPaginate = $('.glide-pagination');

    let sliderCount = elSlideWrapper[0].childElementCount;
    elPaginate.html((statement.index+1) + "/" + sliderCount);
    statement.on('run', function() {
        elPaginate.html((statement.index+1) + "/" + sliderCount);
    });
    

    statement.mount();
});