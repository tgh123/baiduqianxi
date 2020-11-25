# 导入Geo包，注意1.x版本的导入跟0.x版本的导入差别
from pyecharts.charts import Geo
# 导入配置项
from pyecharts import options as opts
# ChartType：图标类型，SymbolType：标记点类型
from pyecharts.globals import ChartType, SymbolType

geo = Geo()

# 地图类型，世界地图可换为world
geo.add_schema(maptype="广西")
# 添加数据点
geo.add("",
        [
         ('南宁市', 450100), ('柳州市', 450200), ('桂林市', 450300), ('梧州市', 450400), ('北海市', 450500), ('防城港市', 450600), ('钦州市', 450700),
         ('贵港市', 450800), ('玉林市', 450900), ('百色市', 451000), ('贺州市', 451100), ('河池市', 451200), ('来宾市', 451300), ('崇左市', 451400)],
        type_=ChartType.EFFECT_SCATTER)
# 添加流向，type_设置为LINES，涟漪配置为箭头，提供的标记类型包括 'circle', 'rect', 'roundRect', 'triangle',
# 'diamond', 'pin', 'arrow', 'none'
geo.add("geo-lines",
        [
         ('南宁市', '钦州市'), ('柳州市', '钦州市'), ('桂林市', '钦州市'), ('梧州市', '钦州市'), ('北海市', '钦州市'), ('防城港市', '钦州市'),
         ('钦州市', '钦州市'),
         ('贵港市', '钦州市'), ('玉林市', '钦州市'), ('百色市', '钦州市'), ('贺州市', '钦州市'), ('河池市', '钦州市'), ('来宾市', '钦州市'),
         ('崇左市', '钦州市')
         ],
        type_=ChartType.LINES,
        effect_opts=opts.EffectOpts(symbol=SymbolType.ARROW, symbol_size=5, color="yellow"),
        linestyle_opts=opts.LineStyleOpts(curve=0.2),
        is_large=True)
# 不显示标签
geo.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 设置图标标题，visualmap_opts=opts.VisualMapOpts()为左下角的视觉映射配置项
geo.set_global_opts(visualmap_opts=opts.VisualMapOpts(), title_opts=opts.TitleOpts(title="广西地市迁徙数据"))
# 直接在notebook里显示图表
geo.render_notebook()
# 生成html文件，可传入位置参数
geo.render("gx.html")
