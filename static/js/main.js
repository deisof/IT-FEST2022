$(function() {
    $('.works-carousel').owlCarousel({
        loop:true,
        margin:30,
        nav:true,
        dots: false,
        navText: ['<img src="/static/img/arrow_left.svg">', '<img src="/static/img/arrow_right.svg">'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:2
            }
        }
    });

    $('ul.tabs__caption').on('click', 'li:not(.active)', function(e) {
        e.preventDefault();
        $(this)
        .addClass('active').siblings().removeClass('active')
        .closest('section.tabs').find('div.tabs__content').removeClass('active').eq($(this).index()).addClass('active');
    });

    $('.contributer-carousel').owlCarousel({
        loop:true,
        margin:0,
        nav:true,
        dots: false,
        navText: ['<img src="/static/img/arrow_left.svg">', '<img src="/static/img/arrow_right.svg">'],
        responsive:{
            0:{
                items:1
            },
            600:{
                items:1
            },
            1000:{
                items:1
            }
        }
    });
});

$(window).load(function(){
    if(window.location.hash){
      $('a[href="'+window.location.hash+'"]').trigger('click');
    }
  });
  
  $(document).on('click', 'a[data-toggle="tab"]', function(){
    window.location.hash = $(this).attr('href');
  })

