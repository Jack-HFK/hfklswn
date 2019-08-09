**CSS属性知识点总结**

```
background:lime;                                设置背景颜色
color:rgba(255,0,0,0);                          设置字体颜色
onclick                                         实现点击按钮在控制台输出
font-size:8px;                                  设置字体大小
font-style:italic;                              设置字体斜体
font-family:Arial,"黑体";                        设置字体名称
font-weight:normal;                             设置字体粗细程度 /normal（默认值）等价于400 /bold(加粗) 等价于700
font : style weight size family;                字体属性简写:font: 斜体 粗细 大小 名称
height:88px                                     设置高度
width:88px                                      设置宽度
min-height                                      设置最小高度
checked                                         设置为默认选中状态,按钮有选中和未选中两个状态,对应checked属性值为true/false
display:none;                                   设置为默认隐藏
display:block;                                  设置为显示内容
display:inline-block;                           元素类型转换
box-shadow:offsetX offsetY blur (spread) color; 设置盒阴影
border:width style color;                       边框实现：填写边框的边框宽度,边框样式,边框颜色
border-top:8px solid blue;                      设置上边框：边框宽度,实线边框,边框颜色
border-right:8px solid rgba(0,0,0,0);           设置右边框：边框宽度,实线边框,边框颜色
border-bottom:8px solid green;                  设置下边框：边框宽度,实线边框,边框颜色
border-left:8px solid lime;                     设置左边框：边框宽度,实线边框,边框颜色
border-radius:像素值/百分比                       设置圆角边框
box-sizing:border-box;                          调整盒模型的计算方式，取值border-box时，表示当前元素指定的width/height是包含边框在内区域的尺寸
transition:8s;                                  添加过渡属性：在属性两种元素状态切换时添加平滑过渡效果
text-decoration:none;                           取消超链接默认下划线
元素:hover;                                     设置元素鼠标悬停时的属性
outline:none;                                   取消表单控件在焦点状态下的轮廓线,取none可以取消文本输入框默认轮廓线
outline:width style color;                      设置轮廓线：填写边框的边框宽度,边框样式,边框颜色
padding:像素;                                    设置内边距:调整元素内容框与边框之间的距离
margin：像素;                                    设置外边距：调整元素与元素之间的距离
vertical-align:top;                             水平方向上元素之间的垂直对齐方式：top(上)/middle(中)/bottom(下)
float:left/right;                               浮动布局:设置元素向左浮动或向右浮动
list-style:none;                                去除列表项目符号(默认样式)
overflow:auto;                                  处理内容溢出：内容超出元素的尺寸范围:auto自动在溢出方向添加可用滚动条
overflow:hidden;                                父元素设置overflow:hidden;解决子元素全部设置浮动,导致父元素高度为0,影响父元素背景色和背景图片展示,影响页面布局
clear:/left/right/both;                         清除浮动:使文档中正常元素不受前面浮动元素的影响：/左浮影响/右浮动影响/整体浮动影响
cursor:default;                                 设置鼠标显示形状 default箭头/pointer手指/text形状I
position:relative/absolute/fixed;               定位布局:可取relative（相对定位）/absolute（绝对定位）/fixed（固定定位）,设置偏移属性
z-index:数字随意;                                调整堆叠次序：元素发生堆叠时可以使用 z-index 属性调整已定位元素的显示位置，值越大元素越靠上,只有定位元素才能够使用z-index属性调整次序
父元素>子元素:first-child;                        父元素下第一个出现的子元素
background-color: 颜色;                          设置背景颜色
background-image : url("路径");                  设置背景图片
background-position:x y;                         设置背景图片的显示位置
background-size:width height;                    设置背景图片的尺寸
text-decoration:none;                            文本装饰线:取值: none:取消装饰线/underline:下划线/overline:上划线/line-through:删除线/
text-align:center;                               文本内容的水平对齐方式:left(默认值):左对齐/center:居中对齐/right:右对齐/justify:两端对齐
line-height:像素;                                 设置行高位置：文本垂直居中
className
readonly                                         限制用户在输入框能不能输入内容
```

**CSS元素知识点总结**

```
<hr>                                水平线标签:在页面中插入一条水平分割线
<br>                                格式标签:换行标签
<i></i>                             斜体标签
<b></b>                             加粗标签
<p></p>                             段落标签
<u></u>                             删除线标签
<h1></h1>                           标题标签:自带加粗效果,从h1到h6字体大小逐级递减
<div></div>                         容器标签:常用于页面结构划分，结合CSS实现网页布局
<span></span>                       行分区标签:用于对特殊文本特殊处理
<a href="锚点跳转"></a>              超链接：通过点击跳转到指定的目标文件 href=""javascript:void(0)
<strong></strong>                   强调标签:效果同b标签
<img src="" alt="">                 图片标签:用于在网页中插入一张图片
<label for="地址"></label>          普通文本标签：常与表单控件结合实现文本与控件的绑定
<table></table>                     表格标签
<tr></tr>                           表格行标签
<th></th>                           表示单元格:自带文本加粗和居中效果
<td></td>                           普通单元格
<ol></ol>                           有序列表:默认使用阿拉伯数字标识每条数据,可添加type属性设置项目符号
<ul></ul>                           无序列表:默认使用实心圆点标识列表项,可添加type属性设置项目符号
<form action="数据提交地址"></form>   表单标签:表单用于采集用户的信息并提交给服务器，由表单元素和表单控件组
<input type="text">                  checkbox复选按钮 radio单选按钮 text文本输入
<input type="radio">                checkbox复选按钮 radio单选按钮 text文本输入
<input type="checkbox">             checkbox复选按钮 radio单选按钮 text文本输入
<input type="text" placeholder="输入框内添加提示文本内容提示">
<button></button>                   表示按钮，标签内容即为按钮显示文本,书写在form中，相当于submit提交按钮
<style></style>                     借助于style标签，在HTML文档中嵌入CSS样式代码,为当前的元素添加样式声明
<link rel="stylesheet" href="URL">  引入外部样式表
```