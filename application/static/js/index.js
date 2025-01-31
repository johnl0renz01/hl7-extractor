// ON LOAD

window.addEventListener('load', function() {
  isToggled = window.sessionStorage.getItem("TOGGLE_FORM")

  if (isToggled) {
    document.getElementById("form").style.display = 'none'
    document.getElementById("toggle").textContent = 'Show Form'
  } else {
    document.getElementById("form").style.display = 'block'
    document.getElementById("toggle").textContent = 'Hide Form'
  }

  window.sessionStorage.removeItem("INDEX_LINK")

  document.getElementById("filterby_placeholder").disabled = true;
  changeFilterDisplay()
  document.getElementById("json_container").style.display = "none"
})

function toggleForm() {
  isToggled = window.sessionStorage.getItem("TOGGLE_FORM")

  if (isToggled) {
    window.sessionStorage.removeItem("TOGGLE_FORM")
    document.getElementById("form").style.display = 'block'
    document.getElementById("toggle").textContent = 'Hide Form'
  } else {
    window.sessionStorage.setItem("TOGGLE_FORM", true)
    document.getElementById("form").style.display = 'none'
    document.getElementById("toggle").textContent = 'Show Form'
  }
}


//Persist scroll position
document.addEventListener("DOMContentLoaded", function(event) { 
  var scrollpos = sessionStorage.getItem('scrollpos');
  if (scrollpos) window.scrollTo(0, scrollpos);
});

window.onbeforeunload = function(e) {
  sessionStorage.setItem('scrollpos', window.scrollY);
};


function confirmDelete(e){
  if(!confirm('Do you really want to delete HL7 message ID #' + e.target.id + "?")) {
    e.preventDefault();
  }
}

function sortDate(e) {
  searchQuery("order", e)
}

function navigatePage(e) {
  searchQuery("page", e)
}


// SEARCH

function searchQuery(key, e) {
  queryString = window.location.search
  let params = new URLSearchParams(queryString);

  // Convert it to plain object
  let paramsObject = {};
  params.forEach((value, key) => {
      paramsObject[key] = value;
  });
  
  if (key == "page"){
    paramsObject[key] = e
  } else {
    paramsObject[key] = e.target.value
  }

  queryString = '?'

  Object.entries(paramsObject).map(entry => {
    let key = entry[0];
    let value = entry[1];
    queryString = queryString + key + "=" + value + "&"
  });

  queryString = queryString.substring(0, queryString.length-1)

  win_href = window.location.href.split("?")[0]
  win_href = win_href.replace("#", "")
  link = win_href + queryString
  
  window.location.replace(link);
}

// FILTER

function resetFilter() {
  window.sessionStorage.removeItem("FILTER_BY")
}

function changeFilter(e) {
  val = e.target.value

  changeFilterDisplay(val)
}

function changeFilterDisplay(val=null) {
  if (!val) {
    val = window.sessionStorage.getItem("FILTER_BY")
  }
  document.getElementById("filterBy").value = val

  hideAll();
  
  if (val == "year") {
    document.getElementById("year").style.display = "block"
  } else if (val == "month") {
    document.getElementById("month").style.display = "block"
  } else if (val == "day") {
    document.getElementById("day").style.display = "block"
  }


  function hideAll() {
    document.getElementById("year").style.display = "none"
    document.getElementById("month").style.display = "none"
    document.getElementById("day").style.display = "none"
  }
}


function filterDay(e) {
  val = e.target.value
  window.sessionStorage.setItem("FILTER_BY", "day")
  document.getElementById("dayForm").submit();
}

function filterMonth(e) {
  val = e.target.value
  window.sessionStorage.setItem("FILTER_BY", "month")
  document.getElementById("monthForm").submit();
}

function filterYear(e) {
  val = e.target.value
  window.sessionStorage.setItem("FILTER_BY", "year")
  document.getElementById("yearForm").submit();
}


// URL

function setLinkURL() {
  window.sessionStorage.setItem("HOME_LINK", window.location.href)
}

function homePage(){
  link =  window.sessionStorage.getItem("HOME_LINK")
  if (link !== null) {
    window.location.replace(link);
  }
}


// JSON

function toggleJSON() {
  currentState = document.getElementById('json_button').name

  if (currentState == 'show') {
    document.getElementById('json_button').name = 'hide';
    document.getElementById('json_button').textContent = 'Hide JSON';
    document.getElementById("json_container").style.display = "inline-block"
  } else {
    document.getElementById('json_button').name = 'show';
    document.getElementById('json_button').textContent = 'Show JSON';
    document.getElementById("json_container").style.display = "none"
  }
  
}

function analyzeData() {
  document.getElementById('analysis').style.position = "relative";
  document.getElementById('analysis').style.top = 0;
}
