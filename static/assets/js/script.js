//Courtesy https://github.com/danfickle/

var myresize = function(idName, reqWidth, reqHeight) {
    var Width = reqWidth;
    var Height = reqHeight;
    var ratioW = window.innerWidth / Width;
    var ratioH = window.innerHeight / Height;

    var ratio = ratioW < ratioH ? ratioW : ratioH;
    var marginL = ((window.innerWidth - (ratio * Width)) / 2) * ratio;
    var marginT = ((window.innerHeight - (ratio * Height)) / 2) * ratio;

    var divs = document.querySelectorAll(idName);

    Array.prototype.forEach.call(divs, function(el, i) {
        console.log(el.id, i);
        el.style.transformOrigin = '0 0';
        el.style.transform = 'scale(' + ratio + ',' + ratio + ')';

        el.style.webkitTransformOrigin = '0 0';
        el.style.webkitTransform = 'scale(' + ratio + ',' + ratio + ')';

        el.style.left = marginL + 'px';
        if (idName != "#scaleDiv") {
            el.style.top = marginT + 'px';
        }
    });
}

function individualResize() {
    myresize("#background", 1440, 720);
    myresize("#scaleDiv", 1280, 600);
}

window.onresize = individualResize;
individualResize();

document.addEventListener('DOMContentLoaded', function() {
    individualResize();
});
