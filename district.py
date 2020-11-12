"""
project name:广西地市区内迁徙数据
@author: 华仔
"""
# 城市级别迁徙网址：
# http://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id=450100&type=move_in&date=20201109&callback=jsonp_1605065779528_211199
# 省份级别迁徙网址：
# http://huiyan.baidu.com/migration/provincerank.jsonp?dt=city&id=450100&type=move_in&date=20201109&callback=jsonp_1605065826250_1163380
# 历史迁徙记录：
# http://huiyan.baidu.com/migration/historycurve.jsonp?dt=city&id=450100&type=move_in&callback=jsonp_1605065778688_3249988
import requests
import json
import time
import xlsxwriter
from citycode import GxCode

headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36'
}


def city_migration(file_title, direction, code):
	if direction == 'in':
		migration = '迁入来源地'
	else:
		migration = '迁出目的地'
	workbook = xlsxwriter.Workbook(f'广西地市区内迁徙数据\\{file_title}-{migration}规模指数.xlsx')
	worksheet = workbook.add_worksheet('sheet')
	city_order = {}
	lines = 1
	city_list = []
	counter_data = 2  # 日期表头
	worksheet.write(0, 0, '城市代码')
	worksheet.write(0, 1, migration)
	for key, value in GxCode.items():
		worksheet.write(lines, 0, str(value))
		worksheet.write(lines, 1, str(key))
		city_order[str(key)] = lines
		lines += 1
		city_list.append(key)
	for date in range(20201001, 20201009):
		date_time = date
		url = f'http://huiyan.baidu.com/migration/cityrank.jsonp?dt=city&id={code}&type=move_{direction}&date={date_time}'
		response = requests.get(url, headers=headers, timeout=10)
		time.sleep(3)
		r = response.text[4:-1]
		print(url)
		data_dict = json.loads(r)
		if data_dict['errmsg'] == 'SUCCESS':
			data_list = data_dict['data']['list']
			worksheet.write(0, counter_data, ('D' + str(date_time)))
			for a in range(len(GxCode)):
				worksheet.write(a + 1, counter_data, 0)  # 先把当前日期下该列所有城市值置0
			# 获取数据
			for i in range(len(data_list)):
				city_name = data_list[i]['city_name']  # 城市名
				if city_name in city_list:
					value = data_list[i]['value']  # 当日迁徙量所占百分比值
					worksheet.write(city_order[str(city_name)], counter_data, value)  # 查找城市序号字典，在对应的行里写入相应的值
				else:
					pass
			counter_data += 1  # 日期计数器自加一
	workbook.close()  # 保存


if __name__ == '__main__':
	dict1 = {
		'南宁市': 450100, '柳州市': 450200,
		'桂林市': 450300, '梧州市': 450400, '北海市': 450500, '防城港市': 450600, '钦州市': 450700,
		'贵港市': 450800, '玉林市': 450900, '百色市': 451000, '贺州市': 451100, '河池市': 451200, '来宾市': 451300,
		'崇左市': 451400,
	}
	ways = ['in', 'out']
	for way in ways:
		if way == 'in':
			way_name = '迁入'
		else:
			way_name = '迁出'
		for key, value in dict1.items():
			city_name = key
			code_number = value
			time.sleep(5)
			city_migration(city_name, way, code_number)
			print(city_name + '--' + way_name + '--', '完成')
