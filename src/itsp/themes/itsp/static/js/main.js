$('[data-btnMenuShow]').click(function () {
    $('[data-mobMenu]').addClass('header__menu_open');
    $('body').addClass('menu-open');
});

$('[data-btnMenuHide]').click(function () {
    $('[data-mobMenu]').removeClass('header__menu_open');
    $('body').removeClass('menu-open');
});

$(window).on('scroll', function () {
    var $this = $(this),
        $nav = $('[data-nav]');
    if ($this.scrollTop() > 0) {
        $nav.addClass('header__nav_scrolled');
    } else {
        $nav.removeClass('header__nav_scrolled');
    }
});

// https://github.com/cferdinandi/smooth-scroll
var scroll = new SmoothScroll('[data-scroll]', {
    header: '.header__nav',
    offset: 20
});

var mymap = L.map('map',{
    dragging: !L.Browser.mobile,
    tap: !L.Browser.mobile
}).setView([46.980062, 28.889553], 13);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    maxZoom: 18,
    id: 'madmak/ckab261sj4z921iph3a9clki9',
    tileSize: 512,
    zoomOffset: -1,
    accessToken: maptoken
}).addTo(mymap);

var mapIcon = L.icon({
    iconUrl: siteurl + '/theme/images/map-marker.svg',
    iconSize: [60, 60]
});

var marker = L.marker([46.980062, 28.889553], {icon: mapIcon}).addTo(mymap);
