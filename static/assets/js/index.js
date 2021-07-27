document.addEventListener('keydown', function (event) {
    if (event.key === 'd') {
      $.ajax({
        type: "GET",
        url: "classify",
        data: {label_selected = label_selected, img_hash = img_hash},
        type: "json"

      });
    }
    else if (event.key === 'D') {
        $.ajax({
            type: "GET",
            url: "classify",
            data: {label_selected = label_selected, img_hash = img_hash},
            type: "json"
    
          });
    }
    else if (event.key === 'a') {
        $.ajax({
          type: "GET",
          url: "classify",
          data: {label_selected = label_selected, img_hash = img_hash},
          type: "json"
  
        });
    }
    else if (event.key === 'A') {
        $.ajax({
            type: "GET",
            url: "classify",
            data: {label_selected = label_selected, img_hash = img_hash},
            type: "json"
    
        });
    }
    else if (event.key === 37) {
        $.ajax({
          type: "GET",
          url: "classify",
          data: {label_selected = label_selected, img_hash = img_hash},
          type: "json"
  
        });
    }
    else if (event.key === 39) {
        $.ajax({
            type: "GET",
            url: "classify",
            data: {label_selected = label_selected, img_hash = img_hash},
            type: "json"
    
        });
    }
  });