// using gsap to animate the sliders
const tl = gsap.timeline({defaults: {ease: "power1.out"}})

tl.to('.text', {y: "0%", duration: 1, stagger: 0.35})
tl.to('.slider', {y: "-100%", duration: 1.5, delay: 0.5})
tl.to('.intro', {y : "-100%", duration: 1}, "-=1.2")
tl.fromTo('.wrapper', {opacity: 0}, {opacity: 1, duration: 1})
tl.fromTo('.hero-text', {opacity: 0}, {opacity: 1, duration: 1}, "-=1")

$(function(){
    $(document).scroll(function(){
        var $nav = $(".wrapper");
        var $icons = $(".icons");
        var $logos = $(".icon");
        var $logo = $(".logo");
        var $resume = $(".resume");
        var $head = $(".hero-image");

        $nav.toggleClass('scrolled', $(this).scrollTop() >= ($head.height()-75));
        $logos.toggleClass('scrolled', $(this).scrollTop() >= ($head.height()-75));
        $logo.toggleClass('scrolled', $(this).scrollTop() >= ($head.height()-75));
        $icons.toggleClass('scrolled', $(this).scrollTop() >= ($head.height()-75));
        $resume.toggleClass('scrolled', $(this).scrollTop() >= ($head.height()-75));
    });
});