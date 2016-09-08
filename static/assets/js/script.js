//Courtesy https://github.com/danfickle/

var myresize = function() {
    var Width = 1280;
    var Height = 742;
    var ratioW = window.innerWidth / Width;
    var ratioH = window.innerHeight / Height;

    var ratio = ratioW < ratioH ? ratioW : ratioH;
    var marginL = ((window.innerWidth - (ratio * Width)) / 2) * ratio;
    var marginT = ((window.innerHeight - (ratio * Height)) / 2) * ratio;

    var divs = document.querySelectorAll('.my-center');

    Array.prototype.forEach.call(divs, function(el, i) {
        el.style.transformOrigin = '0 0';
        el.style.transform = 'scale(' + ratio + ',' + ratio + ')';

        el.style.left = marginL + 'px';
        el.style.top = marginT + 'px';

        el.style.webkitTransformOrigin = '0 0';
        el.style.webkitTransform = 'scale(' + ratio + ',' + ratio + ')';

    });
}

window.onresize = myresize;
myresize();

document.addEventListener('DOMContentLoaded', function() {
    myresize();
});
