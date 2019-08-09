$(function(){
    //1.保存图片路径
    var list = ["index_banner1.jpg","index_banner2.jpg","index_banner3.jpg","index_banner4.jpg","index_banner5.jpg"];
    //2.定义索引下标
    var index = 0;
    //3.setInterval开启定时器
    var timer = setInterval(autoPlay,1000);
    function autoPlay(){
        // 更新图片索引前，先更改圆点索引的颜色
        $("#banner li").eq(index).css("background","gray") //eq 匹配指定下标的元素
        //更新索引
        index = ++index == list.length? 0 : index;
        //切换图片路径
        $("#banner img").attr("src",list[index]);
        //切换图片索引的样式 更改圆点索引颜色
        $("#banner li").eq(index).css("background","red")
    }
    //鼠标的移入和移出
    $("#banner").mouseover(function(){
        //鼠标移入时 ，clearInterval关闭指定id对应的定时器
        clearInterval(timer);
    }).mouseout(function(){
        //鼠标移出时，重启原来定时器
        timer = setInterval(autoPlay,1000)
    })
    //点击左右超链接切图
    $(".prev").click(function(){  //鼠标点击事件设置
        //切换图片索引的样式 更改之前切换前圆点索引颜色
        $("#banner li").eq(index).css("background","gray") //eq 匹配指定下标的元素
        //更新索引
        index = --index <0?list.length-1:index
        //切换图片路径
        $("#banner img").attr("src",list[index]);
        //切换图片索引的样式 更改圆点索引颜色
        $("#banner li").eq(index).css("background","red")
    })
    $(".next").click(function(){
         //切换图片索引的样式 更改之前切换前圆点索引颜色
        $("#banner li").eq(index).css("background","gray") //eq 匹配指定下标的元素
        //更新索引
        index = ++index == list.length? 0 : index;
        //切换图片路径
        $("#banner img").attr("src",list[index]);
        //切换图片索引的样式 更改圆点索引颜色
        $("#banner li").eq(index).css("background","red")




    })





})