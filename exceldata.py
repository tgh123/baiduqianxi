import xlrd
from pyecharts.charts import Geo
# 导入配置项
from pyecharts import options as opts
# ChartType：图标类型，SymbolType：标记点类型
from pyecharts.globals import ChartType, SymbolType

# import matplotlib

path = '广西地市区内迁徙数据'


def in_data(city, date_number):
	workbook = xlrd.open_workbook(f'.\\{path}\\{city}-迁入来源地规模指数.xlsx')
	sheet = workbook.sheet_by_index(0)
	city_od_list = []
	city_od_values = []
	a = 0
	cols = sheet.col_values(1)[1:]
	cols_date = sheet.col_values(date_number + 1)[1:]
	for j in cols:
		city_od = (j, city)
		city_od_v = (j, cols_date[a])
		city_od_list.append(city_od)
		city_od_values.append(city_od_v)
		a += 1
	geo = Geo()
	# 地图类型，世界地图可换为world
	geo.add_schema(maptype="广西")
	# 添加数据点
	geo.add("%", city_od_values, type_=ChartType.EFFECT_SCATTER)
	# 添加流向，type_设置为LINES，涟漪配置为箭头，提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',
	# 'diamond', 'pin', 'arrow', 'none'
	geo.add("迁入城市", city_od_list, type_=ChartType.LINES,
	        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=5, color="yellow"),
	        linestyle_opts=opts.LineStyleOpts(curve=0.2), is_large=True)
	# 不显示标签
	geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
	# 设置图标标题，visualmap_opts=opts.VisualMapOpts()为左下角的视觉映射配置项
	geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title=f"{city}迁入数据"))
	# 直接在notebook里显示图表
	geo.render_notebook()
	# 生成html文件，可传入位置参数
	geo.render(f".\\in_od\\{city}-2020.10.{date_number}迁入OD图.html")


def out_data(city, date_number):
	workbook = xlrd.open_workbook(f'.\\{path}\\{city}-迁出目的地规模指数.xlsx')
	sheet = workbook.sheet_by_index(0)
	city_od_list = []
	city_od_values = []
	a = 0
	cols = sheet.col_values(1)[1:]
	cols_date = sheet.col_values(date_number + 1)[1:]
	for j in cols:
		city_od = (city, j)
		city_od_v = (j, cols_date[a])
		city_od_list.append(city_od)
		city_od_values.append(city_od_v)
		a += 1
	geo = Geo()
	# 地图类型，世界地图可换为world
	geo.add_schema(maptype="广西")
	# 添加数据点
	geo.add("%", city_od_values, type_=ChartType.EFFECT_SCATTER)
	# 添加流向，type_设置为LINES，涟漪配置为箭头，提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',
	# 'diamond', 'pin', 'arrow', 'none'
	geo.add("迁出城市", city_od_list, type_=ChartType.LINES,
	        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=5, color="yellow"),
	        linestyle_opts=opts.LineStyleOpts(curve=0.2), is_large=True)
	# 不显示标签
	geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
	# 设置图标标题，visualmap_opts=opts.VisualMapOpts()为左下角的视觉映射配置项
	geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title=f"{city}迁出数据"))
	# 直接在notebook里显示图表
	geo.render_notebook()
	# 生成html文件，可传入位置参数
	geo.render(f".\\out_od\\{city}-2020.10.{date_number}迁出OD图.html")


if __name__ == '__main__':
	number = int(input('请输入日期：（1-8）代表2020.10.1--2020.10.8:'))
	city_list = (
		'南宁市',
		'柳州市',
		'桂林市',
		'梧州市',
		'北海市',
		'防城港市',
		'钦州市',
		'贵港市',
		'玉林市',
		'百色市',
		'贺州市',
		'河池市',
		'来宾市',
		'崇左市'
	)
	for i in city_list:
		in_data(i, number)
		out_data(i, number)
