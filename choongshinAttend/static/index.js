var view_date;
var return_date;
function clock() {
  var target = document.getElementById("this-sunday");
  var time = new Date(target.innerText);
  var year = time.getFullYear();
  var month = time.getMonth()+1;
  var date = time.getDate();
  month = month >= 10 ? month : '0' + month; 
  date = date >= 10 ? date : '0' + date; 
  return_date = `${year}-${month}-${date}`;
  getDate();
}

// `${month}월 ${date}일 ${week[day]}요일 `;

function preclock() {
  var target = document.getElementById("this-sunday");
  var time = new Date(target.innerText);
  var prevDate = new Date(time.setDate(time.getDate() - 7));
  var year = prevDate.getFullYear();
  var month = prevDate.getMonth()+1;
  var date = prevDate.getDate();
  month = month >= 10 ? month : '0' + month; 
  date = date >= 10 ? date : '0' + date; 
  return_date = `${year}-${month}-${date}`;
  target.innerText = `${year}-${month}-${date}`;
  getDate();
}

function nextclock() {
  var target = document.getElementById("this-sunday");
  var time = new Date(target.innerText);
  var nextDate = new Date(time.setDate(time.getDate() + 7));
  var year = nextDate.getFullYear();
  var month = nextDate.getMonth()+1;
  var date = nextDate.getDate();
  month = month >= 10 ? month : '0' + month; 
  date = date >= 10 ? date : '0' + date; 
  return_date = `${year}-${month}-${date}`;
  target.innerText = `${year}-${month}-${date}`;
  getDate();
}

function getDate() {
  size = document.getElementsByName("attend_date").length;
  for (var i = 0; i < size; i++) {
    document.getElementsByName("attend_date")[i].value = return_date;
  }
}
function savealert() {
  alert("저장완료");
}

function mobilePushButton() {
  $('.mnb button').fadeOut();
  $('.mnb_inner').animate({marginRight: 0}, 1000);
}
function mobilePushExit() {
  $('.mnb button').fadeIn();
  $('.mnb_inner').animate({marginRight: '-60%'}, 1000);
}

setTimeout(function () {
  clock();
}, 100);

