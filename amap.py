import requests
import json
import xlwt

# 设置Poi搜索的各项参数
amap_api_key = ''  # 输入自己的key
poi_search_url = 'https://restapi.amap.com/v3/place/around?'
location = '121.459126,31.162659'
radius = '1500'
types = '120000'

# 设置爬虫网络链接测试链接
test_url = 'https://www.baidu.com'

# 设置文件输出名
place = '云景路'
output_type = '商务住宅'
file_name = place + output_type + '.xls'

# 创建表格
workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Sheet 1')

# 获取数据并保存数据
page = 1
while page <=100:
    k = 0
    req_url = poi_search_url + 'key=' + str(amap_api_key) + '&location=' + str(location) + '&radius=' + str(radius) + '&types=' + str(types) + '&page=' + str(page)
    while k<= 19:
        try:
            line = (page - 1) * 20 + k
            result = requests.get(req_url)
            result.raise_for_status()
            content = result.text
            json_dict = json.loads(content)
            worksheet.write(line, 0, json_dict['pois'][k]['name'])
            worksheet.write(line, 1, json_dict['pois'][k]['location'])
            worksheet.write(line, 2, json_dict['pois'][k]['type'])
            print("数据正在获取中，请耐心等待。")
            k = k + 1
        except:
            try:
                test = requests.get(test_url)
                test.raise_for_status()
                print("数据获取完成，请至爬虫目录下查看。")
                page = 1000
                k = 1000
            except:
                print("数据获取失败，请检查网络连接。")
                page = 1000
                k = 1000
    page = page + 1

# 保存文件
workbook.save(file_name)