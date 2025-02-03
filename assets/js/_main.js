/* ==========================================================================  
   jQuery plugin settings and other scripts  
   ========================================================================== */  

   $(document).ready(function(){  
    // These should be the same as the settings in _variables.scss  
    scssLarge = 925; // pixels  
  
    // Sticky footer  
    var bumpIt = function() {  
        $("body").css("margin-bottom", $(".page__footer").outerHeight(true));  
      },  
      didResize = false;  
  
    bumpIt();  
  
    $(window).resize(function() {  
      didResize = true;  
    });  
    setInterval(function() {  
      if (didResize) {  
        didResize = false;  
        bumpIt();  
      }  
    }, 250);  
  
    // FitVids init  
    fitvids();  
  
    // Follow menu drop down  
    $(".author__urls-wrapper button").on("click", function() {  
      $(".author__urls").fadeToggle("fast", function() {});  
      $(".author__urls-wrapper button").toggleClass("open");  
    });  
  
    // Restore the follow menu if toggled on a window resize  
    $(window).on('resize', function() {  
      if ($('.author__urls.social-icons').css('display') == 'none' && $(window).width() >= scssLarge) {  
        $(".author__urls").css('display', 'block');  
      }  
    });      
  
    // init smooth scroll, this needs to be slightly more than then fixed masthead height  
    $("a").smoothScroll({offset: -65});  
  
    // add lightbox class to all image links  
    $("a[href$='.jpg'],a[href$='.jpeg'],a[href$='.JPG'],a[href$='.png'],a[href$='.gif']").addClass("image-popup");  
  
    // Magnific-Popup options  
    $(".image-popup").magnificPopup({  
      type: 'image',  
      tLoading: 'Loading image #%curr%...',  
      gallery: {  
        enabled: true,  
        navigateByImgClick: true,  
        preload: [0,1] // Will preload 0 - before current, and 1 after the current image  
      },  
      image: {  
        tError: '<a href="%url%">Image #%curr%</a> could not be loaded.',  
      },  
      removalDelay: 500, // Delay in milliseconds before popup is removed  
      mainClass: 'mfp-zoom-in',  
      callbacks: {  
        beforeOpen: function() {  
          this.st.image.markup = this.st.image.markup.replace('mfp-figure', 'mfp-figure mfp-with-anim');  
        }  
      },  
      closeOnContentClick: true,  
      midClick: true // allow opening popup on middle mouse click  
    });  
  
    // Function to open the citation modal with the correct content  
    window.openCitationModal = function(title, citation) {  
      $("#citation-title").text(title);  
      $("#citation-text").text(citation);  
      $("#citation-modal").fadeIn(200); // Use fadeIn instead of direct style change  
    };  
  
    // Function to close the modal  
    window.closeCitationModal = function() {  
      $("#citation-modal").fadeOut(200);  
    };  
  
    // Close modal if user clicks outside the modal content  
    $(window).click(function(event) {  
      if ($(event.target).is("#citation-modal")) {  
        closeCitationModal();  
      }  
    });  
  });  
  