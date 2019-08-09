$(function(){
    //1.全选和取消全选
    var isChecked = false; //标记全选元素
    $(".checkAll").click(function(){ //:checked表示按钮的选中状态
        isChecked = !isChecked;
        if(isChecked){  //属性读取为true显示选中图片
            //类标签.checkAll修改显示图片
            $(".checkAll").attr("src","../images/cart/product_true.png")
            //类标签.checkItem修改商品按钮的显示图片
            $(".checkItem").attr("src","../images/cart/product_true.png")
            .attr("checked",true)
        }else{ //属性读取为false显示未选中图片
            $(".checkAll").attr("src","../images/cart/product_normal.png")
            $(".checkItem").attr("src","../images/cart/product_normal.png")
            .attr("checked",false)
        }
        sum()   //调用总数量和总价格计算函数，计算数量和总价格的变化
        /*$(this).prop("checked") //prop设置或读取click点击事件的选中属性
        //自定义标签属性   //prop设置或读取标签属性 //attr设置或读取标签属性
        $(this).prop("a","b").attr("aa","bb")*/
    })
    //2.反选  //:checked表示按钮的选中状态
    $(".checkItem").click(function(){
        if($(this).attr("checked")){ //单个商品：属性读取为true显示选中图片，并且设置为false传递给全选标签
            //移除标记  //attr设置或读取标签属性
            $(this).attr("checked",false)   //设置为false传递给全选标签
            .attr("src","../images/cart/product_normal.png");
        }else{  //单个商品：属性读取为false显示未选中图片
            $(this).attr("checked",true)    //设置为true传递给全选标签
            .attr("src","../images/cart/product_true.png");
        }
    //2.2反选
    //获取被选中的商品数量==列表长度
    var len = $(".checkItem[checked=checked]").length
    if(len ==$(".checkItem").length ){
        //全选
        $(".checkAll").attr("src","../images/cart/product_true.png")
        isChecked = true;  //设置全选显示选择图片未全选图片
    }else{
        $(".checkAll").attr("src","../images/cart/product_normal.png")
        isChecked = false;  //设置全选显示选择图片为未全选图片
    }
    sum()   //调用总数量和总价格计算函数，计算数量和总价格的变化
    })

    //3.数量增加
    $(".add").click(function(){
        //获取输入框的值
        //prev()返回前一个兄弟元素/返回前一个兄弟元素,要求满足选择器，必须是相邻的一个兄弟元素
        //val()设置或读取表单元素的值,等价于原生value属性
        var value = $(this).prev().val();//获取前一个兄弟元素的值
            value++;  //增加数量
        $(this).prev().val(value); //改变后的数量值重新写入标签值
        //价格联动  parent()返回父元素 html()设置或读取标签内容,等价于原生innerHTML,可识别标签语法
        //获取单价  parents()返回满足选择器的祖先元素 find()返回所有的后代元素(包含直接与间接)
        /*var s1 = $(this).parent().prev().find("p").html();
        var s2 = $(this).parents(".item").find(".price p").html();
        var price = s1.substring(1) //substring()根据指定的下标范围截取字符串
        var tolPrice = price * value;
        tolPrice = tolPrice.toFixed(2);
        //显示总金额
        $(this).parents(".item").find(".sum").html("￥"+tolPrice);*/
        changeSum($(this),value) //函数调用 把.sum标签的总金额重新设置
        sum() //调用总数量和总价格计算函数，计算数量和总价格的变化
    })


    //数量减少
    $(".minus").click(function(){
    //next()返回下一个兄弟元素/返回下一个兄弟元素,必须满足选择器,必须是相邻的一个兄弟元素。
    //val()设置或读取表单元素的值,等价于原生value属性
        var value = $(this).next().val(); //获取下一个兄弟元素的值
        if(value > 1){
            value--;    //减少数量
        }
        $(this).next().val(value) //改变后数量的值重新写入标签值
        changeSum($(this),value) //函数调用 把.sum标签的总金额重新设置
        sum() //调用总数量和总价格计算函数，计算数量和总价格的变化
    })



    //4.价格联动 封装价格计算函数,调用函数
    function changeSum(that,n){
        //价格联动  parent()返回父元素 html()设置或读取标签内容,等价于原生innerHTML,可识别标签语法
        //获取单价  parents()返回满足选择器的祖先元素 find()返回所有的后代元素(包含直接与间接)
        var s1 = $(that).parent().prev().find("p").html();
        //var s2 = $(that).parents(".item").find(".price p").html();
        var price = s1.substring(1) //substring()根据指定的下标范围截取字符串
        var tolPrice = price * n;
        tolPrice = tolPrice.toFixed(2); //保留两位小数
        //显示总金额 把.sum标签的总金额重新设置
        $(that).parents(".item").find(".sum").html("￥"+tolPrice);
    }
    //5.移除商品
    $(".item .action").click(function(){
        $(this).parent().remove();
        sum()
    })

    //6.获取总数量和总价格
    function sum(){
    var num = 0; //总数量
    var price = 0; //总价格
        //获取被选中商品的总数量和总金额进行累加
        //查找.checkItem[checked=checked]被选中的商品 each遍历函数
        $(".checkItem[checked=checked]").each(function(){
            numbers = $(this).parents(".item").find(".count input").val(); //选中的数量值
            num += Number(numbers);  //累加数量值
            var str = $(this).parents(".item").find(".sum").html() //选择商品的价格
            var s = Number(str.substring(1));   //转换数字类型
            price += s; //累加金额
        })
        //修改显示
        $(".total_count").html(num); //修改总商品数量
        price = price.toFixed(2)    // 金额保留两位小数
        $(".total_price").html(price+"元"); //修改商品总金额
    }

















})