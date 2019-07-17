##运行方式
* 如果使用解释的方式，直接打开脚本运行即可
* unix相关系统可以直接运行脚本，输出到结果文件result.csv,如下执行方式

```
python getTTjijin.py >> result.csv

```



## 依赖环境python解释器
* https://www.python.org/downloads/  官网即可下载
* 本代码还使用的是python2.7版本的功能，
* 官网最新版本是3.7.4，可尝试使用最新版本进行运行


## 依赖功能点
* 网页数据分析，开发者工具，network里可以抓取到数据相关请求包
* 伪造浏览器请求，抓取网页数据，主要是http协议，需要使用http相关功能包，python自带
* 网页结果数据是个jsonP的结果需要获取里面的执行数据，字符串处理工具
* 数据结果是一个json，将json转换成对象，输出csv格式，json格式和处理，python自带