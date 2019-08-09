//获取元素
function $(tag,index){ //变量声明未赋值默认为undefined
    if(index){
        elem = document.getElementsByTagName(tag,index);
    }else{
        //index=0或index=undefined
        elem = document.getElementsByTagName(tag)[0];
    }
    return elem;
}

