SVGInject(document.querySelectorAll("img.injectable"));

$( document ).ready(function() {

  //Toggle sub menu on main nav
  $(".nav-drop").on("click", function(e) {
    e.preventDefault();
    if ($(this).parent().find(".sub-nav").is(":visible")) {
      $(this).find(".nav-inner-right svg").attr('transform', 'translate(0 0) rotate(360)');
      $(this).parent().find(".sub-nav").slideUp();
    } else {
      $(this).find(".nav-inner-right svg").attr('transform', 'translate(0 0) rotate(180)');
      $(this).parent().find(".sub-nav").slideDown();
    }
    // $(this).parent().find(".sub-nav").slideToggle();
  });

  $(".nav-select").on("click", function(e) {
    e.preventDefault();
    $(".help-menu-mobile nav").slideToggle();
  });

  //TogglecCollapsible widgets
  $(".collapse-widget-button").on("click", function(e) {
    e.preventDefault();

    if ($(this).parent().parent().parent().parent().parent().find(".collapse-widget").is(":visible")) {
      $(this).parent().parent().parent().parent().parent().find(".collapse-widget").slideUp();
      $(this).parent().parent().parent().parent().parent().find(".collapse-widget-svg").first().attr('transform', 'translate(10.6 14) rotate(360)');
    } else {
      $(this).parent().parent().parent().parent().parent().find(".collapse-widget").slideDown();
      $(this).parent().parent().parent().parent().parent().find(".collapse-widget-svg").first().attr('transform', 'translate(22 19) rotate(180)');
    }
  });

  $(document).on("click", "#Menu", function() {
    $(".main-nav-mobile-left").html('<svg id="mobile-close" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16"><path d="M8,6.609,14.609,0,16,1.391,9.392,8,16,14.609,14.609,16,8,9.392,1.391,16,0,14.609,6.609,8,0,1.391,1.391,0Z" fill="#fff"/></svg>');
    $(".main-nav").slideDown();
  });

  $(document).on("click", "#mobile-close", function() {
    $(".main-nav-mobile-left").html('<svg id="Menu" xmlns="http://www.w3.org/2000/svg" width="19.836" height="16.75" viewBox="0 0 19.836 16.75"><rect id="Rectangle_697" data-name="Rectangle 697" width="19.836" height="1.75" fill="#fff"/><rect id="Rectangle_698" data-name="Rectangle 698" width="19.836" height="1.75" transform="translate(0 7.5)" fill="#fff"/><rect id="Rectangle_699" data-name="Rectangle 699" width="19.836" height="1.75" transform="translate(0 15)" fill="#fff"/></svg>');
    $(".main-nav").slideUp();
  });

  const FloatLabel = (() => {
  
    // add active class and placeholder 
    const handleFocus = (e) => {
      const target = e.target;
      target.parentNode.classList.add('active');
      target.setAttribute('placeholder', target.getAttribute('data-placeholder'));
    };
    
    // remove active class and placeholder
    const handleBlur = (e) => {
      const target = e.target;
      if(!target.value) {
        target.parentNode.classList.remove('active');
      }
      target.removeAttribute('placeholder');    
    };  
    
    // register events
    const bindEvents = (element) => {
      const floatField = element.querySelector('input');
      floatField.addEventListener('focus', handleFocus);
      floatField.addEventListener('blur', handleBlur);    
    };
    
    // get DOM elements
    const init = () => {
      const floatContainers = document.querySelectorAll('.float-container');
      
      floatContainers.forEach((element) => {
        if (element.querySelector('input').value) {
            element.classList.add('active');
        }      
        
        bindEvents(element);
      });
    };
    
    return {
      init: init
    };
  })();
  
  FloatLabel.init();
});