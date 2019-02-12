function toggle_display(cls){
  el = document.querySelector(cls);

  if(el.style.display == 'none'){
      el.style.display = 'block'
  }else{
     el.style.display = 'none'
  }
}

// <button onclick="toggle_display()">Toggle display</button>
//
// <div class="content_section">See me no more</div>
