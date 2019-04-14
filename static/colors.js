var flag = true;  window.setInterval(function () {    var color = flag ? 'ffffcc' : 'ffff99';    document.getElementsByTagName('body')[0].style.backgroundColor = color;    flag = !flag;  }, 1000)
