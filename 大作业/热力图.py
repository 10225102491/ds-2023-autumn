from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd

def china_map(data_pair):
    Map(init_opts=opts.InitOpts(theme='white', width='1280px', height='720px')
        ).add(series_name="",
              data_pair=data_pair,
              maptype="china",
              label_opts=opts.LabelOpts(is_show=True, position='inside', ), is_map_symbol_show=False,
              ).set_global_opts(
        title_opts=opts.TitleOpts(
            title="中国大学分布 热力图",
            pos_left="center",
            pos_top="20",
            title_textstyle_opts=opts.TextStyleOpts(
                font_size=28,
                font_family="Microsoft YaHei", ),
        ),
        tooltip_opts=opts.TooltipOpts(
            is_show=True,
            formatter="{b} : 现有{c}所高校",
        ),
        visualmap_opts=opts.VisualMapOpts(
            is_piecewise=True,
            dimension=0,
            pos_left="10",
            pos_bottom="20",
            pieces=[
                {'max': 49, 'min': 0, 'label': '0-49', 'color': '#FFFFFF'},
                {'max': 99, 'min': 50, 'label': '50-99', 'color': '#FFFFCC'},
                {'max': 149, 'min': 100, 'label': '100-149', 'color': '#FFC4B3'},
                {'max': 199, 'min': 150, 'label': '150-199', 'color': '#FF9985'},
                {'max': 249, 'min': 200, 'label': '200-249', 'color': '#F57567'},
                {'max': 299, 'min': 250, 'label': '250-299', 'color': '#E64546'},
                {'max': 349, 'min': 300, 'label': '300-349', 'color': '#B80909'},
                {'max': 399, 'min': 350, 'label': '350-399', 'color': '#8A0808'},
                {'max': 1000, 'min': 400, 'label': '>=400', 'color': '#660000'}
            ]
        )
    ).render('中国大学分布.html')


if __name__ == '__main__':
    df = pd.read_csv('大学.csv')  # 利用pandas读取数据
    print(df)
    citys = {}
    for i in df["大学所在地"]:
        if i == '北京' or i == '天津' or i == '上海' or i == '重庆':
            i += '市'
        elif i == '西藏' or i == '内蒙古':
            i += '自治区'
        elif i == '新疆':
            i += '维吾尔自治区'
        elif i == '广西':
            i += '壮族自治区'
        elif i == '宁夏':
            i += '回族自治区'
        else:
            i += '省'
        if i in citys:
            citys[i] += 1
        else:
            citys[i] = 1
    City_list = citys.keys() # 各省/区的名字列表
    data_list = citys.values()  # 数据
    data_pair = [x for x in zip(City_list, data_list)]
    print(data_pair)
china_map(data_pair)