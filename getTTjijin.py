# -*- coding: utf-8 -*-
import sys
import urllib2

import datetime
import time
import json

def queryLocationJson(timestamp):
    # 该url参数可以调整, pageSize 为一次拉取的数量，pageIndex为第几页
    url = "http://api.fund.eastmoney.com/FundTradeRank/GetHbRankList?MinsgType=&IsSale=1&strSortCol=&orderType=&pageSize=1000&pageIndex=1&intCompany=&debug=1234567&callback=jQuery18303371837782715743_1563265207809&_={0}";
    url= url.format(str(timestamp));
    # print url;
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    return response.read();


def date2timestamp(date):
    timestamp = int(time.mktime(date.timetuple()))
    timestamp *= 1000
    return timestamp

if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding("utf-8")

    length = len(sys.argv)

    #本来准备来做历史数据查询，貌似不支持,就先这样子吧
    if (length >= 2):
        date = datetime.datetime.strptime(sys.argv[1], "%Y%m%d%")
    else:
        date = datetime.datetime.now()
    timestamp = date2timestamp(date)
    result = queryLocationJson(timestamp)

    #截取json数据，由于服务端返回是个jsonP的格式
    jsonStr = result.split('(')[1].split(')')[0];

    jsonobj = json.loads(jsonStr, encoding='utf-8');

    lists = jsonobj["Data"]

    print '基金代码,基金名称,7日年化,14日年化,28日年化,日期'
    for value in lists:
        print "{0},{1},{2}%,{3}%,{4}%,{5}".format(value["FCODE"],value["SHORTNAME"],value["LJJZ"],value["FTYI"], value["TEYI"], value["FSRQ"])


