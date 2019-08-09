/*封装判断浏览器的支持性*/
function createXhr(){
    if(window.XMLHttpRequest){
        var xhr = new XMLHttpRequest; //<---------创建支持XHR的异步对象
    }else{
        var xhr = new ActiveXObject("Microsoft.XMLHTTP"); //<-----------创建支持AxO的异步对象
    }
    return xhr;
}