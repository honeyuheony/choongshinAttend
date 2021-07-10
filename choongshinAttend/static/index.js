var view_date;

function clock() {
  var target = document.getElementById("this-sunday");
  if (target.innerText != "-") {
    return;
  }
  var time = new Date();
  var sunday = new Date(time.setDate(time.getDate() - time.getDay()));
  view_date = sunday;
  var month = sunday.getMonth();
  var date = sunday.getDate();
  var day = sunday.getDay();
  var week = ["일", "월", "화", "수", "목", "금", "토"];

  target.innerText = `${month + 1}월 ${date}일 ${week[day]}요일 `;
}
setTimeout(function () {
  clock();
}, 500);
// target.innerText = clock();

function preclock() {
  var target = document.getElementById("this-sunday");
  var time = view_date;
  var prevDate = new Date(time.setDate(time.getDate() - time.getDay() - 7));

  var month = prevDate.getMonth();
  var date = prevDate.getDate();
  var day = prevDate.getDay();
  var week = ["일", "월", "화", "수", "목", "금", "토"];
  target.innerText = `${month + 1}월 ${date}일 ${week[day]}요일 `;
}

function nextclock() {
  var target = document.getElementById("this-sunday");
  var time = view_date;
  var nextDate = new Date(time.setDate(time.getDate() - time.getDay() + 7));

  var month = nextDate.getMonth();
  var date = nextDate.getDate();
  var day = nextDate.getDay();
  var week = ["일", "월", "화", "수", "목", "금", "토"];
  target.innerText = `${month + 1}월 ${date}일 ${week[day]}요일 `;
}
