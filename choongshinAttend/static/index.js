
function clock() {
    var target = document.getElementById("this-sunday");
    var time = new Date();
    var sunday = new Date(time.setDate(time.getDate() - time.getDay()));
    
    var month = sunday.getMonth();
    var date = sunday.getDate();
    var day = sunday.getDay();
    var week = ['일', '월', '화', '수', '목', '금', '토'];
    target.innerText = 
    `${month+1}월 ${date}일 ${week[day]}요일 `
}
setTimeout(function() {
    clock();
  }, 500);
// target.innerText = clock();