import json
import requests
import jsonpath
from pyecharts.charts import Map, Geo, Bar, Page, Pie
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType

url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# 获取到各个国家疫情数据
resp = requests.post(url)
# 提取数据,先把json类型转成字典
data = json.loads(resp.text)
country = jsonpath.jsonpath(data, "$..name")  # 国家名称
confirm = jsonpath.jsonpath(data, "$..confirm")  # 累计确诊
confirmAdd = jsonpath.jsonpath(data, "$..confirmAdd")  # 新增
nowConfirm = jsonpath.jsonpath(data, "$..nowConfirm")  # 当前确诊
showContent = []
china_url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5'
json_text = requests.get(china_url).json()
data = json.loads(json_text['data'])
china_confirm = data['chinaTotal']['confirm']
country.append('中国')
confirm.append(china_confirm)
data_list = list(zip(country, confirm))
# 数据可视化 把今天各国的确诊人数用世界地图的方式展示
# pyecharts有比较好的动态效果 静态可选用matplotlib
nameMap = {
    'Afghanistan': '阿富汗',
    'Albania': '阿尔巴尼亚',
    'Algeria': '阿尔及利亚',
    'Andorra': '安道尔',
    'Angola': '安哥拉',
    'Antarctica': '南极洲',
    'Antigua and Barbuda': '安提瓜和巴布达',
    'Argentina': '阿根廷',
    'Armenia': '亚美尼亚',
    'Australia': '澳大利亚',
    'Austria': '奥地利',
    'Azerbaijan': '阿塞拜疆',
    'The Bahamas': '巴哈马',
    'Bahrain': '巴林',
    'Bangladesh': '孟加拉国',
    'Barbados': '巴巴多斯',
    'Belarus': '白俄罗斯',
    'Belgium': '比利时',
    'Belize': '伯利兹',
    'Benin': '贝宁',
    'Bermuda': '百慕大',
    'Bhutan': '不丹',
    'Bolivia': '玻利维亚',
    'Bosnia and Herzegovina': '波斯尼亚和黑塞哥维那',
    'Botswana': '博茨瓦纳',
    'Brazil': '巴西',
    'Brunei': '文莱',
    'Bulgaria': '保加利亚',
    'Burkina Faso': '布基纳法索',
    'Burundi': '布隆迪',
    'Cambodia': '柬埔寨',
    'Cameroon': '喀麦隆',
    'Canada': '加拿大',
    'Cape Verde': '佛得角',
    'Central African Rep.': '中非共和国',
    'Chad': '乍得',
    'Chile': '智利',
    'China': '中国',
    'Colombia': '哥伦比亚',
    'Congo': '刚果（布）',
    'Comoros': '科摩罗',
    'Republic of the Congo': '刚果共和国',
    'Costa Rica': '哥斯达黎加',
    'Croatia': '克罗地亚',
    'Cuba': '古巴',
    'Cyprus': '塞浦路斯',
    'Czech Republic': '捷克共和国',
    'Denmark': '丹麦',
    'Dem. Rep. Congo': '刚果（金）',
    'Dem. Rep. Korea': '朝鲜',
    'Djibouti': '吉布提',
    'Dominica': '多米尼加',
    'Dominican Republic': '多明尼加共和国',
    'Ecuador': '厄瓜多尔',
    'Egypt': '埃及',
    'El Salvador': '萨尔瓦多',
    'Equatorial Guinea': '赤道几内亚',
    'Eritrea': '厄立特里亚',
    'Estonia': '爱沙尼亚',
    'Ethiopia': '埃塞俄比亚',
    'Falkland Islands': '福克兰群岛',
    'Faroe Islands': '法罗群岛',
    'Fiji': '斐济',
    'Finland': '芬兰',
    'France': '法国',
    'French Guiana': '法属圭亚那',
    'French Southern and Antarctic Lands': '法属南半球和南极领地',
    'Gabon': '加蓬',
    'Gambia': '冈比亚',
    'Gaza Strip': '加沙',
    'Georgia': '格鲁吉亚',
    'Germany': '德国',
    'Ghana': '加纳',
    'Greece': '希腊',
    'Greenland': '格陵兰',
    'Grenada': '格林纳达',
    'Guadeloupe': '瓜德罗普',
    'Guatemala': '危地马拉',
    'Guinea': '几内亚',
    'Guinea Bissau': '几内亚比绍',
    'Guyana': '圭亚那',
    'Haiti': '海地',
    'Honduras': '洪都拉斯',
    'Hong Kong': '香港',
    'Hungary': '匈牙利',
    'Iceland': '冰岛',
    'India': '印度',
    'Indonesia': '印度尼西亚',
    'Iran': '伊朗',
    'Iraq': '伊拉克',
    'Iraq-Saudi Arabia Neutral Zone': '伊拉克阿拉伯中立区',
    'Ireland': '爱尔兰',
    'Isle of Man': '马恩岛',
    'Israel': '以色列',
    'Italy': '意大利',
    'Ivory Coast': '科特迪瓦',
    'Jamaica': '牙买加',
    'Jan Mayen': '扬马延岛',
    'Japan': '日本本土',
    'Jordan': '约旦',
    'Kazakhstan': '哈萨克斯坦',
    'Kenya': '肯尼亚',
    'Kerguelen': '凯尔盖朗群岛',
    'Kiribati': '基里巴斯',
    'North Korea': '北朝鲜',
    'Korea': '韩国',
    'Kuwait': '科威特',
    'Kyrgyzstan': '吉尔吉斯斯坦',
    'Laos': '老挝',
    'Latvia': '拉脱维亚',
    'Lebanon': '黎巴嫩',
    'Lesotho': '莱索托',
    'Liberia': '利比里亚',
    'Libya': '利比亚',
    'Liechtenstein': '列支敦士登',
    'Lithuania': '立陶宛',
    'Luxembourg': '卢森堡',
    'Macau': '澳门',
    'Macedonia': '马其顿',
    'Madagascar': '马达加斯加',
    'Malawi': '马拉维',
    'Malaysia': '马来西亚',
    'Maldives': '马尔代夫',
    'Mali': '马里',
    'Malta': '马耳他',
    'Martinique': '马提尼克',
    'Mauritania': '毛里塔尼亚',
    'Mauritius': '毛里求斯',
    'Mexico': '墨西哥',
    'Moldova': '摩尔多瓦',
    'Monaco': '摩纳哥',
    'Mongolia': '蒙古',
    'Morocco': '摩洛哥',
    'Mozambique': '莫桑比克',
    'Myanmar': '缅甸',
    'Namibia': '纳米比亚',
    'Nepal': '尼泊尔',
    'Netherlands': '荷兰',
    'New Caledonia': '新喀里多尼亚',
    'New Zealand': '新西兰',
    'Nicaragua': '尼加拉瓜',
    'Niger': '尼日尔',
    'Nigeria': '尼日利亚',
    'Northern Mariana Islands': '北马里亚纳群岛',
    'Norway': '挪威',
    'Oman': '阿曼',
    'Pakistan': '巴基斯坦',
    'Panama': '巴拿马',
    'Papua New Guinea': '巴布亚新几内亚',
    'Paraguay': '巴拉圭',
    'Peru': '秘鲁',
    'Philippines': '菲律宾',
    'Poland': '波兰',
    'Portugal': '葡萄牙',
    'Puerto Rico': '波多黎各',
    'Qatar': '卡塔尔',
    'Reunion': '留尼旺岛',
    'Romania': '罗马尼亚',
    'Russia': '俄罗斯',
    'Rwanda': '卢旺达',
    'San Marino': '圣马力诺',
    'Sao Tome and Principe': '圣多美和普林西比',
    'Saudi Arabia': '沙特阿拉伯',
    'Senegal': '塞内加尔',
    'Seychelles': '塞舌尔',
    'Sierra Leone': '塞拉利昂',
    'Singapore': '新加坡',
    'Slovakia': '斯洛伐克',
    'Slovenia': '斯洛文尼亚',
    'Solomon Islands': '所罗门群岛',
    'Somalia': '索马里',
    'South Africa': '南非',
    'Spain': '西班牙',
    'Sri Lanka': '斯里兰卡',
    'St. Christopher-Nevis': '圣',
    'St. Lucia': '圣露西亚',
    'St. Vincent and the Grenadines': '圣文森特和格林纳丁斯',
    'Sudan': '苏丹',
    'Suriname': '苏里南',
    'Svalbard': '斯瓦尔巴特群岛',
    'Swaziland': '斯威士兰',
    'Sweden': '瑞典',
    'Switzerland': '瑞士',
    'Syria': '叙利亚',
    'Tanzania': '坦桑尼亚',
    'Taiwan': '台湾',
    'Tajikistan': '塔吉克斯坦',
    'United Republic of Tanzania': '坦桑尼亚',
    'Thailand': '泰国',
    'Togo': '多哥',
    'Tonga': '汤加',
    'Trinidad and Tobago': '特里尼达和多巴哥',
    'Tunisia': '突尼斯',
    'Turkey': '土耳其',
    'Turkmenistan': '土库曼斯坦',
    'Turks and Caicos Islands': '特克斯和凯科斯群岛',
    'Uganda': '乌干达',
    'Ukraine': '乌克兰',
    'United Arab Emirates': '阿联酋',
    'United Kingdom': '英国',
    'United States': '美国',
    'Uruguay': '乌拉圭',
    'Uzbekistan': '乌兹别克斯坦',
    'Vanuatu': '瓦努阿图',
    'Venezuela': '委内瑞拉',
    'Vietnam': '越南',
    'Western Sahara': '西撒哈拉',
    'Western Samoa': '西萨摩亚',
    'Yemen': '也门',
    'Yugoslavia': '南斯拉夫',
    'Democratic Republic of the Congo': '刚果民主共和国',
    'Zambia': '赞比亚',
    'Zimbabwe': '津巴布韦',
    'South Sudan': '南苏丹',
    'Somaliland': '索马里兰',
    'Montenegro': '黑山',
    'Kosovo': '科索沃',
    'Republic of Serbia': '塞尔维亚',
}
page = Page(layout=Page.DraggablePageLayout)
map = Map(init_opts=opts.InitOpts(width='1300px', height='600px',theme=ThemeType.LIGHT),)\
    .add(
    series_name="世界疫情分布",
    data_pair=data_list,
    maptype="world",
    is_map_symbol_show=False,
    name_map=nameMap
)

# 设置默认不显示全部国家名称
map.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
# 设置全局配置项
map.set_global_opts(visualmap_opts=opts.VisualMapOpts(max_=24668541,is_piecewise=True))
#map.render('世界疫情分布情况.html')



# country = jsonpath.jsonpath(data, "$..name")  # 国家名称
# confirm = jsonpath.jsonpath(data, "$..confirm")  # 累计确诊
# confirmAdd = jsonpath.jsonpath(data, "$..confirmAdd")  # 新增
# nowConfirm = jsonpath.jsonpath(data, "$..nowConfirm")  # 当前确诊
bar1 = (
        Bar(init_opts=opts.InitOpts(width='1300px', height='600px', theme=ThemeType.MACARONS), )
            .add_xaxis(country[0:30])
            .add_yaxis("当前确诊", nowConfirm[0:30])
            .set_series_opts(
            itemstyle_opts={
                "normal": {
                    "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 0,
                            color: '#69FF97'
                        }, {
                            offset: 1,
                            color: '#00E4FF'
                        }], false)"""),
                    "barBorderRadius": [6, 6, 6, 6],
                    "shadowColor": 'rgb(0, 160, 221)',
                }},
            markpoint_opts=opts.MarkPointOpts(
                data=[
                    opts.MarkPointItem(type_="max", name="最大值"),
                    opts.MarkPointItem(type_="min", name="最小值"),
                ]
            ), markline_opts=opts.MarkLineOpts(
                data=[
                    opts.MarkLineItem(type_="min", name="最小值"),
                    opts.MarkLineItem(type_="max", name="最大值")
                ]
            ))
            .set_global_opts(toolbox_opts=opts.ToolboxOpts(is_show=True),
                             xaxis_opts=opts.AxisOpts(axistick_opts=opts.AxisTickOpts(is_show=True),
                                                      axislabel_opts=opts.LabelOpts(rotate=-90)
                                                      ),
                             title_opts=opts.TitleOpts(title="疫情当前确诊柱状图")

                             )

    )
confirm_info=[]
for i,j,k in zip(country,confirmAdd,confirm):
    z={
        'country':i,
        'confirmAdd':j,
        'confirm':k,
    }
    confirm_info.append(z)
def takeSecond(elem):
    return elem['confirmAdd']


confirm_info.sort(key=takeSecond,reverse=True)

country_1=[]
confirmAdd_1=[]
confirm_1=[]

for i in confirm_info:
    country_1.append(i['country'])
    confirmAdd_1.append(i['confirmAdd'])
    confirm_1.append(i['confirm'])
bar2 = (
        Pie(init_opts=opts.InitOpts(width='1300px', height='600px', theme=ThemeType.LIGHT))
            .add(
            '累计确诊',
            [list(z) for z in zip(country_1[0:10], confirm_1[0:10])],
            radius=[0, "30%"],
            center=["59%", "50%"],
            label_opts=opts.LabelOpts(position="inner", is_show=False),
        )
            .add(
            '每日新增',
            [list(z) for z in zip(country_1[0:10], confirmAdd_1[0:10])],
            radius=["40%", "75%"],
            center=["59%", "50%"],
            rosetype="radius",
            label_opts=opts.LabelOpts(is_show=True,
                                      # position 标签的位置
                                      position="outside",
                                      # 回调函数，回调函数格式：
                                      # (params: Object|Array) => string
                                      # 设置标签的显示样式
                                      formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
                                      # 背景颜色
                                      background_color="#eee",
                                      # 边框颜色
                                      border_color="#aaa",
                                      # 边框宽度
                                      border_width=1,
                                      # 边框四角弧度
                                      border_radius=4,

                                      rich={
                                          "a": {"color": "#999",
                                                "lineHeight": 22,
                                                "align": "center"  # 对齐方式
                                                },

                                          "abg": {
                                              "backgroundColor": "#e3e3e3",
                                              "width": "100%",
                                              "align": "right",
                                              "height": 22,
                                              "borderRadius": [4, 4, 0, 0],
                                          },

                                          "hr": {
                                              "borderColor": "#aaa",
                                              "width": "100%",
                                              "borderWidth": 0.5,
                                              "height": 0,
                                          },

                                          "b": {"fontSize": 16,
                                                "lineHeight": 33
                                                },

                                          # 百分比
                                          "per": {
                                              "color": "#eee",  # 字体颜色
                                              "backgroundColor": "#334455",  # 背景颜色
                                              "padding": [2, 4],
                                              "borderRadius": 2,
                                          },
                                      },
                                      ),
        )
            .set_global_opts(
            # toolbox_opts=opts.ToolboxOpts(is_show=True),
            title_opts=opts.TitleOpts(title="全球疫情每日新增饼图"),
            legend_opts=opts.LegendOpts(
                orient="vertical",  # 图例垂直放置
                pos_top="15%",  # 图例位置调整
                pos_left="2%"),
        )
    )
page.add(map, bar1,bar2)
page.render('全球疫情分析可视化.html')





