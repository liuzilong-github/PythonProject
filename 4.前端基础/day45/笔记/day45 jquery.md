

# 今日内容



## js补充





### HTML的label标签补充

```
    <label >用户名: 
        <input type="text" name="username" id="username">
    </label>
    <label for="password">密码: </label>
    <input type="password" name="password" id="password">
```



bootcdn官网

https://www.bootcdn.cn/





## jQuery

###  jquery引入

```
外部网址引入
	<!--<script src="https://cdn.bootcss.com/jquery/3.4.1/jquery.js"></script>-->

本地文件引入
	<script src="jquery.js"></script>  //jquery.js本地文件路径

```



### jQuery初识

```
var d1 = $('#d1'); -- jquery对象  -- jQuery.fn.init [div#d1]
var d = document.getElementById('d1');  -- 原生dom对象 -- <div id='d1'></div>
jquery对象和dom对象之前不能调用互相的方法

jquery对象和dom对象可以互相转换
d1[0] -- dom对象   # 通过索引取值的方式
$(d) -- jquery对象  # $(原生DOM对象)
```



### 选择器

#### id选择器

```
$('#d1')  -- 同css

```

#### 类选择器

```
$('.c1') 
$(".c1").css({'color':'green'});
```

#### 元素选择器

```
$('标签名称') -- $('span')  

```

查看jquery对象找到的元素个数

```js
$("li").length;

```





#### 组合选择器

```css
$('#d1,.c2')
示例:
	html代码
		<div id="d1"></div>
        <div class="c2">
            这是c2
        </div>
    css代码:
        #d1,.c2{
            background-color: red;
            height: 100px;
            width: 100px;
            border-bottom: 1px solid black;
        }
  
  jquery代码:
  	$('#d1,.c2').css('background-color','green');
  	$('#d1,.c2')[1];  -- 索引为1的dom对象
  	$('#d1,.c2').eq(1); -- 索引为1 的jquery对象

```



#### 层级选择器

```
$("form input")
```



#### 属性选择器

```
html代码:
    <div class="c1" xx="oo">
        这是啥!
    </div>
css代码:
    [xx]{
    	color:red;
    }

input标签:  type='xx'   [type='xx']--对应的input标签
$('[xx]').css('color','green');
$('[xx="oo"]').css('color','pink');

```

表单对象属性选择器

```
:checked  找到被选中的input标签
:selected  找被选中的select标签中的option标签
```



#### 表单选择器

```
$(":text") 
// $(":input") 找到所有input标签
// $(":password") 找到所有input且type=password的标签
// $(":radio") 找到所有input且type=radio的标签
// $(":checkbox") 找到所有input且type=checkbox的标签

html代码:
	<form action="">
        <input type="text" id="username">
        <input type="text" id="username2">
        <input type="password" id="pwd">

        <input type="submit">
    </form>
jquery代码:找到所有的type=text的input标签
	$(':text');

```



#### 筛选器方法

```
html代码
    <ul>

        <li>谢一峰</li>
        <li class="c1">王子宇</li>
        <li>孙波</li>
        <li class="c2">石淦</li>
        <li>
            <span>白雪冰</span>
        </li>
        <li>方伯仁</li>

    </ul>

```

##### parent()

```
var c = $('.c1');
c.parent();
c.parents();  直系的祖先辈
c.parentsUntil('body');  往上找,直到找到body标签为止,不包含body标签
```

##### children()

```
var u = $('ul');
u.children();  找到所有儿子标签
u.children('.c1'); 找到符合.c1选择器的儿子标签
```

##### next() 

```
var c = $('.c1');
c.next();
nextAll();  下面所有兄弟
c.nextUntil('.c2');  下面到某个兄弟为止,不包含那个兄弟
```

##### prev()

```
var c = $('.c1');
c.prev();
c.prevAll(); 上面所有兄弟,注意顺序都是反的
c.prevUntil('.c1'); 上面到某个兄弟为止,不包含那个兄弟,注意顺序都是反的
```

##### siblings()

```
c.siblings();  找到不包含自己的所有兄弟
c.siblings('.c1');  筛选兄弟中有class类值为c1的标签
```

##### find() 找后代

```
$('li').find('span'); 等同于css的 li span选择器
```

##### first()和last() 和eq(索引值)

```
$('li').first();  找所有li标签中的第一个
$('li').last(); 找所有li标签中的最后一个
$('li').eq(0);  按照索引取对应的那个标签,索引从0开始
$('li').eq(-1);  最后一个
 
```



### 文本操作

### text()  和 html() 

 同js的innerText和innerHTML

```
取文本:
	c.text();  不带标签
	c.html();  带标签
设置文本:
	c.text('文本');
	c.html('文本'); -- 文本--"<a href=''>皇家赌场</a>"
```



### class类值操作

```

html代码
	<div class="c1">
    
	</div>
css代码:
	   .c1{
            background-color: red;
            height: 100px;
            width: 100px;
        }
        .c2{
            background-color: green;
        }
jquery
$('div').addClass('c2');
$('div').removeClass('c2');
$('div').toggleClass('c2');
示例:
	var t = setInterval("$('div').toggleClass('c2');",500);
```

### val值操作

```
示例:
html代码:

    <input type="text" id="username">
    <input type="radio" class="a1" name="sex" value="1">男
    <input type="radio" class="a1" name="sex" value="2">女
    <input type="checkbox" class="a2" name="hobby" value="1">抽烟
    <input type="checkbox" class="a2" name="hobby" value="2">喝酒
    <input type="checkbox" class="a2" name="hobby" value="3">烫头
    <select name="city" id="s1">
     <option value="1">北京</option>
     <option value="2">上海</option>
     <option value="3">深圳</option>
    </select>
    <select name="lover" id="s2" multiple>
     <option value="1">波多</option>
     <option value="2">苍井</option>
     <option value="3">小泽</option>
    </select>

jquery代码:
	
```

```
获取值：
 文本输人框：$('#username').val();
 单选radio框：$('.a1:checked').val();
 多选checkout框：$('.a2:checked').val()是不行的;需要循环取值，如下：
 var d = $(':checkbox:checked');
 for (var i=0;i<d.length;i++){
 console.log(d.eq(i).val());
 }
 单选select框：$('#city').val()；
 多选select框：$('#lover').val();
```

```
设置值：
 文本输入框：$('#username').val('you are my love');
 单选radio框：$('.a1').val([2]); #注意内容必须是列表，写的是value属性对应的值
 多选checkout框：$('.a2').val(['2','3'])
 单选select框：$('#city').val(['1'])；
 多选select框：$('#lover').val(['2','3'])
```

点击事件绑定

```
    $('.c1').click(function () {
        //$(this)表示的就是它自己
        $(this).css('background-color','green');
        // $('.c1').css('background-color','green');
    })
```





## jquery选择器补充

```css
:checked  找到被选中的input标签
:selected  找被选中的select标签中的option标签
:disabled  不可操作的标签 
:enabled   可操作的标签
示例:
	html代码:
		用户名:<input type="text" id="username" disabled>
		密码: <input type="text" id="password">
	jquery代码:
		$(':enabled');  
		$(':disabled');

```



模态对话框





## 创建标签

```js
添加标签:  $('.c1').html('<a href="http://www.baidu.com">百度</a>'); 但是这个属于替换内容,将标签内原来的内容全部替换掉.

js
	var a = document.createElement('a');
	
jquery:
	$('<a>',{
			text:'这还是个链接',
			href:'http://www.baidu.com',
			class:'link',
			id:'baidu',
			name:'baidu'
	})
```



## 文档操作

```
1 标签内部的后面插入内容 append
	html代码:
        <div class="c1">
            <h1>xx</h1>

        </div>
	方式1:
		1. var a = document.createElement('a'); 创建标签
		2. a.href = 'http://www.jd.com';  添加属性
		3. a.innerText = '京东'; 添加文本
		$('.c1').append(a);
	方式2: 常用
		$('.c1').append('<a href="http://www.baidu.com">百度</a>');
2 标签内部的上面插入内容 prepend
	$('.c1').prepend('<a href="http://www.baidu.com">百度</a>');
	$('.c1').prepend('<h1>亚洲</h1>');

3 标签外部的下面插入内容 after
	$('.c1').after('<h1>兄弟</h1>');
4 标签外部的上面插入内容 before
	$('.c1').before('<h1>兄弟</h1>');

简单示例:
	var s = $('<div>',{'class':'c2','text':'彭于晏'});
	$('.c1').after(s);
```



## empty清空标签

```
方式1:$('.c1').empty();
方式2:$('.c1').html(''); .text('')
```

## remove删除标签

```
$('.c1').remove();
```

## 字符占位符${变量名}

```
var username = '胜平';
var s = `我叫${username},我是个好人`;
```



增加和删除的示例



### 事件冒泡

点击儿子标签会触发父级标签\祖父标签..等等的所有点击事件,这叫事件冒泡

```js
html代码
    <div class="c1">
        <div class="c2"></div>
    </div>
css代码
	   .c1{
            border: 1px solid red;
            height: 100px;
        }
        .c2{
            border: 1px solid green;
            height: 50px;
            width: 50px;
        }

jquery代码
	$('.c1').click(function () {
        alert('父级标签c1');
    });
    $('.c2').click(function () {
        alert('儿子标签c2');
        return false; // 阻止后续事件发生
    });


```







### 事件委托

```
    // 事件委托
    $('tbody').on('click','.delete',function () {
        // $(this) 还是你点击的那个按钮标签
        $(this).parent().parent().remove(); // tr
        
    });
```



### prop属性操作

```
selected checked disabled enabled
设置属性
	$('#d1').prop('checked',true);    选中
	$('#d1').prop('checked',false);   取消选中
查看属性
	$('#d1').prop('checked'); true表示选中了,false表示未选中

```

attr方法

看代码





### 逻辑运算符

```
and  &&
or   ||
not  !
```







### 常用事件

focus和blur

```
html代码:

	<input type="text" id="username">
	<div class="c1"></div>

css代码:
	    .c1{
            background-color: red;
            height: 200px;
            width: 200px;
        }
        .c2{
            background-color: green;
        }

    // focus获取光标时触发的事件
    $('#username').focus(function () {
        $(this).css({'background-color':'yellow'});
        $('.c1').addClass('c2');

    });
    // blur失去光标时触发的事件
    $('#username').blur(function () {
        $(this).css({'background-color':'white'});
        $('.c1').removeClass('c2');

    });

```



change

域内容发生变化时触发的事件

```
$('select').change(function () {
        // $('.c1').toggleClass('c2');
        // console.log($(this));
        // console.log($(this).options);
        // console.log($(this).selectedIndex)
        // console.log(this);  //dom对象  $(this)jquery对象
        // console.log(this.options);
        // console.log(this.selectedIndex);
        var option_text = this.options[this.selectedIndex].innerText;
        console.log(option_text);
        // if (option_text === '喝酒'){}
	// 获取被选中的option标签的文本内容
	// $(':selected').text();
    });

```



hover 

鼠标悬浮事件

```
示例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            background-color: red;
            height: 200px;
            width: 200px;
        }
    </style>
</head>
<body>

<div class="c1"></div>


</body>
<script src="jquery.js"></script>
<script>
    $('.c1').hover(
        // 鼠标进入时触发的事件
        function(){
            $('.c1').css({'background-color':'yellow'});
        },
        // 鼠标移出时触发的事件
        function(){
            $('.c1').css({'background-color':'blue'});
        }
    )


</script>
</html>

```



绑定事件的两个方式

```
$('.c1').click(function(){})
$('.c1').on('click',function(){})

事件委托
$('.c1').on('click','子辈的标签选择器',function(){})

```



input

看代码



页面载入

看代码



作业：

添加和删除和编辑操作

![1605684112034](assets/1605684112034.png)





















































































2 jquery选择器



3 文本操作



4 样式操作

















































