$(function (){
    //1.保存图片路径
    var list = ["index_banner1.jpg","index_banner2.jpg","index_banner3.jpg","index_banner4.jpg","index_banner5.jpg"];
    //2.定义索引
    var index = 0;
    //3.开启定时器
    var timer = setInterval(autoPlay,1500);
    function autoPlay(){
        $("#banner li").eq(index).css("background","gray");
        //更新索引
        index = ++index==list.length? 0 : index;
        //切换图片路径
        $("#banner img").attr("src",list[index]);
        //切换图片索引的样式(圆圈)
        $("#banner li").eq(index).css("background","red");

    }
    //鼠标移入移出
    $("#banner").mouseover(function (){
        clearInterval(timer);
    }).mouseout(function (){
        //重启定时器
        timer = setInterval(autoPlay,1500)
    })






})