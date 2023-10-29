// // 最后执行,当页面加载完成(html\css\图片\视频等等)之后,触发的事件
//    window.onload = function(){
//        $('.c1').click(function(){
//            $(this).css({'background-color':'green'});
//        })
//    }

$(document).ready(function(){
    $('.c1').click(function(){
        $(this).css({'background-color':'green'});
    });
});