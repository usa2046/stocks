import requests
import openpyxl
# 创建工作薄
wb=openpyxl.Workbook()  
# 获取工作薄的活动表
sheet=wb.active 
# 工作表重命名
sheet.title='顶牛' 
sheet.append(['序号','股票代码','最新价','涨幅','换手率','量比','DDX','DDY','DDZ','5日','10日','连续','连增','成交量(万元)','BBD(万元)','单数比','买入','卖出','特大差','大单差','中单差','小单差','买入','卖出','买入','卖出','买入','卖出','通吃率1日','通吃率5日','通吃率10日','通吃率20日','主动率1日','主动率5日','主动率10日','流通盘(万股)'])

for x in range(1,187):
    url = "http://www.dingniu888.com/ddx/pm/ygetnewallddxpm.php?zf=0&ddx=0&ddy=0&page={}&pagenum=20&orderby=0&t=0.669614266060109&d=sz".format(x)
    res_data = requests.get(url)
    json_data = res_data.json()
    print(json_data)
    list_stock = json_data['data']
    for stock in list_stock:
        sheet.append(stock)
    print("已下载完第{}页的信息".format(x))
print("下载完毕")
wb.save('顶牛ddx数据.xlsx')