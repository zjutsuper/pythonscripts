##运行方式
```
python getTTjijin.py >> result.csv

```



## 依赖环境python解释器
* https://www.python.org/downloads/  官网即可下载
* 本代码还使用的是python2.7版本的功能，
* 官网最新版本是3.7.4，可尝试使用最新版本进行运行


## 依赖功能点
* 抓取网页数据，http协议，需要使用http相关功能包
* 网页结果数据是个jsonP的结果需要获取里面的执行数据
* 数据结果是一个json，将json转换成对象，输出csv格式