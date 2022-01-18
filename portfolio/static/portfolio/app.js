// using gsap timeline to animate the sliders when website first loads
const tl = gsap.timeline({defaults: {ease: "power1.out"}})

tl.to('.text', {y: "0%", duration: 1, stagger: 0.35})
tl.to('.slider', {y: "-100%", duration: 1.5, delay: 0.5})
tl.to('.intro', {y : "-100%", duration: 1}, "-=1.2")
tl.fromTo('.wrapper', {opacity: 0}, {opacity: 1, duration: 1})
tl.fromTo('.hero-text', {opacity: 0}, {opacity: 1, duration: 1}, "-=1")
tl.fromTo('.social-media', {opacity: 0}, {opacity: 1, duration: 1}, "-=1")

// jQuery to create nav transition when scrolled to the bottom of the hero landing page
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

// javascript to create onclick functions for the nav menu when screen size becomes small
let navbar = document.querySelector('.navbar');
let wrapper = document.querySelector('.wrapper');

document.querySelector('#menu-btn').onclick = () =>{
    navbar.classList.toggle('active');
    wrapper.classList.toggle('active');
    document.querySelector('#menu-btn').classList.toggle('clicked')
}
document.querySelector('.nav-links').onclick = () =>{
    navbar.classList.toggle('active', false);
    wrapper.classList.toggle('active', false);
    document.querySelector('#menu-btn').classList.toggle('clicked', false)

}
